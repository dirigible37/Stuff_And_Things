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
		user="wmohr",         # your username
		passwd="iamjonsnow99",  # your password
		db="wmohr")        # name of the data base

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

#brand =  tree[1][1][4].find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Brand').text
#title_tmp = tree[1][1][8].find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Title').text

#print "Title: "+title_tmp
#print "Best New: "+tree[1][1][9][0][2].text
#print "Best Used: "+tree[1][1][9][1][2].text

for idx, child in enumerate(tree[1][1]):
	tmp = str(child)
	one = tmp.replace("<Element '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}","")
	two = one.split("'",1)[0]
	print two + " " + str(idx)
	print child.text
	print "\n"

#cur.execute("SELECT `Processed` FROM `Item_Name_Lookup` WHERE `Raw` = '"+title_tmp+"'")

#title = cur.fetchone()[0]

#m = md5.new()
#m.update(brand)
#m.update(title)
#m.update("amazon")
#md5_hash = m.digest()

#print brand 
#print list_price
#print title

# Use all the SQL you like
#cur.execute("INSERT IGNORE INTO `Item_List`(`Hash_Code`,`Manufacturer`, `Item Name`, `Price`, `Retailer`) VALUES ('"+md5_hash+"','"+brand+"','"+title+"','"+list_price+"','Amazon')")

#db.commit()

db.close()
