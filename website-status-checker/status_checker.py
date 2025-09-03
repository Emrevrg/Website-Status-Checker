import requests
import sys

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[+] {url} --> Çalışıyor (200)")
        else:
            print(f"[-] {url} --> Hata ({response.status_code})")
    except requests.exceptions.RequestException:
        print(f"[!] {url} --> Ulaşılamıyor")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python status_checker.py <url1> <url2> ...")
        sys.exit(1)

    for site in sys.argv[1:]:
        check_website(site)
