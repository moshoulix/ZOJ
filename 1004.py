# dfs
# 给两个字符串 输出所有方案：第一个出栈入栈的方案以成为第二个字符串

def prt(p):  # 打印
    for i in p:
        print(i, end=' ')
    print()
    return


def dfs(i, j, a, b, stack):
    if i >= 2 * len(x):
        if b == y:
            prt(a)
        return
    if j < len(x):
        a.append('i')
        stack.append(x[j])
        dfs(i+1, j+1, a, b, stack)
        a.pop()
        stack.pop()
    if stack:
        a.append('o')
        c = stack.pop()
        b.append(c)
        dfs(i+1, j, a, b, stack)
        a.pop()
        b.pop()
        stack.append(c)


try:
    while 1:
        x = input()
        y = list(input())
        print('[')
        dfs(0, 0, [], [], [])
        print(']')

except EOFError:
    pass
