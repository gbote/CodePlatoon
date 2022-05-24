#REMEMBER TO PSEUDOCODE
def pad(array, min_size, value = None):
    if min_size > len(array):
        for _ in range(array[-1], min_size):
            array.append(value)
    return array