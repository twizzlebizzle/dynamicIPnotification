import urllib.request

#Below code is used to get the previous IP from a text file and the new IP address
#It then stores them as variables

path = "/home/pi/programs/testprogs/ipaddress.txt"
openfile = open(path,"r")
read_ip = openfile.readline()
openfile.close()

try:
 external_ip = urllib.request.urlopen("https://ident.me").read().decode("utf8")
except:
 external_ip = read_ip

if external_ip == read_ip:
 exit()
else:
 openfile = open(path,"w")
 openfile.write(external_ip)
 openfile.close()
 import http.client, urllib
 conn = http.client.HTTPSConnection("api.pushover.net:443")
 conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
   "token":[TOKEN HERE],
   "user":[TOKEN HERE],
   "message":"IP Address has updated to: "+external_ip,
  }), {"Content-type": "application/x-www-form-urlencoded" })
 conn.getresponse()
