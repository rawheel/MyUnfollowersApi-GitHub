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

def compare_followers(username,prev_followers,recent_followers):
    test_flags = {'username_test':0,'unfollowers_test':0,'newfollowers_test':0}
    try:
        db = myunfollowersdb()
        if db.checkUsername(username):

            # COMMENTED FOR WHITE BOX TEST.
            #prev_followers = load_prev_followers(username)
            #recent_followers = load_recent_followers(username)
            #print(prev_followers,recent_followers,"oye")

            #prev_set = set(prev_followers)
            #recent_set = set(recent_followers[username])

            prev_set = set(prev_followers)
            recent_set = set(recent_followers)

            unfollowers = prev_set-recent_set
            newfollowers  = recent_set - prev_set

            '''data  ={}
            data["username"]=username
            data["unfollowers"] = "Congrats,No one unfollowed you"
            data["newfollowers"] = "Help a person,Get a new Follower"
            data["totalunfollowers"]=0
            data["totalnewfollowers"]=0
            data["totalfollowers"] = recent_followers["totalfollowers"]
            data["avatar_url"] = recent_followers["avatar_url"]'''

            if unfollowers:
                test_flags['unfollowers_test'] = 1
                #data["unfollowers"] = list(unfollowers)
                #data["totalunfollowers"] = len(list(unfollowers))
            if newfollowers:
                test_flags['newfollowers_test'] = 1
                #data["newfollowers"] = list(newfollowers)
                #data["totalnewfollowers"] = len(list(newfollowers))
                
            #return data
            return test_flags
        else:
            save_data_for_first_time(username)
            test_flags['username_test'] = 1
            print("else called")
            return test_flags
            #return {"message": "Your username & Followers have been added for later use!"}


    except Exception as e:
        save_data_for_first_time(username)
        print(e,"error called")
        return {"message": "Your username & Followers have been added for later use!"}