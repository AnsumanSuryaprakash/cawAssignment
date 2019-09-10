from  flask import request
from jwcrypto import jwt, jwk
import json

import os

def post():
	request_object = request.get_json()
	username = request_object.get('username')
	password = request_object.get('password')

	payload = {
		'username': username,
	}
	
	_key = os.environ.get('Secret_Key')
	key = jwk.JWK(**json.loads(_key))



	# Creating an signed JWT token with JWK 
	try:
		Token = jwt.JWT(header={"alg":"HS256"},claims=payload)
		Token.make_signed_token(key)
		EToken = jwt.JWT(header={"alg":"A256KW", "enc":"A256CBC-HS512"},claims=Token.serialize())
		EToken.make_encrypted_token(key)
		return EToken.serialize()

	except Exception as e:
		return "Token couldn't be generated. Please try again."





