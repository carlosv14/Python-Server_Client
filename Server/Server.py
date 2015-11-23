import socket
import Validation
import User
import Json_Manager
import sys
import os.path
import requests
import re
import string

def send_simple_message(to,text,url):
    filename = re.split("\\\\", url)
    filename.reverse()
    return requests.post(
        "https://api.mailgun.net/v3/sandboxc53a54ee60d74130ad038e8fb6c64c34.mailgun.org/messages",
        auth=("api", "key-9b2be08330ce6fe41a9a15a950f624c0"),
        files=[("inline", open(url,"rb"))],
        data={"from": "User Manager <mailgun@sandboxc53a54ee60d74130ad038e8fb6c64c34.mailgun.org>",
              "to": to,
              "subject": "User Information",
              "html": '<html>  <body>' + text + '<img src='"cid:" +filename[0] +' style=width:128px;height:128px;>  </body></html>'})

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 399))
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
                    connection.sendall(b'Enter User Name: \n ')
                    username = str(connection.recv(1024),'utf-8')
                    if "\r\n"  in username:
                        username = re.split("\r\n", username)[0]
                    if Validation.Validation.Unique(users,username,0) and username !='':
                        user.username = username
                        break
                while True:
                    connection.sendall(b'Enter Name: \n')
                    name =  str(connection.recv(1024),'utf-8')
                    if "\r\n"  in name:
                        name = re.split("\r\n", name)[0]

                    if name !='':
                        user.name = name
                        break
                while True:
                    connection.sendall(b'Enter E-mail: \n')
                    email =  str(connection.recv(1024),'utf-8')
                    if "\r\n"  in email:
                        email = re.split("\r\n", email)[0]
                    if Validation.Validation.validEmail(email) and email !='' and Validation.Validation.Unique(users,email,1):
                        user.email = email
                        break
                while True:
                    connection.sendall(b'Enter ID: \n')
                    ID =  str(connection.recv(1024),'utf-8')
                    if "\r\n"  in ID:
                        ID = re.split("\r\n", ID)[0]
                    if Validation.Validation.validID(ID) and ID !='' and Validation.Validation.Unique(users,ID,2):
                        user.id = ID
                        break
                while True:
                    connection.sendall(b'Enter Birth Date: \n')
                    fecha_nac =  str(connection.recv(1024),'utf-8')
                    if "\r\n"  in fecha_nac:
                        fecha_nac = re.split("\r\n", fecha_nac)[0]
                    if Validation.Validation.validDate(fecha_nac) and fecha_nac !='':
                        user.f_nac = fecha_nac
                        break
                while True:
                    connection.sendall(b'Enter Profile Image: \n')
                    pf =  str(connection.recv(1024),'utf-8')
                    user.foto = pf
                    if user.foto!="":
                        break

                users.append(user)
                print("No more info")
                connection.sendall(b'Success\n')
                op = -1
        if op == 2 :
            connection.sendall(b'Enter User Name: \n')
            searchuser = str(connection.recv(1024),'utf-8')
            if "\r\n"  in searchuser:
                searchuser = re.split("\r\n", searchuser)[0]
            u = searchUser(users,searchuser)
            if u != None:
                connection.sendall(User.User.show(u))
                op = -1
            else:
                connection.sendall(b'Not Found \n')
                op=-1
        if op==3:
            connection.sendall(b'Enter User Name: \n')
            searchuser = str(connection.recv(1024),'utf-8')
            if "\r\n"  in searchuser:
                searchuser = re.split("\r\n", searchuser)[0]
            u = searchUser(users,searchuser)
            if u!= None:
                users.remove(u)
                connection.sendall(b'Success \n')
                op=-1
            else:
                connection.sendall(b'Not Found \n')
                op=-1
        if op==4:
            connection.sendall(b'Enter User Name: ')
            searchuser = str(connection.recv(1024),'utf-8')
            connection.sendall(b'Enter Email Recipient: ')
            r = str(connection.recv(1024),'utf-8')
            u = searchUser(users,searchuser)
            if u!= None:
                send_simple_message(r,str(User.User.emailParse(u),'utf-8'),str(User.User.imgSource(u),"utf-8"))
                op =-1
            else:
                connection.sendall(b'Not Found ')
                op=-1
    except:
        print(sys.exc_info()[0])
    finally:
        json_m.writeFile(users)
        connection.close()
