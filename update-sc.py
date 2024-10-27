import os 
from time import sleep

def t (i1,i2):
    t1 = sleep (i1)
    t2 = sleep (i2)
    return t1,t2
    
def s (i):
    o1 = os.system (i)
    return o1

s ('clear ')
print (f"{'cek pembaruan script':^45}")
s ('cd')
s ('pwd')
s ('rm -rf Pembaruan-sistem-otomatis-dengan-python3-/')

t (2,2)
s ('git clone https://github.com/MiftahulKhoiri/Pembaruan-sistem-otomatis-dengan-python3-.git')
t (3,0 )
s ('clear ')
print ('mengolah data ')
s ('rm -rf update-sc.py')
s ('rm -rf update.py')
s ('cd /data/data/com.termux/files/home/Pembaruan-sistem-otomatis-dengan-python3-/')
s ('cp update-sc.py /data/data/com.termux/files/home')
s ('cp update.py /data/data/com.termux/files/home')
s ('cd')
s ('rm -rf Pembaruan-sistem-otomatis-dengan-python3-/')

print (f"{'pembaruan selesai':^45}")


