#1.1 Is Unique
#implement an algorithm to see if a string has all unique characters
#what if you cannot use additional data structures

class mySolution:
    def is_unique(str):         
        char_set = set() #initialize an empty set
        
        for i in str:       #iterate over the chars in the string
            if i in char_set:       #check if the character already exists in the set
                return False        #if it does, string does not have unique chars
            else:
                char_set.add(i)     #if it doesn't, add character to set
        return True                 
#after iterating over the entire string, if no duplicate has been found, it is a unique string
#runtime: O(n), n = length of string
#space complexity: O(n), n = length of string; because worse case will have all characters of string in set
if __name__ == '__main__':
    str_a = "abcdedf"
    assert mySolution.is_unique(str_a) == False
    str_b = "abcdef"
    assert mySolution.is_unique(str_b) == True
    str_c = "123141"
    assert mySolution.is_unique(str_c) == False
    str_d = "12345"
    assert mySolution.is_unique(str_d) == True
    print("All tests pass")