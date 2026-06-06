#!/usr/bin/python
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def cek_header(url):
    if not url.startswith("http"):
        url = "https://" + url
    try:
        r = requests.get(url, timeout=10)
        print(f"\n{Fore.CYAN}=== Header {url} ==={Style.RESET_ALL}")

        headers = ["Server", "X-Powered-By", "Content-Type", "CF-Ray", "X-Cache"]
        for h in headers:
            if h in r.headers:
                print(f"{Fore.GREEN}{h}:{Style.RESET_ALL} {r.headers[h]}")

        print(f"\n{Fore.YELLOW}Status Code:{Style.RESET_ALL} {r.status_code}")
        print(f"{Fore.YELLOW}Response Time:{Style.RESET_ALL} {r.elapsed.total_seconds()}s")

    except Exception as e:
        print(f"{Fore.RED}[ERROR] {e}")

if __name__ == "__main__":
    print(f"{Fore.MAGENTA}=== Header Hunter ==={Style.RESET_ALL}")
    url = input("Masukkan domain: ")
    cek_header(url)
