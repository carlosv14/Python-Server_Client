import socket
import Validation
import User
import Json_Manager
import sys
import os.path
import requests

def send_simple_message(to,text,url):

    return requests.post(
        "https://api.mailgun.net/v3/sandboxc53a54ee60d74130ad038e8fb6c64c34.mailgun.org/messages",
        auth=("api", "key-9b2be08330ce6fe41a9a15a950f624c0"),
        files=[("inline", open(url,"rb"))],
        data={"from": "Excited User <mailgun@sandboxc53a54ee60d74130ad038e8fb6c64c34.mailgun.org>",
              "to": "cvarela1496@gmail.com",
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!",
              "html": '<html>' + text + 'Inline image here: <img src="cid:file.jpg"></html>'})

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 399))
serversocket.listen(5)
users = []
json_m = Json_Manager.JsonManager('users.txt')
if os.path.isfile(json_m.archivo):
    users=json_m.readFile()
op= 0

def searchUser(users,searchuser):
    for u in users:
        if u.username == searchuser:
            return u
    return None


while op!=5:

    try:
        print('Running server on ' + socket.gethostname())
        connection, client_address = serversocket.accept()
        op = int(str(connection.recv(1024),'utf-8'))
        print(op)
        while op==1:
                user = User.User()

                while True:
                    connection.sendall(b'Enter User Name: ')
                    username = str(connection.recv(1024),'utf-8')
                    if Validation.Validation.Unique(users,username,0) and username !='':
                        user.username = username
                        break
                while True:
                    connection.sendall(b'Enter Name: ')
                    name =  str(connection.recv(1024),'utf-8')
                    if name !='':
                        user.name = name
                        break
                while True:
                    connection.sendall(b'Enter E-mail: ')
                    email =  str(connection.recv(1024),'utf-8')
                    if Validation.Validation.validEmail(email) and email !='' and Validation.Validation.Unique(users,email,1):
                        user.email = email
                        break
                while True:
                    connection.sendall(b'Enter ID: ')
                    ID =  str(connection.recv(1024),'utf-8')
                    if Validation.Validation.validID(ID) and ID !='' and Validation.Validation.Unique(users,ID,2):
                        user.id = ID
                        break
                while True:
                    connection.sendall(b'Enter Birth Date: ')
                    fecha_nac =  str(connection.recv(1024),'utf-8')
                    if Validation.Validation.validDate(fecha_nac) and fecha_nac !='':
                        user.f_nac = fecha_nac
                        break
                while True:
                    connection.sendall(b'Enter Profile Image: ')
                    pf =  str(connection.recv(1024),'utf-8')
                    user.foto = pf
                    if user.foto!="":
                        break

                users.append(user)
                print("No more info")
                connection.sendall(b'Success')
                op = -1
        if op == 2 :
            connection.sendall(b'Enter User Name: ')
            searchuser = str(connection.recv(1024),'utf-8')
            u = searchUser(users,searchuser)
            if u != None:
                connection.sendall(User.User.show(u))
                op = -1
            else:
                connection.sendall(b'Not Found ')
                op=-1
        if op==3:
            connection.sendall(b'Enter User Name: ')
            searchuser = str(connection.recv(1024),'utf-8')
            u = searchUser(users,searchuser)
            if u!= None:
                users.remove(u)
                connection.sendall(b'Success ')
                op=-1
            else:
                connection.sendall(b'Not Found ')
                op=-1
        if op==4:
            connection.sendall(b'Enter User Name: ')
            searchuser = str(connection.recv(1024),'utf-8')
            u = searchUser(users,searchuser)
            if u!= None:
                send_simple_message('cvarela1496@gmail.com',str(User.User.emailParse(u),'utf-8'))
                op =-1
            else:
                connection.sendall(b'Not Found ')
                op=-1
    except:
        print(sys.exc_info()[0])
    finally:
        json_m.writeFile(users)
        connection.close()
