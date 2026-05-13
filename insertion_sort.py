# Insertion Sort in Monotonically Decreasing Order
def insertion_sort_desc(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        # Change comparison for decreasing order
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr
numbers = [5, 2, 9, 1, 7, 6]
print("Original Array:")
print(numbers)
sorted_numbers = insertion_sort_desc(numbers)
print("Sorted Array in Monotonically Decreasing Order:")
print(sorted_numbers)