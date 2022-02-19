def JobScheduling(self,jobs,n):
        jobs.sort(key = lambda x: x.profit,reverse = True)
        maxProfit = 0
        maxDeadline = 0

        # Find the maximum deadline among all the jobs.
        for i in range(0, len(jobs)):
            maxDeadline = max(maxDeadline, jobs[i].deadline)
    
        # Create a slots list of size maxDeadline + 1.
        slots=[]

        # Initialize the array to false initially.
        for i in range(0, maxDeadline + 1):
            slots.append(False)
        num = 0 
        maxProfit = 0
        for i in range(len(jobs)):
            x = jobs[i].deadline
            while x > 0:
                if slots[x] == False:
                    maxProfit = maxProfit + jobs[i].profit
                    num += 1
                    slots[x] = True
                    break
                x -= 1
        
        return num,maxProfit
'''
Time Complexity: -
O(N * maxDeadline), where ‘N’ denotes the number of elements of the array “jobs,” and ‘maxDeadline’ is the maximum available deadline among all the jobs.
As for every index of the array “jobs”, we may have to search for all the indices of the array “slots”. Hence, the time complexity in the worst case will be O(N * maxDeadline).
'''
