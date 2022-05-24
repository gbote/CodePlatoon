def calculate_mode(list):
    counts = {}
    ans = []

    # adding/counting up all values into the dictionary
    for i in list:
        if i in counts:
            counts[i] += 1
        elif i != ' ':
            counts[i] = 1

    # sorting the dictionary into a list
    sort_list = sorted(counts.items(), key=lambda x:x[1], reverse = 1)

    # setting the mode
    mode = sort_list[0][1]
    i = 0

    # adding all keys occuring mode times
    while i < len(sort_list) and sort_list[i][1] == mode:
        ans.append(sort_list[i][0])
        i += 1

    return ans
