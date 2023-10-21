"""
Longest Substring
You are tasked with developing a function that finds the length of the longest substring without repeating characters in a given string s. Consider different scenarios involving various characters in the input string.
Scenario: String with No Repeating Characters

Input: "abcdef"
Expected Output: 6
Explanation: In this scenario, the input string contains no repeating characters, so the entire string itself is the longest substring without repeating characters.
Scenario: String with Repeating Characters

Input: "abccba"
Expected Output: 3
Explanation: In this case, the longest substring without repeating characters is "abc" with a length of 3. The characters 'c' and 'b' are repeated, so the substring ends at the first occurrence of the repeated character

Exercise-1
Input :
pqrsstu
Output :
4
Exercise-2
Input:
abbedfgi
Output:
6

"""
import sys
def lengthstring(s):
    start = 0
    max_length = 0
    char_index = {}
    
    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length
    
if __name__ == "__main__":
    user_input = input()
    result = lengthstring(user_input)
    print(result)
