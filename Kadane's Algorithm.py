n = int(input("Enter number of elements: "))
a = list(map(int,input("Enter the elements: ").strip().split()))[:n]
max_so_far =a[0] 
curr_max = a[0] 
for i in range(1,len(a)):
    curr_max = max(a[i], curr_max + a[i]) 
    max_so_far = max(max_so_far,curr_max)
print("Max Subarray Sum: ",max_so_far)
