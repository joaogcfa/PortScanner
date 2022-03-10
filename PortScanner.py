import pyfiglet
import socket

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner, "\n")

ip = input("Target IP \n")

start = int(input('Starting Port\n'))
end = int(input('Ending Portl\n'))


print("-" * 50)
print("Scanning Target: " + ip)
print("-" * 50, "\n")


for port in range(start, end+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    # returns an error indicator
    result = s.connect_ex((ip, port))
    if result == 0:
        service = socket.getservbyport(port)
        print("Port {} is open and runs {} \n".format(port, service))
    s.close()
