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

print (f"{'pembaruan selesai':^45}")

