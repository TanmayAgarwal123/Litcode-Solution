"""
Sum of Numbers With Units Digit K
You are given two integers, num and k. You need to find the minimum possible size of a set of positive integers with the following properties:
1.	Each integer in the set has the unit digit equal to k.
2.	The sum of all the integers in the set equals num.
If such a set exists, return its minimum size. Otherwise, if no set satisfies the conditions, return -1.
Note:
The set can contain multiple instances of the same integer, and if the set is empty, its sum is considered to be 0.
The unit digit of a number refers to its rightmost digit.
Consider the input:
num = 58
k = 9
The function should return 2 because there exists a valid set with two positive integers, both having the units digit 9, and their sum is equal to 58.
Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
Exercise-1
Input :
56
9
Output :
4
Exercise-2
Input:
53
Output:
-1
"""
import sys
def min_set_size(num, k):
    # If k is greater than num, no solution exists
    if k > num:
        return -1

    # If k is 0, then either 1 or no solution
    if k == 0:
        return 1 if num == 0 else -1

    # Check if forming a set is impossible based on the new observation
    if num % 10 < k and num // 10 < k - num % 10:
        return -1

    # Calculate the minimum set size
    set_size = 0
    while num > 0:
        # Subtract the largest possible number with unit digit k
        subtract_value = (num - k) // 10 * 10 + k
        num -= subtract_value
        set_size += 1

    return set_size

if __name__ == "__main__":
    try:
        num = int(input())
        k = int(input())
        result = min_set_size(num, k)
        print(result)
    except:
        print(-1)
