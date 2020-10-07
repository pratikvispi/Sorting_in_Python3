def partition_index(arr,start,end):
    i = start - 1
    pivot = arr[end]

    for j in range(start,end):
        if arr[j] < pivot:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[end] = arr[end] , arr[i+1]

    return (i+1)

def quickSort(arr,start,end):
    if start < end:
        pi = partition_index(arr,start,end)
        quickSort(arr,start,pi-1)
        quickSort(arr,pi+1,end)


arr=[5,4,3,2,1]
n = len(arr)
quickSort(arr,0,n-1)
print(arr)