import sys
import requests 
import colorama
import os
import asyncio
import time
from urllib.parse import urlparse 
from colorama import Fore, Back, Style

clear = lambda : os.system('cls')

def progressbar(it, prefix="", size=60, file=sys.stdout):
    
    clear()
    count = len(it)

    def show(j):
        x = int(size * j / count)
        file.write(
            "%s[%s%s] %i/%i\r" % (prefix, f"{Fore.YELLOW}#{Fore.WHITE}" * x, "." * (size - x), j, count))
        file.flush()

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    file.write("\n")
    file.flush()

for i in progressbar(range(100), "Loading, Please Wait ", 10):
        time.sleep(0.02)

clear()

home = f"{Fore.YELLOW}[cloudssp]{Fore.WHITE} Enter Target (e.g - https://retards.lol)"


def Menu(home):
    print(home)
    cfcheck()

def cfcheck():
    url = inputs = input(f">{Fore.YELLOW} ")
    x = requests.get(url+'/mailman/listinfo/mailman')

    if x.status_code == 404:
              print(f'{Fore.RED}Seems like this site is not vulnerable.')
    else:
          print(f"{Fore.CYAN}Looks like we found something!")
          print("")
          print(f"{Fore.WHITE}IP/Domain links found:")
          print("")

          os.system("curl "+inputs+"/mailman/listinfo/mailman -s | findstr POST")
          time.sleep(0.5)


Menu(home)