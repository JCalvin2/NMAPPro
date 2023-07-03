# NMAPPro
This code will ask the user for IPs/Subnets (manually inputted) or a file with a list of IPs for nmap input. 
It will then validate the given IPs/Subnets.
Afterwards the user will give what flags they wish to use. 
The code executes the nmap command for the user & outputs an xml file. 
To use the script to its full potential you will need to download xml2csv & uncomment the code that uses this. 
https://github.com/NetsecExplained/Nmap-XML-to-CSV
The code will automatically run your nmap command & convert the output to a user friendly csv file. 
