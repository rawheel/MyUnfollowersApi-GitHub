import requests
from pprint import pprint
import threading
import math
import json
import Load_followers
from Load_followers import *
from flask import Flask
from flask_restful import Api, Resource,reqparse,abort
from flask import jsonify
from flask import request
app = Flask(__name__)
#api = Api(app)


#class GithubFollowers(Resource):
@app.route('/',methods=['GET'])
def home():
    username = str(request.args['username'])
    #(username)
    try:
        coming = compare_followers(username)
        print(coming)
        return jsonify(coming)
    except Exception as e:
        #return e
        #print(e)
        abort(400,message="Max Retiries exceeded with URL, take a break man...")

def load_prev_followers():
    read = open("data.txt","r")
    prev_data = json.load(read)
    return prev_data
    #print(self.data)
def load_recent_followers(username):

    load_followers = Load_followers(username)
    print(f"total followers: {str(load_followers.total)}")
    recent_data = load_followers.get_followers()
    with open('data.txt', 'w') as outfile:
        json.dump(recent_data, outfile)
    return recent_data


def save_data_for_first_time(username):

    load_followers = Load_followers(username)
    #print(f"total followers: {str(load_followers.total)}")
    data = load_followers.get_followers()
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)


def compare_followers(username):
    #print(f'Processing {self.username}',end='')
    #print(emoji.emojize(' :man_technologist:'))
    try:
        read = open("data.txt","r")
        prev_data = json.load(read)
        prev_username = [i for i in prev_data]

        if prev_username[0]==username:
            prev_followers = load_prev_followers()
            recent_followers = load_recent_followers(username)


            prev_set = set(prev_followers[username])
            recent_set = set(recent_followers[username])

            newfollowers = prev_set-recent_set
            unfollowers = recent_set - prev_set

            data  ={}
            data["unfollowers"] = "Congrats,No one unfollowed you"
            data["newfollowers"] = "Help a person,Get a new Follower"


            if unfollowers:
                #print(emoji.emojize('Following Folk/s unfollowed you :pensive_face:'))
                #no=0
                #[print(f'{no+1}) {u}') for no,u in enumerate(unfollowers)]
                #print()

                data["unfollowers"] = list(unfollowers)

                #print(emoji.emojize("Congrats,No one unfollowed you :grinning_face_with_big_eyes:"))
            if newfollowers:
                #print(emoji.emojize("Following Folk/s recently started following you :smiling_face_with_heart-eyes:"))
                #no=0
                #[print(f'{no+1}) {n}') for no,n in enumerate(newfollowers)]
                data["newfollowers"] = list(newfollowers)


                #print(emoji.emojize("Help a person,Get a new Follower :smiling_face_with_halo:"))
            #print(data)

            return data

            #return json.dumps(data)
        else:
            save_data_for_first_time(username)

            #print(emoji.emojize(":check_mark: Your username & Followers have been added for later use!"))
            return {"message": "Your username & Followers have been added for later use!"}


    except Exception as e:
        save_data_for_first_time(username)
        #print(emoji.emojize(":check_mark: Your username & Followers have been added for later use!"))
        #print(e)

        return {"message": "Your username & Followers have been added for later use!"}


#api.add_resource(GithubFollowers,"/<string:username>")

if __name__ == "__main__":
	app.run(threaded= True,port=5000)

#main_object = GithubFollowers("wajahatkarim3")
#main_object.compare_followers()

