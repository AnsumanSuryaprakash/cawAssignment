from flask import request
from jwcrypto import jwt, jwk
import json
import jsonpatch
import os
from jsonpatch import InvalidJsonPatch



def patch():
	# getting the inputs from request body
	request_object = request.get_json()
	username = request_object.get('username')
	token = request_object.get('token',None)
	json_object = request_object.get('json_object')
	json_patch_object = request_object.get('json_patch_object')

	# sanity checks 
	if not json_object or not json_patch_object:
		return "420 Not all required parameters are passed"
	if not token:
		return "403 No JWT token present in request"
	_key = os.environ.get('Secret_Key')
	key = jwk.JWK(**json.loads(_key))
	encrypted_token = jwt.JWT(key=key, jwt=token)
	signed_token = jwt.JWT(key=key, jwt=encrypted_token.claims)
	token_username = signed_token.claims['username']

	if username != token_username:
		return "401 User is not authorized for the request"

	#Applying the patch and returning the result or if we get error it return 418
	try:
		patch = jsonpatch.JsonPatch.from_string(json_patch_object)
		result = patch.apply(json_object)
		return result
	except InvalidJsonPatch:
		return "418 passed json patch object is invalid"

