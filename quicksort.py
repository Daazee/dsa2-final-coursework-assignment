def quickSort(word_array, low, high):
    if low < high:
        # Partition the array using the second-to-last element in the array
        pivot_index = partition(word_array, low, high)

        quickSort(word_array, low, pivot_index - 1) #sort left array recursively
        quickSort(word_array, pivot_index + 1, high) #sort right array recursively

def partition(word_array, low, high):
    pivot_index = high - 1 # choose the second-to-last element as the pivot
    pivot_value = word_array[pivot_index] #pivot

    # temporarily swap the pivot to the end for easier partitioning
    swap(word_array, pivot_index, high)

    # Index of smaller element
    left = low - 1

    # loop through and move smaller elements compare to the pivot value to the left
    for right in range(low, high):
        if word_array[right] < pivot_value:
            left += 1
            swap(word_array, left, right)

    # Move pivot after smaller elements in the array and return its position
    left = left + 1
    swap(word_array, left, high)
    return left

def swap(word_array, left, right):
     temp =  word_array[left]
     word_array[left] = word_array[right]
     word_array[right] = temp


#testing the quicksort function
word_array = ["ban", "arrow", "and", "cat", "dog","book", "elephant"]
array_length = len(word_array)

quickSort(word_array, 0, array_length - 1)

for value in word_array:
    print(value, end=" ")
