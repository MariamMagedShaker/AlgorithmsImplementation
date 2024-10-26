
def BinarySearch(sorted_array,item):
    low=0
    high=len(sorted_array)-1
    
    while low <= high:
        mid= (low+high) //2
        var=sorted_array[mid]
        
        if item == var :
            return mid
        elif item > var:
            low = mid + 1
        else:
            high = mid - 1

    return None




