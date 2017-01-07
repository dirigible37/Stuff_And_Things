import base64
import hashlib
import hmac
import urllib

def sign_that_shit(some_shit, secret):
	hash = hmac.new(secret, some_shit, digestmod=hashlib.sha256).digest()
	return base64.b64encode(hash)
	
def encode_that_shit(signed_shit):
	return urllib.quote(signed_shit)
