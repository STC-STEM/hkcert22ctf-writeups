from itertools import combinations

characters = " " + "abcdefghijklmnopqrstuvwxyz1234567890{}-_"
memory = [6, 126, 330, 225, 6, 77, 297, 230, 28, 49, 440, 80, 2, 329, 528, 245, 100, 133, 209, 15, 72, 28, 55, 195, 102, 7, 22, 5, 28, 364, 583, 20, 72, 98, 55, 20, 108, 280, 121, 25, 50, 112, 330, 20, 110, 392]

def get_j(count):
    j = len(memory)
    for _ in range(count + 1):
        j = (j + 2) % 4 + 1
    return j - 1

def check_and_decrypt(keys):
    decrypt = ''
    for e in range(len(memory)):
        j = get_j(e)
        char_idx = int(round(memory[e] / keys[j], 0))

        if char_idx <= 0 or char_idx >= len(characters):
            decrypt += ''
        else:
            decrypt += characters[char_idx]
    if 'pass' in decrypt:
        return decrypt
    return None

def format_flag(flag_content):
    return 'hkcert22{' + flag_content + '}'

def output_filter(possible_flag):
    if None == possible_flag:
        return
    # print(format_flag(possible_flag))
    if '_' in possible_flag:
        print(format_flag(possible_flag))

print('All possible flags:')
for (a, b, c, d) in combinations(range(len(memory)), 4):
    keys = [0, 0, 0, 0]
    keys[get_j(a)] = memory[a] / characters.index('p')
    keys[get_j(b)] = memory[b] / characters.index('a')
    keys[get_j(c)] = memory[c] / characters.index('s')
    keys[get_j(d)] = memory[d] / characters.index('s')
    if any([x == 0 for x in keys]):
        continue
    output_filter(check_and_decrypt(keys))
