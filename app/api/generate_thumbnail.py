from flask import request
from jwcrypto import jwt, jwk
import json
import os
import validators
from io import BytesIO
import requests
from PIL import Image

def is_downloadable(url):
	#This method checks if the URL has an downloadable image or not. Parsing the header of the URL
	h = requests.head(url,allow_redirects=True)
	header = h.header
	content_type = header.get('content-type')
	if 'image' in content_type.lower():
		return True

	return False

def post():
	# getting the inputs from request body
	request_object = request.get_json()
	username = request_object.get('username')
	token = request_object.get('token',None)
	url = request_object.get('url')

	# sanity checks 
	if not url:
		return "420 Not all required parameters are passed"
	if not validators.url(url):
		return "415 unsupported media type"
	if not token:
		return "403 No JWT token present in request"
	_key = os.environ.get('Secret_Key')
	key = jwk.JWK(**json.loads(_key))
	encrypted_token = jwt.JWT(key=key, jwt=token)
	signed_token = jwt.JWT(key=key, jwt=encrypted_token.claims)
	token_username = signed_token.claims['username']

	if username != token_username:
		return "401 User is not authorized for the request"

	if not is_downloadable(url):
		return "415 unsupported Media Type."

	# downloading the image and sending the response thumbnail
	downloaded_image = requests.get(url)
	image = Image.open(BytesIO(downloaded_image.content))
	thumbnail = image.resize((50,50), Image.ANTIALIAS)

	return thumbnail
	


