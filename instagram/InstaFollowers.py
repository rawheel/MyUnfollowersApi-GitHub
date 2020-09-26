from flask import Flask
from flask_restful import Api, Resource,reqparse,abort
from flask import jsonify
import threading
import instaloader
app = Flask(__name__)
api = Api(app)
class InstaFollowers(Resource):
	def get(self,username,password):
		self.username = username
		self.password = password
		self.names = []
		self.followers_data={}
		ret = self.initiate()
		return jsonify(ret)


	def initiate(self):
		self.L = instaloader.Instaloader()
		self.L.login(self.username,self.password)
		check = self.get_follower()
		return check


	def add_to_list(self, i):
		j = str(i).split(" ")
		self.names.append(j[1])

	def get_follower(self):
		account_name = "pytroops"
		try:
			print('\n\nGetting followers from',account_name)
			#filename = 'downloads/'+pro+'.csv'
			profile = instaloader.Profile.from_username(self.L.context, account_name)
			main_followers = profile.followers
			lust = []
			for count,i in enumerate(profile.get_followers()):
				t2 = threading.Thread(target=self.add_to_list, args=[i])
				t2.start()
				lust.append(t2)
			for thread in lust:
				thread.join()
			#print(f'account name: {pro}, total followers: {count}')

		except Exception as e:
			self.followers_data = {account_name:self.names}
			#print(self.followers_data)
			#print('Skipping',account_name,e)
			return self.followers_data
		self.followers_data = {account_name:self.names}
		#print(self.dict_fol)

		return self.followers_data

#ob1 = InstaFollowers("test.accw2","testacc1")
#ob1.start()
api.add_resource(InstaFollowers,"/<string:username>/<string:password>")

if __name__ == "__main__":
	app.run(debug=True)