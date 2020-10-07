def bubbleSort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1],arr[j]
                print(swaps)
                swaps += 1
                
    print(arr,swaps)


arr = [64, 34, 25, 12, 22, 11, 90] 
  
bubbleSort(arr) 
