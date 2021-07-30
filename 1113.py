# 计算e

print('n e')
print('- -----------')
print('0 1')
print('1 2')
print('2 2.5')
res = 2.5
factorial = 2
for i in range(3, 10):
    factorial *= i
    res += 1 / factorial
    print('{} {:.9f}'.format(i, res))
