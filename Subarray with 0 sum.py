def zerosubarray(arr,n):
    for i in range(n):
        s=0
        for j in range(i,n):
            s=s+arr[j]
            if(s==0):
                return(True)
    return(False)
N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:N]
if(zerosubarray(Arr,N)):
    print("Yes")
else:
    print("No")
