import signature
import urllib
import requests
import datetime
from BeautifulSoup import BeautifulSoup as bs

secret = "bepkWh672/YLnf182DzOd2xIAwkONeNq+vU1G6qX"

time = urllib.quote(datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z")

request_url = "AWSAccessKeyId=AKIAIYC74XQ54GX6L5YQ&AssociateTag=stuffandthi03-20&ItemId=B00008OE6I&Operation=ItemLookup&Timestamp="+time

to_sign = """GET
webservices.amazon.com
/onca/xml
"""+request_url;

sig = signature.encode_that_shit(signature.sign_that_shit(to_sign, secret))

r = requests.get("http://webservices.amazon.com/onca/xml?"+request_url+"&Signature="+sig)
print r.status_code

res = r.text

soup = bs(res)
print soup.prettify()
