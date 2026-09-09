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