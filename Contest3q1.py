"""
 Merge two sorted linked lists
Suppose we have two sorted linked lists, represented by the pointers headA and headB. Our task is to merge these two lists into a single sorted linked list. It's possible for either headX or headY to be null, indicating that the corresponding list is empty.
For example, consider the following linked lists: 
headX refers to 2 -> 4 -> 6 -> 8 -> NULL
headY refers to 1 -> 3 -> 5 -> NULL
We need to merge these two lists into a new list, where the elements are sorted in ascending order. After merging, the resulting linked list would be:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 8 -> NULL
Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
Exercise-1
input:
3
1
3
7
2
1
2
output:
1
1
2
3
7
Here the first value is the count of the first link node, and the fifth value is the count of the second link node.
Exercise-2
input:
3
2
3
4
2
1
7
Output:
1
2
3
4
7


"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(-1)
    current = dummy

    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    if l1 is not None:
        current.next = l1
    else:
        current.next = l2

    return dummy.next

def build_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def linked_list_to_list(head):
    nums = []
    current = head
    while current:
        nums.append(current.val)
        current = current.next
    return nums
    
def read_input_and_process():
    n1 = int(input().strip())
    
    l1_nums = [int(input().strip()) for _ in range(n1)]
    l1 = build_linked_list(l1_nums)
    
    n2 = int(input().strip())
    
    l2_nums = [int(input().strip()) for _ in range(n2)]
    l2 = build_linked_list(l2_nums)
    
    merged_head = merge_two_sorted_lists(l1, l2)
    merged_list = linked_list_to_list(merged_head)
    
    for num in merged_list:
        print(num)

read_input_and_process()
