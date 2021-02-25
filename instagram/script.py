
import threading
import instaloader

class InstaFollowers:
	def __init__(self,username,password):

		self.username = username
		self.password = password

	def get_follower(self):
		try:
			L = instaloader.Instaloader()
			L.login(self.username,self.password)
			try:
				print('\n\nGetting followers from',self.username)
				profile = instaloader.Profile.from_username(L.context,self.username)	
				
				followers= {'username':self.username,'followers':[f.username for f in profile.get_followers()],'totalfollowers':profile.followers}
				return followers

			except Exception as e:
				return 2
		except Exception as e:
			return 0
			
			

ob1 = InstaFollowers("username","pass")
print(ob1.get_follower())
