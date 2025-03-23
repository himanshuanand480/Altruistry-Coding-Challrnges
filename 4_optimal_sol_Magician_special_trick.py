n = int(input().strip())
a = input().strip()
b = input().strip()
def optimized_min_swaps(n, a, b):
    if sorted(a) != sorted(b):
        return -1
    swaps = 0
    a = list(a)
    for i in range(n):
        target1 = a.index(b[i]) 
        while target1 > i:
            a[target1], a[target1- 1] = a[target1-1], a[target1]
            target1-= 1
            swaps += 1 
    return swaps
print(optimized_min_swaps(n, a, b))

#if input n<=10^5:
#Time Complexity:O(N2)
#Space Complexity:O(N)

#if input n>10^5:
#Time Complexity:O(NlogN)
#Space Complexity:O(N)
