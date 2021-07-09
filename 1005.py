# 水壶倒水问题 输入多个 小水壶 大水壶 目标
# 输出方案
# a b 互质则一定可以达到目标
#
# 解决：如果a空就灌满，a倒入b，判断b是否成功，重复

def prt(List):
    numbers = {
        0: 'fill A',
        1: 'fill B',
        2: 'empty B',
        3: 'pour A B',
        4: 'success'
    }
    for num in List:
        print(numbers.get(num))


try:
    while 1:
        x = input().split(' ')
        a = int(x[0])
        b = int(x[1])
        n = int(x[2])

        if b == n:
            prt([1, 4])
        else:
            res = []
            temp_a = temp_b = 0
            while 1:
                if temp_a == 0:
                    res.append(0)
                    temp_a = a

                res.append(3)
                (temp_a, temp_b) = (0, temp_a + temp_b) if temp_a + temp_b <= b else (temp_a + temp_b - b, b)

                if not temp_a:
                    if temp_b == n:
                        res.append(4)
                        break
                else:
                    res.append(2)
                    temp_b = 0
            prt(res)

except EOFError:
    pass
