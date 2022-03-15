'''
Problem Statement 
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
'''

#two pointers: from opposite ends of the sorted arr to account for negative numbers. They converge towards the middle.
#And then another to point towards an index in the output arr

def make_squares(arr):
    left, right = 0, len(arr) - 1
    result = [0] * len(arr)

    next_highest_square = len(arr) - 1
    #calculate the squares from both ends at each iteration and place the greatest square in relevent
    #index in result arr, while updating pointers.
    while (left != right):

        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if (left_square > right_square):
            result[next_highest_square] = left_square
            left += 1
        else:
            result[next_highest_square] = right_square
            right -= 1
        next_highest_square -= 1
    
    return result


#Time Complexity: O(n) just iterating across length of array from ends to middle
#Space Complexity: O(n) creating new output array with same length as input array

if __name__ == '__main__':
    
    assert(make_squares([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9])
    assert(make_squares([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9])
    print("All Test Cases Pass")




    
    
    
    