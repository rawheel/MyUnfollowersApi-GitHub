import threading
from flask import Flask,abort
from flask import jsonify
from flask_cors import CORS
from flask import request
from views import compare_followers
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/github/',methods=['GET'])

class Github(Resource):
    def get(self,username):
        try:
            #abort(400,description="Max Retries exceeded with URL or Invalid Username! take a break man...")
            #return 400
            result = compare_followers(username)
            return result
            #response = jsonify(result)
            #response.headers.add("Access-Control-Allow-Origin", "*")
            
        except Exception as e:
            abort(400,description="Max Retries exceeded with URL or Invalid Username! take a break man...")
            
api.add_resource(Github, '/githubapi/<string:username>')


if __name__ == "__main__":
	#app.run(threaded= True,port=5000)
    app.run(debug=True)


