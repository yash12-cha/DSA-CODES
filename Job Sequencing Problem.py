def JobScheduling(N,profits,deadlines):
    # Combine profit and deadline of jobs in single list
    jobs = []
    for i in range(N):
        l = []
        l.append(profits[i])
        l.append(deadlines[i])
        jobs.append(l)

    # Sort the jobs array in the descending order of the profit associated with each job.
    jobs.sort(key=lambda x: x[0], reverse=True)

    # Find the maximum deadline among all the jobs.
    maxDeadline = 0
    for i in range(N):
        maxDeadline = max(maxDeadline,jobs[i][1])

    # Create a slots list of size maxDeadline + 1
    slots = []

    # Initialize the array to false initially.
    for i in range(maxDeadline + 1):
        slots.append(False)
        
    maxProfit = 0
    num = 0
    for i in range(N):
        x = jobs[i][1]
        while x>0:
            if slots[x] == False:
                maxProfit = maxProfit + jobs[i][0]
                num += 1
                slots[x] = True
                break
            x -= 1
    return num,maxProfit


N = int(input("Input number of jobs: "))
profits = list(map(int,input("Input Profits: ").split()))
deadlines = list(map(int,input("Input Deadlines: ").split()))
num,maxProfit = JobScheduling(N,profits,deadlines)
print("Number of jobs done: ",num,end=" ")
print()
print("Maximum profit: ",maxProfit,end=" ")

'''
Input:
Input number of jobs: 4
Input Profits: 20 10 40 30
Input Deadlines: 4 1 1 1

Output:
Number of jobs done:  2 
Maximum profit:  60 
'''


'''
Time Complexity: -
O(N * maxDeadline), where ‘N’ denotes the number of elements of the array “jobs,” and ‘maxDeadline’ is the maximum available deadline among all the jobs.
As for every index of the array “jobs”, we may have to search for all the indices of the array “slots”. Hence, the time complexity in the worst case will be O(N * maxDeadline).
'''
