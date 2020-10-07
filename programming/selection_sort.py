def selection(arr):
    n = len(arr)
    swaps = 0

    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i] , arr[min_index] = arr[min_index],arr[i]
        swaps+=1
    return arr,swaps

A = [64, 25, 12, 22, 11] 
print(selection(A))