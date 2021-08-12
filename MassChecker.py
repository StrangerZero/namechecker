import requests
import threading
import colorama
import webbrowser
from colorama import Fore, Style, init
init()

webbrowser.open('https://github.com/wsex')

names = open('names.txt', 'r').read().split('\n')
valid = open('valid.txt', 'a')

print(Fore.GREEN + '''

 ███▄    █  ▄▄▄       ███▄ ▄███▓▓█████     ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
 ██ ▀█   █ ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒███      ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░░   ░ ▒░  ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
   ░   ░ ░   ░   ▒   ░      ░      ░      ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
         ░       ░  ░       ░      ░  ░   ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░

         ''')

def menu():
    
    print()
    print(Fore.GREEN + '''

<======>

[ 1 ] - GitHub Name Checker

[ 2 ] - Osu! Name Checker

[ 3 ] - Steam Name Checker

[ 4 ] - TikTok Name Checker

[ 5 ] - Xbox Gamertag Checker

<======>
''')

menu()
option = int(input())

def req(name):
    r = requests.get('https://github.com/' + name) 
    if r.status_code in [200, 201, 204]:
        print('Bad: ' + name)
    if r.status_code in [400, 401, 404]:
        print('Hit: ' + name)
        valid.write(f'{name}\n')
    if r.status_code == 429:
        print('ERROR: Rate Limited')


def req2(name):
    r = requests.get('https://osu.ppy.sh/users/' + name) 
    if r.status_code in [200, 201, 204]:
        print('Bad: ' + name)
    if r.status_code in [400, 401, 404]:
        print('Hit: ' + name)
        valid.write(f'{name}\n')
    if r.status_code == 429:
        print('ERROR: Rate Limited')

def req3(name):
    r = requests.get('https://steamcommunity.com/id/' + name) 
    if r.status_code in [200, 201, 204]:
        print('Bad: ' + name)
    if r.status_code in [400, 401, 404]:
        print('Hit: ' + name)
        valid.write(f'{name}\n')
    if r.status_code == 429:
        print('ERROR: Rate Limited')

def req4(name):
    r = requests.get('https://tiktok.com/@' + name) 
    if r.status_code in [200, 201, 204]:
        print('Bad: ' + name)
    if r.status_code in [400, 401, 404]:
        print('Hit: ' + name)
        valid.write(f'{name}\n')
    if r.status_code == 429:
        print('ERROR: Rate Limited')

def req5(name):
    r = requests.get('https://xboxgamertag.com/search/' + name) 
    if r.status_code in [200, 201, 204]:
        print('Bad: ' + name)
    if r.status_code in [400, 401, 404]:
        print('Hit: ' + name)
        valid.write(f'{name}\n')
    if r.status_code == 429:
        print('ERROR: Rate Limited')
        
if option == 1:
    for name in names:
        thread = threading.Thread(target=req, args=(name,))
        thread.start()


if option == 2:
    for name in names:
        thread = threading.Thread(target=req2, args=(name,))
        thread.start()

if option == 3:
    for name in names:
        thread = threading.Thread(target=req3, args=(name,))
        thread.start()

if option == 4:
    for name in names:
        thread = threading.Thread(target=req4, args=(name,))
        thread.start()

if option == 5:
    for name in names:
        thread = threading.Thread(target=req5, args=(name,))
        thread.start()

