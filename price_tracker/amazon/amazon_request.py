import signature
import urllib
import requests
import datetime
from BeautifulSoup import BeautifulSoup as bs
import xml.etree.ElementTree as ET
import MySQLdb
import time as time_lib 
import sys
import md5

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
		user="stuff",         # your username
		passwd="super_secure_password",  # your password
		db="stuff_and_things")        # name of the data base

cur = db.cursor()

Response_Groups = urllib.quote("Large")

f = open('secret.txt', 'r')
secret = f.read().rstrip('\n')
f.close()
f = open('access.txt', 'r')
Access_Key = f.read().rstrip('\n')
f.close()

item = sys.argv[1]

item_id = urllib.quote(item)
time = urllib.quote(datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z")

request_url = "AWSAccessKeyId="+Access_Key+"&AssociateTag=stuffandthi03-20&ItemId="+item_id+"&Operation=ItemLookup&ResponseGroup="+Response_Groups+"&Timestamp="+time

to_sign = """GET
webservices.amazon.com
/onca/xml
"""+request_url;

sig = signature.encode_that_shit(signature.sign_that_shit(to_sign, secret))

r = requests.get("http://webservices.amazon.com/onca/xml?"+request_url+"&Signature="+sig)
res = r.text
tree = ET.fromstring(res)
thing = bs(res)

brand =  tree[1][1][8].find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Brand').text
title_tmp = tree[1][1][8].find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Title').text

#for idx, child in enumerate(tree[1][1][10][3][1][1]):
#	tmp = str(child)
#	one = tmp.replace("<Element '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}","")
#	two = one.split("'",1)[0]
#	print two + " " + str(idx)
#	print child.text
#	print "\n"
cur.execute("SELECT `Processed` FROM `Item_Name_Lookup` WHERE `Raw` = '"+title_tmp+"'")

title = cur.fetchone()[0]
timestamp = str(datetime.datetime.utcnow())

m = md5.new()
m.update(brand)
m.update(title)
m.update("amazon")
md5_hash = m.hexdigest()

list_price = tree[1][1][10][3][1][1].find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}FormattedPrice').text

#print "Hash: "+md5_hash
#print "Title: "+title
#print "Brand: "+brand
#print "Best New: "+list_price
cur.execute("UPDATE `Item_List` SET `Current`=0 and `End_Date`='"+timestamp+"' WHERE `Current`=1 AND `Hash_Code`='"+md5_hash+"' AND `Price` <> '"+list_price+"' AND `Condition`='New'")
cur.execute("INSERT IGNORE INTO `Item_List`(`Hash_Code`, `Manufacturer`, `Item Name`, `Price`, `Retailer`, `Condition`, `Current`, `Start_Date`) VALUES ('"+md5_hash+"','"+brand+"','"+title+"','"+list_price+"','Amazon','New',1,'"+timestamp+"')")

list_price = tree[1][1][9][1].find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}FormattedPrice').text
cur.execute("UPDATE `Item_List` SET `Current`=0 and `End_Date`='"+timestamp+"' WHERE `Current`=1 AND `Hash_Code`='"+md5_hash+"' AND `Price` <> '"+list_price+"' AND `Condition`='Used'")
cur.execute("INSERT IGNORE  INTO `Item_List`(`Hash_Code`, `Manufacturer`, `Item Name`, `Price`, `Retailer`, `Condition`, `Current`, `Start_Date`) VALUES ('"+md5_hash+"','"+brand+"','"+title+"','"+list_price+"','Amazon','Used',1,'"+timestamp+"')")

db.commit()

db.close()
