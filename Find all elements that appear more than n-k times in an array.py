N = int(input("Enter the value of N: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:N]
K = int(input("Enter the value of K: "))
freq = {}
x = N//K
for i in range(N) :   
        if Arr[i] in freq :
            freq[Arr[i]] += 1
        else :
            freq[Arr[i]] = 1
for i in freq :
        if (freq[i] > x) :
            print(i)
