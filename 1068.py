# 莫斯电码

dict1 = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..', '_': '..--', '.': '---.', ',': '.-.-', '?': '----'}

dict2 = {value: key for key, value in dict1.items()}

n = int(input())
for i in range(n):
    mes = input()
    text = ''
    numbers = []
    for letter in mes:
        temp = dict1[letter]
        text += temp
        numbers.append(len(temp))
    numbers.reverse()
    idx = 0
    res = ''
    for num in numbers:

        res += dict2[text[idx:idx+num]]
        idx = idx + num
    print('{}: {}'.format(i + 1, res))
