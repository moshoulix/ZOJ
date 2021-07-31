# 给定几类长方体的长宽高，求塔的最大高度
# 要求上面的长宽必须要小于下面的 动态规划

class Block:
    def __init__(self, lis):
        self.x, self.y = (lis[0], lis[1]) if lis[0] <= lis[1] else (lis[1], lis[0])
        self.z = lis[2]

    def __gt__(self, other):
        return self.x > other.x or (self.x == other.x and self.y > other.y)

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.x)+' '+str(self.y)+' '+str(self.z)


def can_place(block):
    result = []
    for t in range(n):
        if blocks[t].x < block.x and blocks[t].y < block.y:
            result.append(t)
    return result


idx = 0
while 1:
    n = int(input())
    if not n:
        break

    blocks = []
    for _ in range(n):
        temp_line = list(map(int, input().split(' ')))
        blocks.append(Block(temp_line))
        flag = [temp_line[2]]
        for _ in range(2):
            temp_line.append((temp_line.pop(0)))
            if temp_line[2] not in flag:
                blocks.append(Block(temp_line))
                flag.append(temp_line[2])
    blocks.sort()  # 排序，保证所有能放到上面的块都在前面
    n = len(blocks)
    dp = [0 for _ in range(n)]  # 代表第几个block为底时最大高度，检测前面的块哪个能放上去，并且找最大的
    for i in range(n):
        temp_block = blocks[i]
        try:
            dp[i] = max(dp[j] for j in can_place(temp_block)) + blocks[i].z
        except ValueError:  # max不能取空列表所以try
            dp[i] = blocks[i].z
    idx += 1
    print('Case {}: maximum height = {}'.format(idx, max(dp)))
