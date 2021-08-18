import subprocess
from pip._vendor.colorama import Fore
import threading
import time
import os
#import layn # Silmeyiniz Yoksa Çal1şma3acak

subprocess.call('start https://discord.gg/akargang', shell=True)
subprocess.call('start https://github.com/DiabloAkar', shell=True)
subprocess.call('start https://github.com/yusufakartr', shell=True)

# Diablo Akar CODE OWNER

bammer = '''
                                                                                              
  ______   _______ _______  ___     _______     ___ ___ ___ ___ _______ ___ ___ _______ 
 |   _  \ |   _   |   _   \|   |   |   _   |   |   Y   |   Y   |   _   |   Y   |   _   |
 |.  |   \|.  1   |.  1   /|.  |   |.  |   |   |   1   |.  |   |   1___|.  |   |.  1___|
 |.  |    |.  _   |.  _   \|.  |___|.  |   |    \_   _/|.  |   |____   |.  |   |.  __)  
 |:  1    |:  |   |:  1    |:  1   |:  1   |     |:  | |:  1   |:  1   |:  1   |:  |    
 |::.. . /|::.|:. |::.. .  |::.. . |::.. . |     |::.| |::.. . |::.. . |::.. . |::.|    
 `------' `--- ---`-------'`-------`-------'     `---' `-------`-------`-------`---'    
                                                                                                                                                                                                                                                                                                                                                                                  

'''
print()
print(Fore.RED+bammer)
print(Fore.WHITE+'3|'+Fore.BLUE+'| >'+Fore.WHITE+' Code Owner Diablo Akar > AKARGANG ')
print(Fore.WHITE+'1|'+Fore.BLUE+'| >'+Fore.WHITE+' Developer Yusuf Akar > AKARGANG ')
print()

granted = False
def grant():
    global granted
    granted = True
def login(name,password):
    success = False
    file = open("data.txt","r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==name and b==password):
             success = True
             break
    file.close()
    if(success):
        print("Giriş Başarılı")
        grant()
    else:
        print("Geçerli Şifre")
        
def register(name,password):
    file = open("data.txt","a")
    file.write("\n"+name+","+password)
    grant()
def access(option):
    global name
    if(option=="giris"):
        name = input("Kullanıcı Adınızı Giriniz: ")
        password = input("Sifrenizi Giriniz: ")
        login(name,password)
    else:
        print("Kayıt'a hoşgeldiniz İlk önce Kullancıadı > sifre")
        name = input("Kullanıcı adı oluşturunuz: ")
        password = input("Sifre Oluşturunuz: ")
        register(name,password)

def begin():
    global option
    print("Hoşgeldiniz Giriş Yaparak Devam Ediniz")
    option = input("Giriş Veya Kayıt Olunuz | giris > kayit: ")
    if(option!="giris" and option!="kayit"):
        begin()
        
begin()
access(option)