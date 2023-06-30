import re
import os

ip_list = []

def start():
	
	print('Thanks for using NMAP Filter Pro!' + '\n')
	print('Would you like to manually give me IP Addresses or would you like to give me a file?' + '\n')
	print('M for manual | F for file (For file: please do one IP per line)')
	
	while(1 == 1):
		x = str(input())
	
		if (x == 'M' or x == 'm'):
			print('\n' + 'Manual: please give me each IP(v4) address (pressing enter after each one). Once completed, please say "done")')
			while (2 == 2):
				ip = str(input('IP: '))
				if(ip == 'done'):
					nmap_filter()
					break;
				else:
					result = validIP(ip)
					if(result == "Valid"):
						ip_list.append(ip)
					else:
						print('Invalid IPv4')
			break;
			
		if (x == 'F' or x == 'f'):
			print('\n' + 'File: please give me the location of the file you want to use. ex: D:\Downloads\MyFile.txt | /home/kali/Desktop/MyFile.txt')
			while (3 == 3):
				try:
					myfile = open(str(input('File: ')), 'r')
					lines = myfile.readlines()
					for line in lines:
						line = line.strip()
						result = validIP(line)
						if(result == "Valid"):
							ip_list.append(line)
						else:
							print('Invalid IPv4: ' + line)
					nmap_filter()
					break;
					
				except IOError:
					print('Cannot find File' + '\n')
			break;
			
		else:
			print('Please enter M or F' + '\n')
			
def validIP(y):
	valid = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
	
	if(re.search(valid, y)):
		return("Valid")
	else:
		return("")

def nmap_filter():
	print('Data Retrieved. What would you like the results to return?')
	while(4 == 4):
		cmd = input()
		try:
			process = os.popen(cmd)
		except:
			print("Invalid Command")
	results = str(process.read())
	print(results)
	exit()

#Starting the code
start()
