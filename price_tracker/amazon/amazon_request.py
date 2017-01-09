import signature
import urllib
import requests
import datetime
from BeautifulSoup import BeautifulSoup as bs
import xml.etree.ElementTree as ET

secret = "bepkWh672/YLnf182DzOd2xIAwkONeNq+vU1G6qX"

time = urllib.quote(datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z")

item_id = "B01GX5YWAO"
Response_Groups = urllib.quote("ItemAttributes")

request_url = "AWSAccessKeyId=AKIAIYC74XQ54GX6L5YQ&AssociateTag=stuffandthi03-20&ItemId="+item_id+"&Operation=ItemLookup&ResponseGroup="+Response_Groups+"&Timestamp="+time

#print request_url

to_sign = """GET
webservices.amazon.com
/onca/xml
"""+request_url;

sig = signature.encode_that_shit(signature.sign_that_shit(to_sign, secret))

r = requests.get("http://webservices.amazon.com/onca/xml?"+request_url+"&Signature="+sig)
#print r.status_code

res = r.text

tree = ET.fromstring(res)

thing = bs(res)

#print thing.prettify()

print tree[1][1][4][12][2].text
