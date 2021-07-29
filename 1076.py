# 输入头尾，求最多不相交线段序列，贪心

class Gene:  # 定义基因类，先比左，后比右
    def __init__(self, Idx, Left, Right):
        self.idx = Idx
        self.left = Left
        self.right = Right

    def __str__(self):
        return str(self.idx)

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __le__(self, other):
        if self.left == other.left:
            return self.right < other.right
        else:
            return self.left < other.left

    def __gt__(self, other):
        if self.left == other.left:
            return self.right > other.right
        else:
            return self.left > other.left


while 1:
    n = int(input())
    if not n:
        break

    gene = []
    for i in range(n):
        temp_line = input().split(' ')
        gene.append(Gene(i + 1, int(temp_line[0]), int(temp_line[1])))
    gene.sort()

    res = [gene[0]]
    for i in range(1, n):  
        if gene[i].left > res[-1].right:  # 如果这个基因的 左 比结尾要大，加入这个基因
            res.append(gene[i])
        elif gene[i].right < res[-1].right:  # 如果这个基因的 右 比结尾小，将这个基因替换成结尾；其余情况都是浪费或不合法
            res[-1] = gene[i]

    print(' '.join(str(j) for j in res))
