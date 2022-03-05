'''
Problem Statement 
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you cannot skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.
Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

def fruits_into_baskets(fruits):
    
    window_start = 0
    max_sum = 0
    
    fruit_dic = dict()

    for window_end in range(len(fruits)):
        if fruits[window_end] not in fruit_dic:
            fruit_dic[fruits[window_end]] = 1
        else:
            fruit_dic[fruits[window_end]] += 1
        
        while (len(fruit_dic) > 2):
            if fruit_dic[fruits[window_start]] == 1:
                del fruit_dic[fruits[window_start]]
            else:
                fruit_dic[fruits[window_start]] -= 1
            window_start += 1
        
        if (len(fruit_dic) == 2):
            max_sum = max(max_sum, window_end - window_start + 1)
    return max_sum

if __name__ == '__main__':
    
    fruits_a = ['A', 'B', 'C', 'A', 'C']
    fruits_b = ['A', 'B', 'C', 'B', 'B', 'C']

    assert(fruits_into_baskets(fruits_a) == 3)
    assert(fruits_into_baskets(fruits_b) == 5)
    print("All Test Cases Pass")


