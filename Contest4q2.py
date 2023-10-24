"""
Is Graph Bipartite?
You have an undirected graph with n nodes, each represented by a number between 0 and n - 1. The graph is described by a 2D array graph, where graph[u] is an array containing nodes adjacent to node u. In other words, there is an undirected edge between node u and each node v present in graph[u]. The graph satisfies the following conditions:
•	There are no self-edges, meaning that node u is not present in graph[u].
•	There are no parallel edges, implying that each node appears only once in the adjacency list.
•	The graph is undirected, so if node v is adjacent to node u, then node u is also adjacent to node v (i.e., an edge between u and v implies an edge between v and u).
•	The graph may not be fully connected, so there can be two nodes u and v such that there is no direct path between them.
•	The task is to determine whether the given graph is bipartite or not. A graph is considered bipartite if its nodes can be partitioned into two independent sets, denoted as set A and set B, such that each edge connects a node from set A to a node from set B.
Example:
Input: [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
Output : false
0 -- 1
| |
3 -- 2
Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
Exercise-1
Input : 
4
1 2 3
0 2
0 1 3
0 2

Output :
false
Exercise-2
Input:
4
1 2 3
0 2
0 1
0

Output:
false
Exercise-3
Input:
4
1 3
0 2
1 3
0 2

Output:
true
"""

from typing import List
from collections import deque

def is_bipartite(graph: List[List[int]]) -> bool:
    n = len(graph)
    color = [0] * n

    for i in range(n):
        if color[i] == 0 and graph[i]:
            color[i] = 1
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
    return True
    
def get_user_input():
    num_nodes = int(input())

    graph = []
    for i in range(num_nodes):
        adj_list = input().split()
        graph.append([int(node) for node in adj_list])

    return graph

def main():
    graph = get_user_input()
    if is_bipartite(graph):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
