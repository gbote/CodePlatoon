from sum_pairs import sum_pairs

# write your specs here!
print(sum_pairs([1,2,3,4,5], 9) == [[4,5]])
print(sum_pairs([1,2,3,4,5], 7) == [[2,5], [3,4]])
print(sum_pairs([3,1,5,8,2], 27) == 'unable to find pairs')
print(sum_pairs([10,20,30,40,50], 90) == [[40,50]])
print(sum_pairs([1,2,3,4,5], 1) == 'unable to find pairs')
