#1.3 URLify
#URLify (Write a method to replace all spaces in a string with '%20').
#You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
#(Note: if implementing in java, please use a character array so that you can perform this operation in place.)

class Solution:
    def urlify(word, true_length):
        word = word[:true_length]   #removes extra spaces at end of meaningful characters with given true length
        return '%20'.join(word.split()) #splits word into array of chars and then joins them back into string separated by '%20' between each element

#runtime: O(1)
#space complexity: O(1)
if __name__ == '__main__':
    str_a = "Mr John Smith"
    length = 13
    output_a = "Mr%20John%20Smith"
    output_b = "Mr%20John%20Smith%20/%20/%20/%20"
    assert Solution.urlify(str_a, length) == output_a
    str_b = "Mr John Smith    "
    assert Solution.urlify(str_b, length) == output_a
    assert (Solution.urlify(str_b, length) == output_b) == False
    print("All tests pass")


    
    
