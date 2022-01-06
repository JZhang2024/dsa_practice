#1.2 checkPermutation
#Given two strings, write a method to determine if one string is a permutation of the other

class Solution:

    #sort strings, then check equality
    def check_permutation(str1, str2):
        if len(str1) != len(str2):
            return False
        sorted_a = sorted(str1)
        sorted_b = sorted(str2)
        if sorted_a == sorted_b:
            return True
        else:
            return False

#runtime: O(nlogn)
#space complexity: O(1): only storing the 2 sorted strings

if __name__ == '__main__':
    str_a = "abcdef"
    str_b = "dbacfe"
    assert Solution.check_permutation(str_a, str_b) == True
    str_c = "abcdefg"
    str_d = "abcdef"
    assert Solution.check_permutation(str_c, str_d) == False
    str_e = "rwgqgrg"
    str_f = "1234567"
    assert Solution.check_permutation(str_e, str_f) == False
    print("All tests pass")


