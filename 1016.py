# 对于一个合法的括号序列，有两种编码
# P编码pi表示第i个右括号的左边有几个左括号
# W编码wi表示第i个右括号和匹配的左括号有几个左括号包括自己
# p2w

t = int(input())
for _ in range(t):
    n = int(input())
    temp_line = input().split(' ')
    p = []
    for i in temp_line:
        p.append(int(i))

    temp = 0
    s = []
    w = []
    for i in p:  # 后项减前项，得出每个右括号之间有几个左括号
        s.append(i - temp)
        temp = i
    for i in range(n):  # 匹配：如果当前位置右括号和上一个右括号之间有左括号，那么w一定是1
        if s[i]:
            w.append(1)
            s[i] -= 1
        else:          # 如果没有左括号那么向前寻找不为0的位置
            temp_s = s[:i]
            temp_s.reverse()
            for j in range(len(temp_s)):
                if temp_s[j]:
                    w.append(j + 2)
                    s[i - j - 1] -= 1
                    break

    print(' '.join(str(i) for i in w))
