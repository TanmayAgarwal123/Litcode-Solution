"""
Sliding Subarray Beauty:
You are given an array of integers arr and an integer k. Your task is to find the given n th position of the smallest integer in each contiguous subarray of size k and print these smallest integers.
A subarray is a contiguous non-empty sequence of elements within the original array.
For each subarray of size k, you need to find the given n th position of the smallest integer within that subarray.
The given n th position of the smallest integer in a subarray is the integer that appears at the given n th position when the subarray is sorted in ascending order.
.
Your task is to return an integer array containing n - k + 1 elements, denoting the beauty of the subarrays in order from the first index in the array.
Exercise-1
Input: 
1 2 3 4 5 6 7 8 9 10
3
2
Note: 
Line 1: input array
Line 2: sub array length
Line 3: position of the smallest value

Output:
2 3 4 5 6 7 8 9
Exercise-2
Input:
1 2 3 4 5 6 7 8 9 10
4
2

Output:
2 3 4 5 6 7 8
"""


def nth_smallest_in_subarrays(arr, k, n):
    nth_smallest_numbers = []
    for i in range(len(arr) - k + 1):
        subarray = arr[i:i + k]
        subarray.sort()
        nth_smallest_numbers.append(subarray[n - 1])
    return nth_smallest_numbers

if __name__=="__main__":
    a=list(map(int,input().split()))
    b=int(input())
    c=int(input())
    print(*nth_smallest_in_subarrays(a,b,c))

