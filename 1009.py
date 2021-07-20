# 加解密  字典求反函数
# 解密步骤：1变成数字；2减去旋转；3字典逆映射；4加上旋转；5变成小写字母（2到4步骤需要重复三次，因为是三次映射）
# ACE       024        012      105       117     111 bbb

case = 0
while 1:
    n = int(input())
    if not n:
        break

    rotors = []
    for _ in range(3):
        temp_row = []
        for letter in input():
            temp_row.append(ord(letter) - 65)
        rotors.append(dict(zip(temp_row, list(range(n)))))  # 反向字典
    codes = []
    m = int(input())
    for _ in range(m):
        temp_row = []
        for letter in input():
            temp_row.append(ord(letter) - 65)
        codes.append(temp_row)

    case += 1
    if case != 1:
        print()
    print('Enigma {}:'.format(case))

    for i in range(m):
        code = codes[i]
        for j in range(len(code)):
            step = [j % n, (j // n) % n, (j // (n * n)) % n]
            res = code[j]
            for k in (2, 1, 0):  # 倒着来
                res = rotors[k][(res - step[k]) % n] + step[k]
            print(chr(res % n + 97), end='')
        print()
