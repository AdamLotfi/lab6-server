import math
import socket
import sys
import time
import errno
from multiprocessing import Process

def process_start(s_sock):
    s_sock.send(str.encode('\n--------Simple Calculator------\n'))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        try:
            operation, val = data.split(":")
            opt = str(operation)
            n = float(val)

            if opt[0] == '1':
                opt = 'Logarithmic function'
                ans = math.log10(n)
            elif opt[0] == '2':
                opt = 'Square Root'
                ans = math.sqrt(n)
            elif opt[0] == '3':
                opt = 'Exponential Function'
                ans = math.exp(n)
            else:
                answer = ('ERROR!!...Please Input 1, 2 and 3 only')

            sendAns = ('\n'+str(opt)+ '['+ str(n) + ']= ' + str(ans) + ('\n\n'))
            print ('\nDone')
        except:
            print ('Connection Terminated')
            sendAns = ('Connection Terminated')

        if not data:
            break

        s_sock.send(str.encode(str(sendAns)))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8080))
    print("Listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                print("Connected to client...")
                p.start()

            except socket.error:
                print('There is error in your socket connection')

    except Exception as e:
                print("An exception occurred!")
                print(e)
                sys.exit(1)
    finally:
     	   s.close()
