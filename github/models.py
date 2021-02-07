import sqlite3

class myunfollowersdb:
    def __init__(self):
        self.connection = sqlite3.connect('database/myunfollowers.db')
        self.cursor = self.connection.cursor()

    def createTables(self):
        self.cursor.execute("""CREATE TABLE "users" (
                "userId"	INTEGER NOT NULL,
                "username"	TEXT NOT NULL,
                PRIMARY KEY("userId" AUTOINCREMENT)
                            );""")
        self.cursor.execute("""CREATE TABLE userdata (
            dataId INTEGER,
            followers INTEGER,
            FOREIGN KEY(dataId) REFERENCES users(userId) ON DELETE CASCADE);""")
        self.connection.commit()
   
    def insertUser(self,username):
        self.cursor.execute("INSERT or REPLACE INTO users VALUES(NULL,?)",(username,))
        self.connection.commit()

    def insertData(self,id,data):
        self.cursor.execute("INSERT or REPLACE INTO userdata VALUES(?,?)",(id,data))
        self.connection.commit()
        #self.connection.close()

    def fetchallUsernames(self):
        self.cursor.execute("select username from users")
        return self.cursor

    def checkUsername(self,username):
        flag = False
        if len([user for user in self.fetchallUsernames() if username in user]):
            flag = True
        return flag

    def fetchUserData(self,username):
        self.cursor.execute("""SELECT userdata.followers FROM userdata,users WHERE users.username = (?) AND users.userId = userdata.dataId""",(username,))
        for i in self.cursor:
            followers =[i[0].strip('][')][0].replace(',', '').replace("'", '').split(' ')
        return followers
    
    def updateData(self,username,data):
        self.cursor.execute("""SELECT userId from users where username = (?)""",(username,))
        id = [i[0] for i in self.cursor][0]
       
        self.cursor.execute("""UPDATE userdata SET followers = (?) WHERE dataId= (?)""",(data,id))
        self.connection.commit()
        