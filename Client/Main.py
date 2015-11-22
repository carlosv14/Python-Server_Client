import socket

def main():
    op = 0
    while op != 5:
        print('1. Add User')
        print('2. Search User')
        print('3. Delete User')
        print('4. Send User Info')
        print('5. Exit')
        op = int(input('Option: '))
        if op == 1:
            try:
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                server_address = (socket.gethostname(),399)
                sock.connect(server_address)
                sock.sendall(str.encode(str(op)))

                data = ''
                while data != 'Success':
                    data = str(sock.recv(1024),'utf-8')
                    if data!='Success':
                        info = input(data)
                        sock.sendall(str.encode(info))
                    elif data == 'Success':
                        op=-1

            finally:
                print('closing')
                sock.close()
        if op == 2:
            try:
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                server_address = ('CarlosV',399)
                sock.connect(server_address)
                print(str(op))
                sock.sendall(str.encode(str(op)))

                while True:
                    data = str(sock.recv(1024),'utf-8')
                    if data =='Enter User Name: ':
                        info = input(data)
                        sock.sendall(str.encode(info))
                    else:
                        print(data)
                        op = -1
                        break

            finally:
                print('closing')
                sock.close()

        if op == 3:
            try:
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                server_address = ('CarlosV',399)
                sock.connect(server_address)
                print(str(op))
                sock.sendall(str.encode(str(op)))

                while True:
                    data = str(sock.recv(1024),'utf-8')
                    if data =='Enter User Name: ':
                        info = input(data)
                        sock.sendall(str.encode(info))
                    else:
                        print(data)
                        op = -1
                        break

            finally:
                print('closing')
                sock.close()
        if op == 4:
            try:
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                server_address = ('CarlosV',399)
                sock.connect(server_address)
                print(str(op))
                sock.sendall(str.encode(str(op)))

                while True:
                    data = str(sock.recv(1024),'utf-8')
                    if data =='Enter User Name: ':
                        info = input(data)
                        sock.sendall(str.encode(info))
                    elif data == 'Enter Email Recipient: ':
                        info = input(data)
                        sock.sendall(str.encode(info))
                    else:
                        print(data)
                        op = -1
                        break

            finally:
                print('closing')
                sock.close()

if __name__ == "__main__":
    main()