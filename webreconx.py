import requests
from rich import *
import pyfiglet
import argparse
import datetime
import socket

def safe_datetime(ts):
    if ts:
        return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    else:
        return "N/A"
    

parser = argparse.ArgumentParser(description="WebReconX - Website Info Scanner")
parser.add_argument('--url', type=str, required=True, help='URL to scan')
args = parser.parse_args()
print(f"Scanning {args.url}...")

url=args.url
if url.find('s'):
    domain=url[8:]
else:
    domain=url[7:]
print(pyfiglet.figlet_format("WebReconX",justify="center"))

response=requests.get(f'https://api.whois.vu/?q={domain}',timeout=5)
try:
    info=requests.get(url, headers={
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
    })
except:
    print('[-] Connection failed to the requested website.')
    exit(1)

if response.status_code==200:
    data=response.json()
    ip=socket.gethostbyname(domain)
    created_date=safe_datetime(data.get('created'))
    updated_date=safe_datetime(data.get('updated'))
    expires_date=safe_datetime(data.get('expires'))
    save_data=f"""🔎 WHOIS & Domain Info
---------------------
🌐 Domain     : {data.get('domain')}
🛡️ Registrar  : {data.get('registrar')}
🗓️ Created    : {created_date}
🔄 Updated    : {updated_date}
⌛ Expires    : {expires_date}
🏢 Type       : {data.get('type')}
✅ Available  : {data.get('available')}
📍 IP Address : {ip}  

🌐 HTTP Response Headers
-----------------------"""
    print(save_data)
    save_data+="\n"
    for x,y in info.headers.items():
        if x in ["Content-Type","Content-Encoding","Connection","Server","Cache-Control","ETag","Alt-Svc","Connection"]:
            print(f'{x}:{y}')
            save_data+=x+":"+y+"\n"
    

    rep = input("\nDo you want to save it? (Y/N):").strip()
    while rep not in ["Y","N"]:
        rep = input("Please enter Y or N:").strip()
    if rep=="Y":
        file_name="data-saved(WebReconX).txt"
        
        with open(file_name,"w",encoding="utf-8") as f:
               f.write(save_data)
        print(f"\n[bold green]Data saved [/](FileName:{file_name})")
    else:
        print("\n[bold red]Data not saved ❌")


else:
    print("❌ ERROR: Failed to fetch WHOIS data")

print("\n[italic cyan][!] This tool is a work in progress. More features coming soon![/]")







