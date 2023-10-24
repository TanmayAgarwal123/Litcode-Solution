"""
Mix the array
Given a 1-indexed array initially filled with zeros and a list of operations, perform each operation by adding a value to each element of the array between two given indices (inclusive). After performing all operations, find and return the maximum value in the array.
For example, let's consider the following scenario:
q = {[2,4,5],[3,6,3],[1,7,10]}
Initial Array size = 7
Array: [0, 0, 0, 0, 0, 0, 0]
Operations:
Add 5 between indices 2 and 4: [0, 5, 5, 5, 0, 0, 0]
Add 3 between indices 3 and 6: [0, 5, 8, 8, 3, 3, 0]
Add 10 between indices 1 and 7: [10, 15, 18, 18, 13, 13, 10]
In this scenario, the maximum value in the array is 18.
Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
Exercise-1
Input:
5
3
2 4 3
4 5 9
3 3 11
Output:
14
Note:
Line -1 : array size
Line -2 : query count
Exercise-2
Input:
10
3
3 10 3
4 5 9
2 9 11
Output:
23
"""

def max_value_after_operations_input_format():
    n = int(input())
    m = int(input())

    array = [0] * (n + 1)

    for _ in range(m):
        start, end, value = map(int, input().split())
        for i in range(start, end + 1):
            array[i] += value

    return max(array)

max_value = max_value_after_operations_input_format()
print(max_value)
    
