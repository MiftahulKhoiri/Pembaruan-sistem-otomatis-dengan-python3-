import os
from time import sleep

def s (t1,t2):
    tt1=sleep(t1)
    tt2=sleep(t2)
    return tt1,tt2
    
def o (i):
    o1=os.system(i)
    return o1
    
def update ():
    os.system('clear')
    print ('cek pembaruan paket')
    s(5,2)
    o('apt update')
    s(2,2)
    os.system('clear')
    print('peningkatan paket ')
    s(2,3)
    o('apt upgrade  -y')
    os.system('clear')
    s(3,0)
    print('pembaruan selesai ')
    exit()
    
    
    
print (f"{'SELAMAT DATANG':^45}")
print (''' ini adalah script pembaruan firwer secara otomatis '''
)

while True :
    t = input('apakah anda setuju:  (y/n)')
    if t == 'y':
        print (f"{'MULAI':^45}")
        update()
        
    elif t == 'n':
        print ("{'perogram selesae ':^45}")
        exit()


