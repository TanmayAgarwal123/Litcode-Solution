"""
Build a wall with lego blocks
How many different ways can you build a wall of height 'n' and width 'm' using an infinite number of Lego bricks of four types, each with different dimensions (depth x height x width)? The types of Lego bricks available are:
Depth: 1, Height: 1, Width: 1
Depth: 1, Height: 1, Width: 2
Depth: 1, Height: 1, Width: 3
Depth: 1, Height: 1, Width: 4
The wall should satisfy the following conditions:
1.	There should be no holes in the wall.
2.	The wall should be a single solid structure without a straight vertical break across all rows of bricks.
3.	The bricks must be laid horizontally.
Provide the number of ways to build the wall, considering that the result should be output modulo 1000000007.
Example:
For n = 2 and m = 2, the output should be legoWall(n, m) = 3.
For n = 3 and m = 2, the output should be legoWall(n, m) = 7.
For n = 2 and m = 3, the output should be legoWall(n, m) = 9.
Input/Output:
1.The input consists of two integers: n and m, representing the desired height and width of the wall, respectively.
2.The output is a long integer representing the number of ways to build the wall, modulo 1000000007.
Exercise-1
Input:
2
2
Here
First row - n value
Second row - m value
Output:
3
Exercise-2
Input:
4
4
Output:
3375
"""
import sys

def legoBlocks(n, m):
    MOD = (10**9 +7)
    row_combinations = [1, 1, 2, 4]
    
    while len(row_combinations) <= m: 
        row_combinations.append(sum(row_combinations[-4:]) % MOD)

    total = [pow(c, n, MOD) for c in row_combinations]
    unstable = [0, 0]
    
    for i in range(2, m + 1):
        f = lambda j: (total[j] - unstable[j]) * total[i - j]
        result = sum(map(f, range(1, i)))
        unstable.append(result % MOD)
    return (total[m] - unstable[m]) % MOD
    
if __name__=="__main__":
    n=int(input())
    m=int(input())
    print(legoBlocks(n,m))
