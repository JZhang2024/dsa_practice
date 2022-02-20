'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.
Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''
def longest_substring_with_k_distinct(str, k):
    max_len = 0
    window_start = 0
    char_dict = dict()

    for window_end in range(len(str)):
        if str[window_end] not in char_dict:
            char_dict[str[window_end]] = 1
        else:
            char_dict[str[window_end]] += 1
        
        while len(char_dict) > k:
            if char_dict[str[window_start]] == 1:
                char_dict.pop(str[window_start])
            else:
                char_dict[str[window_start]] -= 1
            window_start += 1
            
        if len(char_dict) == k:
            max_len = max(max_len, sum(char_dict.values()))
    return max_len

        


if __name__ == '__main__':
    test_A = ("araaci", 2)
    test_B = ("araaci", 1)
    test_C = ("cbbebi", 3)

    
    assert(longest_substring_with_k_distinct(test_A[0], test_A[1]) == 4)
    assert(longest_substring_with_k_distinct(test_B[0], test_B[1]) == 2)
    assert(longest_substring_with_k_distinct(test_C[0], test_C[1]) == 5)
    print("All Test Cases Pass")


