# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    while arrA and arrB:
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB.pop(0))
        else:
            merged_arr.append(arrA.pop(0))

    merged_arr = merged_arr + arrA + arrB

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    if len(arr) < 2:
        return arr

    mid = int( (len(arr) - 1) / 2 ) + 1
    arrA = arr[:mid]
    arrB = arr[mid:]

    if len(arrA) > 1:
        arrA = merge_sort(arrA)
    if len(arrB) > 1:
        arrB = merge_sort(arrB)

    return merge(arrA, arrB)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

