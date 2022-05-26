# from msilib import sequence


def bubble_sort(list):
    swaps = 0
    n = len(list)
    iteration_count = 0
    for _ in range(n):
        swapped = False
        for index in range(1, len(list)):
            iteration_count += 1
            if list[index] < list[index - 1]:
                list[index - 1], list[index] = list[index], list[index - 1]
                swaps += 1
                swapped = True
        if not swapped:
            break


    print(f"Swaps: {swaps}")
    print(f"Iterations: {iteration_count}")
    return list

sequence = [4, 3, 5, 0, 1, 6]
print(f"Final Result: {bubble_sort(sequence)}")