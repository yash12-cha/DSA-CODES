N = int(input())
K = int(input())
Arr = []
p = float('inf')
for i in range(0, N):
    ele = int(input())
    Arr.append(ele)
Arr.sort()
for i in range(0,N-K+1):
    temp = Arr[i+K-1] - Arr[i]
    if temp < p:
        p = temp
print(p)
