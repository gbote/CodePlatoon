# take in an integer arrray and a desired sum
# output an array of pairs that equal the desired sum

# sum_pairs([1,2,3,4,5], 7) # [[2,5], [3,4]]
# sum_pairs([3, 1, 5, 8, 2], 27) # 'unable to find pairs'

def sum_pairs(arr, num):

# initialize an empty array to capture the answer array
    answer_array = []

# add each number to every other number in the array
    for i in range(0, len(arr)-1):
        for j in range(i + 1, len(arr)):
            summed_pair = (arr[i] + arr[j])
            # check summed pair for a match with the given sum
            if summed_pair == num:
                # if summed pair matches the sum push the summed pair to the answer array
                answer_array.append([arr[i], arr[j]])
    if answer_array == []:
        return('unable to find pairs')
    return(answer_array)