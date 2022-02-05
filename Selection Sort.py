def selectionSort(self, Arr,N):
        for i in range(0,N-1):
            mini = i
            for j in range(i+1,N):
                if Arr[j] < Arr[mini]:
                    mini = j
            temp = Arr[i]
            Arr[i] = Arr[mini]
            Arr[mini] = temp
        return Arr
