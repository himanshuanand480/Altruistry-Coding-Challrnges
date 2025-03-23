str1 = input().strip()
n = int(input().strip())
queries = [tuple(map(int, input().split())) for _ in range(n)]
def Treasure_hunter(str1, queries):
    res = []
    for i,j in queries:
        res.append(str1[i-1:j].count('T'))
    return res
res=Treasure_hunter(str1, queries)
for ans in res:
    print(ans)

#Time Complexity:O(N)
#Space Complexity:O(1)
