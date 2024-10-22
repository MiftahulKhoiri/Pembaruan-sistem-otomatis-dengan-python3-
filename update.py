import os
from time import sleep

r1=('/data/data/com.termux/files/home')
r2 = ('cd')
h1=r2,r1
def t (t1,t2):
    tt1=sleep(t1)
    tt2=sleep(t2)
    return tt1,tt2
    
def s (i): 
    o1=os.system(i)
    return o1

def rumah ():
    o2 = s (r2)
    return o2
    
def update ():
    s('clear')
    rumah()
    print ('cek pembaruan paket')
    t(5,2)
    s('apt update')
    t(2,2)
    s('clear')
    print ('paket yang akan di tingkat kan ')
    s('apt list --upgradable')
    t(3,0)
    print('peningkatan paket ')
    t(2,3)
    s('apt upgrade  -y')
    s('clear')
    t(3,0)
    print('pembaruan selesai ')
    
    
    
#mulai program 
print (f"{'SELAMAT DATANG':^45}")
print (''' ini adalah script pembaruan firwer secara
 otomatis apakah anda setuju'''
)

while True :
    T = input(' (y/n) : ')
    if T == 'y':
        print (f"{'MULAI':^45}")
        update()
    elif T == 'Y':
        print (f"{'MULAI':^45}")
        update()
        
    elif T == 'n':
        print (f"{'perogram selesae ':^45}")
        exit()
        
    elif T == 'N':
        print (f"{'perogram selesae ':^45}")
        exit()
        
        
    else :
        print ('Pilhan salah ulangi lagi ')

