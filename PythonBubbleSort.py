# Define the function
def bubbleSort(arr, size):
  # first loop
    for i in range(size-1):
        print("\nProcess number: ", i+1)
        # second loop
        for j in range(size-1):
            # checks the elements one by one
            if arr[j] > arr[j+1]:
                # switch positions
                temp = j+1
                (arr[j], arr[temp]) = (arr[temp], arr[j])
            print(arr)
        size = size-1

array = [7,1,8,9,4,3,5,0,11,10,6]
size = len(array)
# call the function
bubbleSort(array, size)
print("\nFinal result:")
print(array)
