# █▀▀ ▄▀█ █▀▄▀█ █▀▀ █▀█ █░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀ #
# █▄▄ █▀█ █░▀░█ ██▄ █▀▄ █▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█ #
import os
import webbrowser
import requests
import re
import random
import time
from requests.structures import CaseInsensitiveDict
from colorama import Fore, init
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
os.system('pip install -r requirements.txt')
try:
    os.system('cls')
except:
    os.system('clear')
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
color_3 = Fore.RED
print(color_3+r'''
       _________
      / ======= \
     / __________\
    |  _________  |
    | | >_      | |
    | |         | |
    | |_________| |
    \=____________/   
    / """"""""""" \                       
   / ::::::::::::: \                  
  (_________________) 
  ''')
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
color_1 = Fore.YELLOW
print(color_1+'[1]Newest Cameras Hacking ')
print(color_1+'[2]Camera Hacking Dorks Seshat')
print(color_1+'[3]Camera Finder')
print(color_1+'[4]routersploit')
print(color_1+'[5]Resource')
print(color_1+'[6]Search engine')
print          ('|')
num = int(input('└──╼ ✞ Enter Your Number ✞ : '))
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
if num == 1:

    URL = "http://www.insecam.org/en/jsoncountries/"

    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
    ]

    headers = CaseInsensitiveDict({
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "www.insecam.org",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": random.choice(USER_AGENTS)
    })

    try:
        response = requests.get(URL, headers=headers)
        data = response.json()
        countries = data['countries']
    except:
        red = Fore.RED
        print(red + "Please check your internet connection.")

    for key, value in countries.items():
        print(f'Code : ({key}) - {value["country"]} / ({value["count"]})')

    try:
        country = input("Code(##) : ")
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}", headers=headers
        )
        last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

        with open(f'{country}.txt', 'w') as f:
            for page in range(int(last_page)):
                res = requests.get(
                    f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
                    headers=headers
                )
                find_ip = re.findall(r"http://\d+\.\d+\.\d+\.\d+:\d+", res.text)

                for ip in find_ip:
                    print("")
                    print("\033[1;31m", ip)
                    f.write(f'{ip}\n')
                time.sleep(3)
    except:
        pass
    finally:
        print("\033[1;37m")
        print('\033[37mSave File :' + country + '.txt')
        exit()
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
elif num == 2:
    with open('dorks.txt', 'r', encoding='utf-8')as file:
        dork = file.read()
        color_4 = Fore.BLUE
        print(color_4+dork)
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
elif num == 3:
    import socket
    from concurrent.futures import ThreadPoolExecutor

    def is_port_open(ip, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            return result == 0

    def scan_for_cameras(ip_range, target_ports):
        results = []
        with ThreadPoolExecutor(max_workers=20) as executor:
            for ip in ip_range:
                futures = [executor.submit(is_port_open, ip, port) for port in target_ports]
                open_ports = [port for port, status in zip(target_ports, futures) if status.result()]
                if open_ports:
                    results.append(f"Found camera at {ip} on ports: {', '.join(map(str, open_ports))}")
        return results

    if __name__ == "__main__":
        start_ip = input("Enter start IP address: ")
        end_ip = input("Enter end IP address: ")
        target_ports = [80, 554, 8080, 443, 9100, 9000, 3389, 8000, 37777, 34567, 5554, 65535, 6200, 8888, 8585, 9080]
        ip_range = [f"{start_ip.rsplit('.', 1)[0]}.{ip}" for ip in range(int(start_ip.split('.')[-1]), int(end_ip.split('.')[-1]) + 1)]
        results = scan_for_cameras(ip_range, target_ports)
    
        if results:
            with open("camera_results.txt", "w") as file:
                for result in results:
                    file.write(result + "\n")        
            print("Scan results saved to 'camera_results.txt'")
        else:
            print("No cameras found.")      
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
elif num == 4:
    url = "https://github.com/threat9/routersploit"
    webbrowser.open(url)
 # 卐 卐 卐 卐 卐 卐 卐 卐 卐  
elif num == 5:
    color_5 = Fore.LIGHTCYAN_EX
    print(color_5+'''
    Site🖥️  http://www.insecam.org/
    Site🖥️  http://www.opentopia.com/
    Site🖥️  https://www.earthcam.com/
    Site🖥️  https://hackeracademy.org/10-ways-to-hack-cctv-cameras-and-how-to-prevent-it/
    Tool🗡️  https://angryip.org/
    Tool🗡️  https://subscription.packtpub.com/book/security/9781782168492/6/ch06lvl1sec45/xhydra
    Site🖥️  http://routerpwn.com/
    Site🖥️  https://learncctv.com/hikvision-backdoor-exploit-tool-download
    ''')
elif num == 6:
    color_6 = Fore.CYAN
    url = "https://www.shodan.io/explore/search?query=tags%3Acamera&page=1"
    url_2 = "https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=webcamxp" 
    url_3 = "https://www.zoomeye.org/searchResult?q=cctv"
    webbrowser.open(url)
    webbrowser.open_new_tab(url_2)
    webbrowser.open_new_tab(url_3)