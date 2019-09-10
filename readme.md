<h3>Setup of the project</h3> 
1. Install jwcrypto using pip install jwcrypto.</br>
2. open a python repl session and use the following code<br>
''' 
		from jwcrypto import jwk
		key = jwk.JWK(generate='oct', size=256)
		key.export()
'''

3. Add result to an environment varriable called 'Secret_Key'</br>
4. Create an virtual environment in python using virtualenv and activate it.<br>
5. Install the requirements 
'''
		pip install -r requirements.txt
'''
6. Start the app by navigating to app folder in the terminal and type <br>
'''
		python app.py

'''

<b>You can download the docker image from dockerhub using tag <em>ansuigit/casassignment</em></b>


This application has 3 endpoints 1 public endpoint and 2 protected endpoints.</br>

The public endpoint "/v1/obtain_token" would take username and password in the request body and generate and retrun a signed JWT token.</br>

The protected endpoint "/v1/json_patch" would require a JWT token and username along with a JSON object and a Json patch object as string, in the request body and return the patched JSON object in the response.</br>

The protected endpoint "/v1/generate_thumbnail" would require a JWT token and username along with a image URL and retruns a thumbnail of size 50x50 of the image downloaded from the URL.</br>




