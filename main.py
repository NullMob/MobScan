import socket

# Input domain from the user
host = input("Type a host: ")

# List of Ports to test
portslist = "PortList.txt"
listport = []

#Final Statistics
time = 0
opensp = 0

# Read the wordlist file
with open(portslist, "r") as archive:
    for line in archive:
        line = line.strip()
        value = int(line)
        listport.append(value)


for port in listport:
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.3)
    time += 0.3
    code = client.connect_ex((host, port))

    if code == 0:
        print("Port Open:", port)
        opensp += 1

print ("Done!", opensp,"ports found in", time,"seconds.")
