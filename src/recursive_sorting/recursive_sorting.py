# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    res = []
    # TO-DO
    i, j = 0, 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            res.append[arrA[i]]
            i += 1
        else:
            res.append(arrB[j])
            j += 1
    while i < len(arrA):
        res.append(arrA[i])
        i += 1
    while j < len(arrB):
        res.append(arrA[j])
        j += 1
    return res



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    arr_len = len(arr)

    if arr_len < 2:
        return [:] # return a new list
    else:
        mid = arr_len // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
