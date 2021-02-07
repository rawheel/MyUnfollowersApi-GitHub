import sqlite3
from Load_followers import Load_followers
import models
from models import myunfollowersdb

def load_prev_followers(username):
    db = myunfollowersdb()
    return db.fetchUserData(username)

def load_recent_followers(username):

    load_followers = Load_followers(username)
    recent_data = load_followers.get_followers()
    username=[key for key in recent_data][0]
    db = myunfollowersdb()
    db.updateData(username,str(recent_data[username]))

    return recent_data

def save_data_for_first_time(username):
    
    load_followers = Load_followers(username)
    data = load_followers.get_followers()
    username=[key for key in data][0]

    db = myunfollowersdb()
    db.insertUser(username)
    db.insertData(db.cursor.lastrowid,str(data[username]))

def compare_followers(username):
    try:
        db = myunfollowersdb()
        if db.checkUsername(username):
            prev_followers = load_prev_followers(username)
            recent_followers = load_recent_followers(username)


            prev_set = set(prev_followers)
            recent_set = set(recent_followers[username])

            unfollowers = prev_set-recent_set
            newfollowers  = recent_set - prev_set

            data  ={}
            data["username"]=username
            data["unfollowers"] = "Congrats,No one unfollowed you"
            data["newfollowers"] = "Help a person,Get a new Follower"
            data["totalunfollowers"]=0
            data["totalnewfollowers"]=0
            data["totalfollowers"] = recent_followers["totalfollowers"]

            if unfollowers:
                data["unfollowers"] = list(unfollowers)
                data["totalunfollowers"] = len(list(unfollowers))
            if newfollowers:
                data["newfollowers"] = list(newfollowers)
                data["totalnewfollowers"] = len(list(newfollowers))
                
            return data
        else:
            save_data_for_first_time(username)
            return {"message": "Your username & Followers have been added for later use!"}


    except Exception as e:
        save_data_for_first_time(username)
        return {"message": "Your username & Followers have been added for later use!"}