# 矩阵乘法包括多少次乘法，栈

class Matrix:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y


# 如果左括号 或 矩阵 加入，如果右括号 找到前一个左括号计算再加入矩阵积
def solve(Ex):
    global res
    stack = []
    for temp in Ex:
        if temp == '(':
            stack.append(temp)

        elif temp == ')':
            temp_stack = stack[::-1]
            idx = len(stack) - 1 - temp_stack.index('(')
            multi = stack[idx + 1:]
            stack = stack[:idx]
            if multi:
                matrix = multi.pop(0)
                for i in multi:
                    if matrix.y == i.x:
                        matrix = Matrix(matrix.x, i.y)
                        res += matrix.x * i.x * i.y
                    else:
                        return False
                stack.append(matrix)

        else:
            stack.append(matrix_list[name_list.index(temp)])

    if stack:
        matrix = stack.pop(0)
        for i in stack:
            if matrix.y == i.x:
                matrix = Matrix(matrix.x, i.y)
                res += matrix.x * i.x * i.y
            else:
                return False
    return True


n = int(input())
name_list = []
matrix_list = []
for _ in range(n):
    temp_line = input().split(' ')
    name_list.append(temp_line[0])
    matrix_list.append(Matrix(int(temp_line[1]), int(temp_line[2])))

try:
    while 1:
        expression = input()
        res = 0
        if solve(expression):
            print(res)
        else:
            print('error')

except EOFError:
    pass
