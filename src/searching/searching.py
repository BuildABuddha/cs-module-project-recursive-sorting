# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    if end == -1:
        return -1

    mid = int( (start + end) / 2 )

    if arr[mid] == target:
        return mid
    elif end - start <= 0:
        return -1
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

    # Call private recursive version of this function:
    return __recursive_agnostic_binary_search(arr, target, 0, len(arr) - 1)

def __recursive_agnostic_binary_search(arr, target, start, end):
    mid = int( (start + end) / 2 )

    if end == -1:
        return -1

    if arr[mid] == target:
        return mid
    elif end - start <= 0:
        return -1
    elif (arr[start] < arr[end] and arr[mid] > target) or (arr[start] > arr[end] and arr[mid] < target):
        return __recursive_agnostic_binary_search(arr, target, start, mid - 1) 
    elif (arr[start] < arr[end] and arr[mid] < target) or (arr[start] > arr[end] and arr[mid] > target):
        return __recursive_agnostic_binary_search(arr, target, mid + 1, end)

