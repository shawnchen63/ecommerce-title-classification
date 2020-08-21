from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
from model_api import Model

import memory_profiler as mp

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "ML React App", 
		  description = "Predict results using a trained model")

name_space = app.namespace('prediction', description='Prediction APIs')

flask_model = app.model('Prediction params', 
				  {'query': fields.String(required = True, 
				  							   description="Product Title", 
    					  				 	   help="Product Title cannot be blank"),
				  'big_category': fields.Integer(required = True, 
				  							description="One of [1, 2 ,3], corresponding to beauty, fashion and mobile", 
    					  				 	help="Big category cannot be blank")})

model = Model()

# classifier = joblib.load('classifier.joblib')

@name_space.route("/")
class MainClass(Resource):

	def options(self):
		response = make_response()
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add('Access-Control-Allow-Headers', "*")
		response.headers.add('Access-Control-Allow-Methods', "*")
		return response

	@app.expect(flask_model)
	#@mp.profile		
	def post(self):
		try: 
			formData = request.json
			data = [val for val in formData.values()]
			predicted_category = model.predict(data[0], int(data[1]))
			response = jsonify({
				"statusCode": 200,
				"status": "Prediction made",
				"category": predicted_category
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			return response
		except Exception as error:
			response = jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"category": "Error: " + str(error),
				"error": str(error)
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			return response