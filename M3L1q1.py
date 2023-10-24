"""
Maximize Subsequences in String
You are given two strings, text and pattern, both consisting of only lowercase English letters. The objective is to modify the text by adding either pattern[0] or pattern[1] exactly once at any position. After the modification, you need to determine the maximum number of times the pattern can occur as a subsequence in the modified text.
A subsequence is a sequence of characters obtained by deleting some or no characters from the original sequence without changing the order of the remaining characters.
Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
Example
INPUT
abdcdbc
ac
OUTPUT
4
Exercise-1
Input :
ababc
ab
Output :
5
Exercise-2
Input:
ababab
ab
Output:
9

"""

def count_subsequences(text, pattern):
    dp = [[0] * (len(pattern) + 1) for _ in range(len(text) + 1)]

    for i in range(len(text) + 1):
        dp[i][0] = 1

    for i in range(1, len(text) + 1):
        for j in range(1, len(pattern) + 1):
            if text[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


def maximize_subsequences(text, pattern):
    max_count = 0
    for i in range(len(text) + 1):
        for char in pattern:
            new_text = text[:i] + char + text[i:]
            count = count_subsequences(new_text, pattern)
            max_count = max(max_count, count)

    return max_count

if __name__ == "__main__":
    a=input()
    b=input()
    print(maximize_subsequences(a,b))
