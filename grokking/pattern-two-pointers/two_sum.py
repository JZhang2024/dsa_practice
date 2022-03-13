'''
Problem Statement 
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
'''
def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while (left != right):
        value = arr[left] + arr[right]
        
        if (value == target):
            return [left, right]
        elif (value > target):
            right -= 1
        else:
            left += 1
    return 0

if __name__ == '__main__':
    arr_a = [1, 2, 3, 4, 6]
    target_a = 6
    output_a = [1, 3]
    assert(two_sum(arr_a, target_a) == output_a)

    arr_b = [2, 5, 9, 11]
    target_b = 11
    output_b = [0, 2]
    assert(two_sum(arr_b, target_b) == output_b)

    print("All Test Cases Pass")