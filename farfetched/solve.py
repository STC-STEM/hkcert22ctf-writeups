flag = ['*' for _ in range(64)]

def sf(i, j, offset = 0): # set flag
    flag[i] = chr(ord(flag[j]) - offset)

#knowns

flag[0] = 'h'
flag[1] = 'k'
flag[2] = 'c'
flag[3] = 'e'
flag[4] = 'r'
flag[5] = 't'
flag[6] = '2'
flag[7] = '2'
flag[8] = '{'

#sorted

sf(51, 0)
sf(9, 1)
sf(61, 2, -2)
sf(10, 3)
sf(34, 4)
sf(23, 5)

flag[47] = chr(ord(flag[6])*2)
flag[26] = chr((ord(flag[7])-1)*2)
sf(28, 26, -5)
sf(36, 28)
sf(12, 36, -2)
sf(17, 12)
sf(27, 17)
sf(48, 27)
sf(16, 48, -12)
sf(38, 16)
sf(45, 38)
sf(29, 45, -2)
sf(11, 29, -2)
sf(32, 11)
sf(56, 32)

sf(37, 51, -2)
sf(20, 37, -2)
sf(22, 20, -2)
sf(46, 22)
sf(49, 46)
sf(40, 49, -2)
sf(15, 40, -1)
sf(13, 15, -2)
sf(41, 13)

sf(33, 47, -2)
sf(18, 33, -16)
sf(31, 18, -2)

flag[53] = 'c'
sf(19, 53, 2)
sf(30, 19)

sf(39, 9, -2)
sf(25, 39, -2)
sf(35, 25)
sf(44, 35)

#TODO

sf(55, 8, 1)

sf(14, 10)




sf(21, 14)







sf(52, 21)

sf(24, 23)
sf(50, 24)






sf(42, 30)

sf(62, 31, 4)


sf(43, 34)


sf(12, 36, -2)





sf(57, 41)
sf(63, 42, -28)
sf(59, 43)
sf(54, 44)




sf(16, 48, -12)

sf(58, 50)


sf(60, 52)



for c in flag:
    print(c, end='')
print()
