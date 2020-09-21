import requests
from pprint import pprint
import threading
import math
import json
class save_followers:
    def __init__(self,username):
        self.username = username

        info=f"https://api.github.com/users/{self.username}"
        total_followers = requests.get(info).json()
        self.length = math.ceil((int(total_followers["followers"]))/100)
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

class comp:
    def __init__(self,username):
        self.username = username


    def save_my_followers(self):
        read = open("blank.txt","r")
        try:
            data = json.load(read)
            print(data)
        except:
            save_followers_object = save_followers(self.username)
            all_followers = save_followers.get_followers()
            with open('data.txt', 'w') as outfile:
                json.dump(info_dict, outfile)
            print("your followers all loaded")

ob  = comp("wajahatkarim3")
ob.save_my_followers()

