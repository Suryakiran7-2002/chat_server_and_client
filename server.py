import socket
import threading

c = []
a = []
def handle_client(conn,addr):
    while True:
        msg = conn.recv(1024).decode()
        if msg == '!bye':
            conn.close()
            c.remove(conn)
            print("disconnected from ",addr)
            break
        #print(addr,msg)

        '''
        if conn == c[0]:
            
            c[1].send(bytes(msg,"utf-8"))
        elif conn == c[1]:
            c[0].send(bytes(msg,"utf-8"))
        '''

        #multi part

        for i in range(len(c)):
            if conn == c[i]:
                continue
            else:
                c[i].send(bytes(msg, "utf-8"))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostname()
port = 4444

s.bind(('',port))

s.listen(4)

while True:
    conn,addr = s.accept()
    c.append(conn)
    a.append(addr)
    thread = threading.Thread(target=handle_client,args=(conn,addr))
    thread.start()
    print(threading.activeCount()-1)