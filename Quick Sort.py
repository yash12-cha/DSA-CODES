class Solution:
    #Function to sort a list using quick sort algorithm.
    def partition(self,arr,lb,ub):
        pivot = arr[lb]
        start = lb + 1
        end = ub
        while True:
            while (start <= end and arr[start] <= pivot):
                start += 1
            while (start <= end and arr[end] >= pivot):
                end -= 1
            if (start < end):
                arr[start], arr[end] = arr[end], arr[start]
            else:
                break
        arr[lb], arr[end] = arr[end], arr[lb]
        return end
        
    def quickSort(self,A,left,right):
        if left < right:
            pi = self.partition(A,left,right)
            self.quickSort(A,left,pi-1)
            self.quickSort(A,pi+1,right)
