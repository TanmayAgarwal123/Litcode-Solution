"""
Close the brackets
You are given a set of strings, each consisting of brackets (, ), {, }, [, or ]. A bracket is considered an opening bracket if it is one of (, {, or [, and it is considered a closing bracket if it is one of ), }, or ].
A string of brackets is considered balanced if it meets the following conditions:
It contains no unmatched brackets.
For every opening bracket, there is a corresponding closing bracket of the same type, and the brackets are properly nested.
Your task is to determine, for each given string, whether it is balanced or not. If a string is balanced, output "YES"; otherwise, output "NO".
Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
Exercise-1
input:
{[()]},{[(])},{{[[(())]]}}
Output:
YES
NO
YES
Exercise-2
input:
[],{},(),[}
Output:
YES
YES
YES
NO
"""

def is_balanced(brackets):
    
    matching_brackets = {')': '(', '}': '{', ']': '['}
    stack = []

    for bracket in brackets:
        if bracket in matching_brackets:
            if not stack or stack[-1] != matching_brackets[bracket]:
                return "NO"
            stack.pop()
        else:
            stack.append(bracket)
    
    return "YES" if not stack else "NO"


def process_input(input_str):

    brackets_sets = input_str.split(',')
    results = [is_balanced(brackets) for brackets in brackets_sets]
    return results

def process_input_and_format(input_str):
    brackets_sets = input_str.split(',')
    results = [is_balanced(brackets) for brackets in brackets_sets]
    formatted_results = '\n'.join(results)
    return formatted_results

if __name__=="__main__":
    print(process_input_and_format(input()))
