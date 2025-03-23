k=int(input())
n=int(input())
arr1 = [int(input().strip()) for _ in range(n)] 
def brute_force_min_of_max_brightness(k, arr1):
    max_values = []
    for i in range(len(arr1) - k + 1):
        max_values.append(max(arr1[i:i + k]))
    return min(max_values)
print(brute_force_min_of_max_brightness(k, arr1))

#Time Complexity:O(NxK)
#Space Complexity:O(1)
