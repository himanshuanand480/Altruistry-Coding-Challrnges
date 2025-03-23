n = int(input().strip())
a = input().strip()
b = input().strip()
def brute_force_min_swaps(n, a, b):
    if sorted(a) != sorted(b):
        return -1
    a = list(a)
    swaps = 0
    for i in range(n):
        target1 = a.index(b[i]) 
        while target1 > i:
            a[target1], a[target1 - 1] = a[target1 - 1], a[target1]
            target1 -= 1
            swaps += 1
    return swaps
print(brute_force_min_swaps(n, a, b))

#Time Complexity:O(N3)
#Space Complexity:O(N)
