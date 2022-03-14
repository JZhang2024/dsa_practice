'''
Problem Statement 
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.
Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''

#If I were allowed to use space, I could just use a set to filter out duplicate elements
#Without additional space, I need to use two pointers: one to iterate through the length of the array
#and another to point to the index of the next non-duplicate number
#this way, I can maintain the unique elements of the array and keep a count of the new length

def remove_duplicates(arr):
    i = 1   #iterating pointer
    next_non_duplicate = 1    #next non_duplicate element
    #start at index 1 to compare to previous elements

    while (i < len(arr)):
        if (arr[next_non_duplicate - 1] != arr[i]):
            arr[next_non_duplicate] = arr[i]  #if the element is not a duplicate of the last non-duplicate element, add to new_arr
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate


#Time Complexity: O(n), iterating across array of n elements
#Space Complexity: O(1), modifying array in-place, so no additional space used




if __name__ == '__main__':
    assert(remove_duplicates([2, 3, 3, 3, 6, 9, 9]) == 4)
    assert(remove_duplicates([2, 2, 2, 11]) == 2)
    print("All Test Cases Pass")
