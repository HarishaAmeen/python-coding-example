# Problem statement: Given an array of integers and a value,
# determine if there are any three integers in the array whose sum equals the given value.
# If does not exist, return False

# Example - 
# Arraay - [1, 10, 5, 20, 15, 30, 25]
# target sum - 30
# Answer - 10, 15, 5


def find_triplet(array, target):
    array.sort()
    # sort array
    l = len(array)
    left = 0
    right = l-1
    while left < right:
        sum = array[left] + array[right]
        third = target - sum
        if third != array[left] and third != array[right] and third in array:
            return array[left], array[right], third
        elif sum >= target:
            right -= 1
        else:
            left += 1
    return False

  
numbers = [1, 10, 15, 25, 12, 24, 6, 8, 50, 20, 30, 5, 6, 11, 13, 17, 19, 21, 31, 33, 34, 38, 44, 42,99]
target = 52
print(find_triplet(numbers, target))

numbers = [1, 5, 3, 2, 9, 7, 6, 8]
target = 10
print(find_triplet(numbers, target))
