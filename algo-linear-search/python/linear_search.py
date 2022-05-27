array_to_search_through = list(range(1, 1001))

def linear_search(value_to_find, array_to_search_through): 
    return next((number for number in range(len(array_to_search_through)) if array_to_search_through[number] == value_to_find), None) 

def global_linear_search(value, array_to_search):
    output_array = [number for number in range(len(array_to_search)) if array_to_search[number] == value]
    print(output_array)