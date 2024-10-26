def SelectionSort(arr):
    sorted_arr=[]
    for i in range(len(arr)):
        smallest=arr[0]
        index=0
        for i in range(len(arr)):
            if arr[i]<smallest:
                smallest=arr[i]
                index=i
        sorted_arr.append(smallest)
        arr.pop(index)
    
    return sorted_arr

