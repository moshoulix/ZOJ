# 加解密


def text2code(cipher_text):
    cipher_code = []
    for code in cipher_text:
        if code == '_':
            cipher_code.append(0)
        elif code == '.':
            cipher_code.append(27)
        else:
            cipher_code.append(ord(code) - 96)
    return cipher_code


def code2text(plain_code):
    plain_text = []
    for code in plain_code:
        if code == 27:
            plain_text.append('.')
        elif code == 0:
            plain_text.append('_')
        else:
            plain_text.append(chr(code + 96))
    return plain_text


while 1:
    x = input().split(' ')
    if x[0] == '0':
        break

    k = int(x[0])
    y = text2code(x[1])
    n = len(x[1])
    ans = [1] * n
    for i in range(0, n):
        a = (y[i] + i) % 28
        t = (k * i) % n
        ans[t] = a

    print(''.join(code2text(ans)))
