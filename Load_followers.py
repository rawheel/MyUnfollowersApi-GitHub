import requests
import threading
import math
import json
import instaloader

class Api_services:
    
    def githubApi(self,username):
        info=f"https://api.github.com/users/{username}"
        return info
    def githuburlApi(self,username,page,per_page):
        url = f"https://api.github.com/users/{username}/followers?page={page}&per_page={per_page}"
        return url

class Load_followers:
    def __init__(self,username):
        self.username = username
        self.apis = Api_services()

        self.info = self.apis.githubApi(username) 
        self.response = requests.get(self.info).json()
        self.total = int(self.response["followers"])
        self.length = math.ceil(self.total/100)
        self.followers=[]

    def call_api(self,page):
        per_page = 100
        url = self.apis.githuburlApi(self.username,page,str(per_page))
        user_data = requests.get(url).json()
        [self.followers.append(user_data[i]["login"]) for i in range(len(user_data))]
        
    def get_followers(self):
        threads=[]
        for page in range(1,self.length+1):
            t = threading.Thread(target=self.call_api,args=[page])
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
        
        info_dict={self.username:self.followers,"totalfollowers":self.total,"avatar_url":self.response['avatar_url']}
        return info_dict

class InstaFollowers:
	def __init__(self,username,password):

		self.username = username
		self.password = password

	def get_follower(self):
		try:
			L = instaloader.Instaloader()
			L.login(self.username,self.password)
			try:
				profile = instaloader.Profile.from_username(L.context,self.username)	
				
				followers= {'username':self.username,'followers':[f.username for f in profile.get_followers()],'totalfollowers':profile.followers}
				return followers

			except Exception as e:
				return 2
		except Exception as e:
			return 0
			
			

#ob1 = InstaFollowers("username","pass")
#print(ob1.get_follower())
