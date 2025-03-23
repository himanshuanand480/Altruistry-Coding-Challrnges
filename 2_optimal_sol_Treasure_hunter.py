def preprocess_prefix(s):
    prefix = [0] * (len(s) + 1) 
    for i in range(1, len(s) + 1):
        prefix[i] = prefix[i - 1] + (1 if s[i - 1] == 'T' else 0)   
    return prefix
def count_treasures(s, queries):
    prefix = preprocess_prefix(s)
    results = []
    for l, r in queries:
        results.append(prefix[r] - prefix[l - 1])
    return results
s = input().strip()
n = int(input().strip())
queries = [tuple(map(int, input().split())) for _ in range(n)]
results = count_treasures(s, queries)
for res in results:
    print(res)

#Time Complexity:O(N)
#Space Complexity:O(N)
