'''A lightweight, multithreaded TCP connect() port scanner written in Python, 
built as a hands-on exercise in the reconnaissance/scanning phase of a penetration test
'''
import socket    # pyth's built-in module for network communication
import sys       #let's us read arguments typed in the terminal 

if len (sys.argv) < 2:
    print("Usage: python scanner.py <target>")
    sys.exit(1)
target = sys.argv[1]   #sys.argv allows type what we want to scan after typing the scanner.py 
print (f"Target: {target}")

port = 80 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a socket for IPV4 (AF_INET) using TCP(SOCK_STREAM)
result = sock.connect_ex((target, port)) #tries to connect

if result == 0: #Instead of crashing, it returns 0 for success 
    print(f"port {port} is open")
else:
    print(f"port {port} is closed") #and a non-zero for failure

sock.close() #frees the connection; closes it once were done with it
