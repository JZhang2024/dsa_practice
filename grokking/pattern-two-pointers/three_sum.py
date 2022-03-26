'''
Problem Statement 
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
'''

#fix in place one element at a time, iterating across the list of elements
#while performing two-sum at each iteration with the target sum of the pairs being the negative of the element

def three_sum(arr):
    
    arr.sort()  #sort first to make it easier to avoid repeats and to be able to do the two-pointer solution for two_sum
    output = []
    #iterate across each element of arr and fix each as left pointer
    for i in range(len(arr)):
        #make sure no repeated elements
        if ((i > 0) and (arr[i] == arr[i - 1])):
            continue
        two_sum(arr, -arr[i], i+1, output)  #left pt starts one index ahead because i is reserved for target
    return output

#can have separate two_sum function to make code cleaner
def two_sum(arr, target, left, output_arr):
    #right pointer will always start as the last element in the arr
    right = len(arr) - 1

    while (left < right):
        current_sum = arr[left] + arr[right]
        
        if (current_sum == target): #if triplets = 0
            output_arr.append([-target, arr[left], arr[right]]) #adds triplet to output arr
            left += 1
            right -= 1
            #avoid duplicate elements by skipping whenever a pointer finds a consecutive value
            while (left < right) and (arr[left] == arr[left - 1]):
                left += 1
            while (left < right) and (arr[right] == arr[right + 1]):
                right -= 1
        elif (current_sum > target):
            right -= 1
        else:
            left += 1
    return

#space complexity: other than output arr which is the length of unique triplets, O(n) space needed for sorting
#time complexity: sorting - O(logn)
#                 two_sum() - O(n)
#                 #outer iteration - O(n)
#Overall: O(n^2 + nlogn) -> O(n^2)

if __name__ == '__main__':
    
    test_A = [-3, 0, 1, 2, -1, 1, -2]
    test_B = [-5, 2, -1, -2, 3]

    assert(three_sum(test_A) == [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]])
    assert(three_sum(test_B) == [[-5, 2, 3], [-2, -1, 3]])
    print("All Test Cases Pass")