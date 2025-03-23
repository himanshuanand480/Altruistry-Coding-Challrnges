from collections import deque
k=int(input())
n=int(input())
arr1= [int(input().strip()) for _ in range(n)]
def optimal_min_of_max_brightness(k, arr):
    deque1 = deque()
    max1 = []
    for i in range(k):
        while deque1 and arr[deque1[-1]] <= arr[i]:
            deque1.pop()
        deque1.append(i)
    for i in range(k,len(arr1)):
        max1.append(arr[deque1[0]])     
        while deque1 and deque1[0] <= i - k:
            deque1.popleft()
        while deque1 and arr1[deque1[-1]] <= arr1[i]:
            deque1.pop()
        deque1.append(i)
    max1.append(arr1[deque1[0]])
    return min(max1)
print(optimal_min_of_max_brightness(k, arr1))


#Complexity
#Time:O(N)
#Space:O(K)
