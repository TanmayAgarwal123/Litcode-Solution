"""
Queue
Write a program to implement a custom queue using two stacks. The queue should support the following three types of queries:
Enqueue: This query type is denoted by "1 x", where x is an element to be enqueued. It means that you need to insert element x at the end of the queue.
Dequeue: This query type is denoted by "2". It indicates that you should remove the element at the front of the queue.
Print Front: This query type is denoted by "3". It instructs you to print the element at the front of the queue without removing it.
Exercise-1
input:
1 42,2,1 14,3
output:
14
Exercise-2
input:
1 23,2,1 14,3,2,1 78,3
Output:
14
78
"""
class CustomQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            self.stack2.pop()

    def print_front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            print(self.stack2[-1])

# Example usage
queries = input().split(',')
queue = CustomQueue()

for query in queries:
    if query[0] == '1':
        _, element = query.split()
        element = int(element)
        queue.enqueue(element)
    elif query == '2':
        queue.dequeue()
    elif query == '3':
        queue.print_front()
