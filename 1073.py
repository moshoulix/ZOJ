# 循环数检测 142857 * 7 = 999999

try:
    while 1:
        flag = 1
        text = input()
        number = int(text) * (len(text) + 1)
        for num in str(number):
            if num != '9':    
                print('{} is not cyclic'.format(text))
                flag = 0
                break
        
        if flag:
            print('{} is cyclic'.format(text))

except EOFError:
    pass
