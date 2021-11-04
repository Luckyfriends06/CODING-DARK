#!/bin/python
# PEROGAM PERULANGAN KATA BY ABU

# module
import os,sys,time
from time import sleep

# tampilan
os.system ('clear')
os.system ('figlet PERULANGAN KATA BY ABU')
sleep(1)
print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
print('       〤 SILAHKAN GUNAKAN NGAB 〤')
print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
print('        ')
print('MASUKAN KATA" KAMU')
kata = input('━> ')
print(' MASUKAN JUMLAH KATA')
jumlah = int(input('━> '))

#data
try:
  for i in range(jumlah):
      print('〤 ' + kata)
      sleep(0.30)
      print('〤 ' + kata)
      sleep(0.30)

except:
      print('BERHASIL')
