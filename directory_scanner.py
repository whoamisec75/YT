import requests
from concurrent.futures import ThreadPoolExecutor

with open('wordlist.txt') as wordlist: #replace the "wordlist.txt" with your wordlist name :)
    read = wordlist.read().splitlines()

exts = [
    'php',
    'html' #you can add more...
]

target = 'http://testphp.vulnweb.com' #change the target if you want

def scanner(target, dir, ext):
    build_url = (f'{target}/{dir}.{ext}')
    req = requests.get(build_url)
    resp = req.status_code

    if resp == 200:
        print('[+] Valid path found:', build_url)
    elif resp == 403:
        print('[!] Access denied:',build_url) 

with ThreadPoolExecutor(max_workers=100) as executor: #you can change "max_workers" according to you 
    for dir in read:
        for ext in exts:
            executor.submit(scanner, target, dir, ext)
