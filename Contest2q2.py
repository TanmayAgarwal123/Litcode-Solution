"""
Largest Palindrome
A palindrome is a string that reads the same from left to right and right to left, like 'civic' or '1001'. You are given a string representing an integer and a maximum number of changes you can make. Your goal is to modify the string, one digit at a time, to create the highest possible integer while adhering to the constraint on the number of changes. The length of the string must remain unchanged, and you must consider the position of zeros to the left of all higher digits. For example, '1001' is a valid representation, while '0011' is not.
Example:
Input:
3
12321
Step 1:
Index 0 and 4 are equal.
Index 1 and 3 are equal.
Index 2 is in the middle.
Total changes allowed: 3
Mismatches count: 0
Since total changes - 2 >= mismatches count, we replace index 0 and 4 with the maximum value of 9. Two changes are completed, and one remaining change is available.
The output is 92329.
Step 2:
Now we can go to index 1 and 3.
Total changes - 2 >= mismatches count is not satisfied because the remaining changes available is 1. So, we need to find the maximum value at index 1 and 3. Here, both are equal.
The output is 92329.
Step 3:
Index 2 is in the middle, so we can do one change. Here, one change is available, so we replace it with 9. (Note: If no change is available, we need to retain the same value.)
The output is 92929.
Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
Exercise 1:
Input:
1
12321

Note:
The first input is an integer representing the maximum number of changes allowed.
The second input is a string representation of an integer.

Output:
12921
Exercise 2:
Input:
3
1231

Output:
9339
"""

from math import floor

def largest_palindrome(k, num):
    n = len(num)
    num = list(num.strip())
    unpaired = len(list(filter(lambda x: x[0] != x[1], zip(num[:int(floor(n / 2))], reversed(num)))))

    if unpaired > k:
        return -1

    for i in range(int(floor(n / 2))):
        if unpaired < k and k >= 2:
            if num[i] != num[n - 1 - i]:
                unpaired -= 1
            if num[i] != '9':
                k -= 1
            if num[n - 1 - i] != '9':
                k -= 1
            num[i] = num[n - 1 - i] = '9'
            continue
        if num[i] == num[n - 1 - i]:
            continue
        k -= 1
        if k < 0:
            break
        num[i] = max(num[i], num[n - 1 - i])
        num[n - 1 - i] = num[i]

    if k > 0 and n % 2 == 1:
        num[int(floor(n / 2))] = '9'

    return -1 if k < 0 else ''.join(num)
    
if __name__ == "__main__":
    a=int(input())
    b=input()
    print(largest_palindrome(a,b))
