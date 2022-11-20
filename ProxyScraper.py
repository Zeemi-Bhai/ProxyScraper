from bs4 import BeautifulSoup
import requests
from slowprint.slowprint import *

logo ="""  
 ______                    _                   _
 |___  /                  (_)  _ \| |         (_)
    / / ___  ___ _ __ ___  _| |_) | |__   __ _ _ 
   / / / _ \/ _ \ '_ ` _ \| |  _ <| '_ \ / _` | |
  / /_|  __/  __/ | | | | | | |_) | | | | (_| | |
 /_____\___|\___|_| |_| |_|_|____/|_| |_|\__,_|_|   
 """
slowprint("Lisenced to @ZeemiBhai | github.com/Zeemi-Bhai",0.5)
slowprint(logo,0.05)
slowprint("\t\t\t\t\tt.me/AnonCyberWarrior",0.5)


filename = input("Enter the output filename : ")

url = 'https://free-proxy-list.net/'
r = requests.get(url)
content = r.content
soup = BeautifulSoup(content,'html.parser')

proxies = set()
table = soup.find('div',class_='table-responsive fpl-list')
body = table.find('tbody')
rows = body.find_all('tr')
for row in rows :
    ip = row.find('td')
    port = ip.findNext().text
    ip = ip.text
    print(f"{ip}:{port}")
    proxy = f"{ip}:{port}" 
    proxies.add(str(proxy+'\n'))
# for proxy in proxies:
with open(filename,'w')as f:
    f.writelines(proxies)
    # for proxy in proxies:
