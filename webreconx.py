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
while url.find("http://www.")==-1 and url.find("https://www.")==-1:
    print("[red]Invalid URL. Try again (e.g., https://www.example.com)")
    url=input("")
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
    

    """
"""
    path1=requests.get(url+"/sitemap.xml")
    if path1.status_code==200:
        print("\n🗺️[bold grey] SITEMAP.XML\n-----------------------")
        save_data+="\n🗺️ SITEMAP.XML\n-----------------------\n"
        items=[]
        xml=path1.text
        xml=xml[xml.find("<sitemap>"):]
        while xml.find("/sitemap") != -1:
            items.append(xml[xml.find(url)+len(url):xml.find('/sitemap')])
            xml=xml[xml.find("/sitemap") + 1:]
        items=list(set(i.strip() for i in items if i.strip()))
        items.sort()
        for i in range(0, len(items), 3):
            col1 = items[i] if i < len(items) else ""
            col2 = items[i+1] if i+1 < len(items) else ""
            col3 = items[i+2] if i+2 < len(items) else ""
            print(f"{col1:<30} {col2:<30} {col3}")
            save_data+=items[1]+"\n"+items[2]+"\n"+items[3]+"\n"
        
    path2=requests.get(url+"/robots.txt")
    if path2.status_code==200:
        print("\n[bold grey]🧾 ROBOTS.TXT\n-----------------------")
        save_data+="\n🧾 ROBOTS.TXT\n-----------------------\n"
        rtxt=path2.text
        robots=[]
        i=0
        while rtxt!="":
            if rtxt.startswith("User-agent"):
                robots.append("User-agent"+rtxt[rtxt.find(":"):rtxt.find("\n")].strip())   
            elif rtxt.startswith("Allow"):
                robots.append(rtxt[rtxt.find(":")+1:rtxt.find("\n")].strip())  
            rtxt=rtxt[rtxt.find("\n")+1:]
        for x in robots:
            if x.startswith("User-agent"):
                print(f"\n[bold blue]{x}[/bold blue]")
            else:
                print(f"  [green]{x}[/green]")
            save_data+=x+"\n"
    path3=requests.get(url+"/humans.txt")
    if path3.status_code==200:
        print("\n[bold grey]👨‍💻 HUMANS.TXT\n-----------------------")
        save_data+="\n👨‍💻 HUMANS.TXT\n-----------------------\n"
        save_data+=path3.text
        print(path3.text)
    
    path4=requests.get(url+"/ads.txt")
    if path4.status_code==200:
        print("\n[bold grey]📢 ADS.TXT\n-----------------------")
        save_data+="\n📢 ADS.TXT\n-----------------------\n"
        save_data+=path4.text
        print(path4.text)
    
    path5=requests.get(url+"/security.txt")
    if path5.status_code==200:
        print("\n[bold grey]🔐 SECURITY.TXT\n-----------------------")
        save_data+="\n🔐 SECURITY.TXT\n-----------------------\n"
        save_data+=path5.text
        print(path5.text)


    rep = input("\nDo you want to save it? (Y/N):").strip()
    while rep not in ["Y","N"]:
        rep = input("Please enter Y or N:").strip()
    if rep=="Y":
        file_name="data-saved(WebReconX).txt"
        
        with open(file_name,"w",encoding="utf-8") as f:
               f.write(save_data)
        print(f"\n[bold green]Data saved [/](FileName:{file_name})")
    else:
        print("\n[bold red]Data not saved")
        

else:
    print("❌ ERROR: Failed to fetch WHOIS data")

print("\n[italic cyan][!] This tool is a work in progress. More features coming soon![/]")







