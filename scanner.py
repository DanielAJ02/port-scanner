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

start_port = 1    #scanning from port one to 100
end_port = 100

for port in range(start_port, end_port + 1): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a sockrt for IPV4 using TCP
    sock.settimeout(0.5) #sets timeout for checking if port is open to o.5 secs
    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    sock.close()