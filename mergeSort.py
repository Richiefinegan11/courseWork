#import module to help show time efficiency
import time
start_time = time.time()

#create a function that takes the parameter of an array
def mergeSort(arr):
    
    #check if the array is equal to 1 and return if true, because it is already sorted
    if len(arr) > 1:
        split = len(arr) // 2
        left = arr[split:]
        right = arr[:split]
    
        #recursively call and merge sort the arrays
        mergeSort(left)
        mergeSort(right)
        
        """
        set variable 'a' to track the smallest number in the left array and
        'b' to keeptrack of the smallest in the right, while c is set to keep
        track of the index of the sorted array
        """
        a = b = c = 0
        
        
        while a < len(left) and b < len(right):
            """
            check if the first element in the left array is smaller than the first
            element in the right array and pushes to the sorted array if true
            """
            if left[a] <= right[b]:
                arr[c] = left[a]
                #moves to the next index if the above statement is true
                a += 1
            #if the above statement is not true, it pushes the first element in the
            #right array
            else:
                arr[c] = right[b]
                #moves to the next index if the above statement is true
                b += 1
            #moves to the next index in the sorted array, to push more numbers
            c += 1
        
        #check if there is any elements left in the left array
        while a < len(left):
            #push the number to the sorted array if above statement is true
            arr[c] = left[a]
            #moves the the next index in the left array, if needed
            a += 1
            #moves to the next index in the sorted array, to push more numbers
            c += 1
            
        while b < len(right):
            arr[c] = right[b]
            #moves the the next index in the left array, if needed
            b += 1
            #moves to the next index in the sorted array, to push more numbers
            c += 1

#function for printing the array
def printArr(arr):
    
    mergeSort(arr)
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    
    print("--- %s seconds ---" % (time.time() - start_time))
 

# Driver code
if __name__ == '__main__':

    arr = [0,1,44,5,7,9,44,6,32,10,15,90,100]
    print("First sorted array is: ")
    printArr(arr)
    
    arr2 = [7,312,16,32,11,17,314,63,77]
    print("\nSecond sorted array is: ")
    printArr(arr2)
    
    arr3 = [1,2,3,4,5,6,7,8,9,12,15]
    print("\nThird sorted array is: ")
    printArr(arr3)
    