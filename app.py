import threading
from flask import Flask,abort
from flask import jsonify
from flask import request
from views import compare_followers
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/github/',methods=['GET'])

class Github(Resource):
    def get(self,username):
        try:
            result = compare_followers(username)
            #response = jsonify(result)
            #response.headers.add("Access-Control-Allow-Origin", "*")
            return result
        except Exception as e:
            print(e)
            abort(400,description="Max Retries exceeded with URL or Invalid Username! take a break man...")
api.add_resource(Github, '/githubapi/<string:username>')


'''
def github():
    username = str(request.args['username'])
    try:
        result = compare_followers(username)
        response = jsonify(result)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response 
    except Exception as e:
        print(e)
        abort(400,description="Max Retries exceeded with URL or Invalid Username! take a break man...")
'''


if __name__ == "__main__":
	#app.run(threaded= True,port=5000)
    app.run(debug=True)


