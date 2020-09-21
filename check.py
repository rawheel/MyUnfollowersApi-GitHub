import requests
from pprint import pprint
import threading
import math
import emoji
import json
class Load_followers:
    def __init__(self,username):
        self.username = username

        info=f"https://api.github.com/users/{self.username}"
        self.total_followers = requests.get(info).json()
        self.total = int(self.total_followers["followers"])
        self.length = math.ceil((int(self.total_followers["followers"]))/100)
        self.followers=[]
    def call_api(self,page):
        per_page = 100 
        url = f"https://api.github.com/users/{self.username}/followers?page={page}&per_page={str(per_page)}"
        user_data = requests.get(url).json()
        [self.followers.append(user_data[i]["login"]) for i in range(len(user_data))]
        
    def get_followers(self):
        threads=[]
        for page in range(1,self.length+1):
            #get_followers(page)
            t = threading.Thread(target=self.call_api,args=[page])
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
        info_dict={self.username:self.followers}
        '''with open('data.txt', 'w') as outfile:
            json.dump(info_dict, outfile)'''
        return info_dict

#object_1 = save_followers("wajahatkarim3")

#saved_followers = object_1.save_followers()

#pprint(json.load(read))
#print(saved_followers)
#print(len(saved_followers))

class GithubFollowers:
    def __init__(self,username):
        self.username = username

    def load_prev_followers(self):
        read = open("data.txt","r")
        self.prev_data = json.load(read)
        return self.prev_data
        #print(self.data)
    def load_recent_followers(self):
        load_followers = Load_followers(self.username)
        self.recent_data = load_followers.get_followers()
        with open('data.txt', 'w') as outfile:
            json.dump(self.recent_data, outfile)
        return self.recent_data
        '''read = open("recent.txt","r")
        self.recent_data = json.load(read)
        return self.recent_data'''


    def save_data_for_first_time(self):
        print("loading followers...")
        
        load_followers = Load_followers(self.username)
        self.data = load_followers.get_followers()
        #print("Loading Done")
        with open('data.txt', 'w') as outfile:
            json.dump(self.data, outfile)
        

    def compare_followers(self):
        try:
            read = open("data.txt","r")
            prev_data = json.load(read)
            prev_username = [i for i in prev_data]

            if prev_username[0]==self.username:
                #print("hello")
                #print(prev_username[0],self.username)
                prev_followers = self.load_prev_followers()
                recent_followers = self.load_recent_followers()
                

                prev_set = set(prev_followers[self.username])
                recent_set = set(recent_followers[self.username])

                unfollowers = prev_set-recent_set
                newfollowers = recent_set - prev_set


                if unfollowers:
                    print(emoji.emojize('Following Folk/s unfollowed you :pensive_face:'))
                    no=0
                    [print(f'{no+1}) {u}') for no,u in enumerate(unfollowers)]
                    print()
                else:
                    print(emoji.emojize("Congrats,No one unfollowed you :grinning_face_with_big_eyes:"))
                if newfollowers:
                    print(emoji.emojize("Following Folk/s recently started following you :smiling_face_with_heart-eyes:"))
                    no=0
                    [print(f'{no+1}) {n}') for no,n in enumerate(newfollowers)]
                else:
                    print(emoji.emojize("Help a person,Get a new Followers :smiling_face_with_halo"))
            else:
                self.save_data_for_first_time()
                #print(e)
                print(emoji.emojize(":check_mark: Your username & Followers have been added for later use!"))                
       
            
        except Exception as e:
            self.save_data_for_first_time()
            #print(e)
            print(emoji.emojize(":check_mark: Your username & Followers have been added for later use!"))



main_object = GithubFollowers("rawheel")
main_object.compare_followers()
