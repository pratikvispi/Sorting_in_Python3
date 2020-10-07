def insertion(arr):
    n = len(arr)

    for i in range(n):
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr



arr = [12, 11, 13, 5, 6] 
print(insertion(arr)) 