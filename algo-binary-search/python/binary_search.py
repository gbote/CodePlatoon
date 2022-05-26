def binary_search(num, array, start, end):
    sorted_arr = sorted(array)
    if end >= start:
        middle = int(start + end) // 2
        if sorted_arr[middle] == num:
            return middle
        elif num < sorted_arr[middle]:
            return binary_search(num, sorted_arr, start, middle - 1)
        else:
            return binary_search(num, sorted_arr, middle + 1, end)
    else:
        return -1