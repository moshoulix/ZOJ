def f(X):
    Sum = 0
    for i in range(2, 300):
        Sum += 1 / i
        if Sum > X:
            return i


while 1:
    x = float(input())
    if not x:
        break
    print(f(x)-1, 'card(s)')
