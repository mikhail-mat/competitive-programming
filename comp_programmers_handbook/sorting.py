arr = [10,9,3,4,2,8,1]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    k = (len(arr)-1) // 2
    left = merge_sort(arr[:k+1])
    right = merge_sort(arr[k+1:])
    
    i = j = 0
    res = []

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1
    
    res.extend(left[i:])
    res.extend(right[j:])

    return res

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
print(merge_sort(unsortedArr))
