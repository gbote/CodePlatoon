array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

def linear_search(value_to_find, array_to_search_through): 
    for number in range(len(array_to_search_through)):
        if array_to_search_through[number] == value_to_find:
            return(number)
    return(None) 

def global_linear_search(value, array_to_search):
    output_array = []
    for number in range(len(array_to_search)):
        if array_to_search[number] == value:
            output_array.append(number)
    print(output_array)