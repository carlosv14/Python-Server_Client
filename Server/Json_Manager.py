import json
import User

class JsonManager:


    def __init__(self,archivo):
        self.archivo = archivo


    def writeFile(self,userlist):
        with open(self.archivo, 'w') as usersFile:
           json.dump(userlist,usersFile,default=lambda o: o.__dict__)


    def asUsers(self,dct):
        users = []
        x=0
        for u in dct[0]:
            users.append(User.User(dct[0][x]['username'],dct[0][x]['name'],dct[0][x]['email'],dct[0][x]['id'],
                                   dct[0][x]['f_nac'],dct[0][x]['foto']))
            x+=1
        return  users

    def readFile(self):
        users=[]
        with open(self.archivo, 'r+') as usersFile:
            users.append(json.load(usersFile))
        return self.asUsers(users)

