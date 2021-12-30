import requests
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor

lst = [
    'mail',
    'mail2',
    'www',
    'tv',
    'photos',
    'hack',
    'accounts',
    'users',
]

domain = 'google.com'

def scanner(subdomain):
    build_url = (f'http://{subdomain}.{domain}')
    send_rq = requests.get(build_url)
    resp = send_rq.status_code

    if resp == 200:
        print(Fore.GREEN + Style.BRIGHT + '[+] Valid subdomain found:' + Style.RESET_ALL,build_url)
    else:
        pass

with ThreadPoolExecutor(max_workers=20) as executor:
    for subdomain in lst:
        executor.submit(scanner, subdomain)

