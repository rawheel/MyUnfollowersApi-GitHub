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
        self.length = math.ceil(self.total/100)
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

