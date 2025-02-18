import socket 
import termcolor


def scan(targets, ports):
	for ports in range(1,ports):
		scan_port(targets,ports)



def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] - port opened" + str(port))
	except:
		pass
targets = input("[*] Enter Target To Scan: ")
ports = int(input("[*] Enter how many Ports You Want To Scan: "))
if ',' in targets:
	print("[*] Scanning Multiply Targets")
	for ip_addr in targets.split(","):
		scan(ip_addr.strip(" "), ports)
else:
	scan(targets, ports)		
