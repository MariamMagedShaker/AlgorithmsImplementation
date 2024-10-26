from SelectionSort import SelectionSort
from BinarySearch import BinarySearch




if __name__ == "__main__":
    
    length_Array=int(input("please enter the length of the array: "))
    # Below line read inputs from user using map() function
    arr = list(map(int, input("\nEnter the numbers : ").split()))[:length_Array]
 
    print("\nList is - ", arr)
    search= int(input("\nplease enter the element you want to search: "))

    sorted_array=SelectionSort(arr)
    
    print(f"\nThe reesult of sorting the array using Selection Sort : {sorted_array} ")

    print(f"\nThe Index of Element {search} after sorting the array is {BinarySearch(sorted_array,search)}")


