import re
import os

file1 = open('deletable.txt', 'x')

def start():
	
	print('Thanks for using NMAP Pro!' + '\n')
	print('Would you like to manually give me IP Addresses or would you like to give me a file?' + '\n')
	print('M for manual | F for file (For file: please do one IP per line)')
	
	while(1 == 1):
		x = str(input())
	
		if (x == 'M' or x == 'm'):
			print('\n' + 'Manual: please give me each IP(v4) address (pressing enter after each one). Once completed, please input "done")')
			while (2 == 2):
				ip = str(input('IP: '))
				if(ip == 'done'):
					file1.close()
					nmap_filter()
					break;
				else:
					result = validIP(ip)
					if(result == "Valid"):
						file1.write(ip + ' ')
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
							file1.write(ip + ' ')
						else:
							print('Invalid IPv4: ' + line)
					file1.close()
					nmap_filter()
					break;
					
				except IOError:
					print('Cannot find File' + '\n')
			break;
			
		else:
			print('Please enter M or F' + '\n')
			
def validIP(y):        		
	valid = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
	
	if '/' in y:
		pos = y.find('/')
		newy = ''
		for i in range(pos):
			newy = newy + y[i]
		
	if(re.search(valid, y) or re.search(valid, newy)):
		return("Valid")
	else:
		return("")

def nmap_filter():
	print('Data Retrieved. What flags do you want to use (do not use file output flag)? Make sure there is no whitespace before or after your flag inputs. Input "done" when completed.')
	print('Input nmap -h or nmap -help to view flags. Make sure to add context to your flags. ex. -p 80')
	
	flags = []
	while(4 == 4):
		f = input("Flag: ")
		
		if(f == "nmap -h" or f == "nmap --help"):
			os.system("nmap -h")
		
		else:
			if(f == 'done'):
				break;
			else:
				print('Flag added: ' + f)
				ye = input("Is that correct? (y/n) ")
				
				if(ye == 'y' or ye == 'Y'):
					flags.append(f)
				elif(ye == 'n' or ye == 'N'):
					print("Flag removed.")
		
	name = input('What would you like your output file to be named?' + '\n')
	
	flag = ''
	for b in range(len(flags)):
		flag = flag + ' ' + flags[b]
	
	os.system("nmap " + "-iL deletable.txt -oX " + name + ".xml " + flag)

	#comment this out if you are using the second print statement below
	print('\n' + "Completed! Please check " + name + ".xml for your results!")
  
  	#To use this you will need to have xml2csv.py in the same directory. https://github.com/NetsecExplained/Nmap-XML-to-CSV 
	#os.system('python xml2csv.py -f ' + name + '.xml -csv ' + name + '.csv')
	#print('\n' + "Completed! Please check " + name + ".csv for your results! P.S. If there is no csv file then there were no valid results.")
	

#Starting the code
start()
