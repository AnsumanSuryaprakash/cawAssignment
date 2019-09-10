from connexion.resolver import RestyResolver
import connexion
import os 
from jwcrypto import jwk

import flask_monitoringdashboard as dashboard

SECRET_KEY = os.environ.get('Secret_Key')

if not SECRET_KEY:
	key = jwk.JWK(generate='oct', size=256)
	os.environ['Secret_Key'] = key.export()



if __name__ == '__main__':
	options = {"swagger_ui": False}
	app = connexion.App(__name__,specification_dir="../swager/",options=options)
	dashboard.config.init_from(file='../config.cfg')
	dashboard.bind(app)
	app.add_api('simple_microservice.yaml',resolver = RestyResolver('api'))
	app.run(9090)

    # options = {"swagger_ui": False}
    # app = connexion.FlaskApp(__name__, specification_dir='openapi/', options=options)
    # path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # path = os.path.join(path, "swager", "simple_microservice.yaml")
    # print(path)
    # app.add_api(path)


    