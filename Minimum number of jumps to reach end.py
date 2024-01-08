def jump(nums):
    if len(nums) <= 1:
        return 0
    maxi = 0
    maxRange = 0
    jumps = 0
    n = len(nums)
    for i in range(0, n, 1):
        maxi = max(maxi, i + nums[i])
        if maxRange == i:
            maxRange = maxi
            jumps += 1
            if maxRange >= n - 1:
                return jumps
nums = list(map(int,input("Input Array: ").split()))
jumps = jump(nums)
print("Minimum number of jumps to reach end: ",jumps)
