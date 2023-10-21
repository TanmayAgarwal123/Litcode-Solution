"""
Create a text editor using commands
You are developing a text editor that allows users to perform various operations on the text using the "CustomStack" class. The class supports the following operations:
1.	insert(value): Inserts a string of characters at the current cursor position in the text.
2.	delete(value): Deletes the last value characters from the text starting from the current cursor position.
3.	get(value): Retrieves the character at index value from the text and displays it.
4.	undo(): Reverts the last executed 
5.	command on the text.
Each command is represented by a string in the following format:
1.Command 1: '1 value' - Inserts the string value at the current cursor position in the text.
2.Command 2: '2 value' - Deletes the last value characters from the text starting from the current cursor position.
3.Command 3: '3 value' - Retrieves the character at index value from the text and displays it.
4.Command 4: '4' - Reverts the last executed command on the text.
Consider a scenario where you have a text editor with a "CustomStack" class that implements the required operations. Assume the initial text is empty.
Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

Exercise-1
input:
1 abc,3 3,2 2,3 1
Here
1 abc -> command and input text
3 3 -> command and index of the stack
Output:
c
a

Exercise-2
Input:
1 zxy,3 3,2 2,1 def,3 2
Output:
y
d


"""

import sys
class CustomStack:
    def __init__(self):
        self.text = ""  
        self.stack = [] 

    def insert(self, value):
        self.text += value
        self.stack.append(self.text)

    def delete(self, value):
        if value > len(self.text):
            self.text = ""
        else:
            self.text = self.text[:-value]
        self.stack.append(self.text)

    def get(self, value):
        if 1 <= value <= len(self.text):
            character = self.text[value - 1]
            print(character)

    def undo(self):
        # Revert the last executed command on the text.
        if self.stack:
            self.stack.pop()
            if self.stack:
                self.text = self.stack[-1]
            else:
                self.text = ""


def process_commands():
    custom_stack = CustomStack()
    user_input = input()
    commands = user_input.split(',')
    for command in commands:
        cmd, *args = command.split()
        if cmd == '1':
            custom_stack.insert(args[0])
        elif cmd == '2':
            custom_stack.delete(int(args[0]))
        elif cmd == '3':
            custom_stack.get(int(args[0]))
        elif cmd == '4':
            custom_stack.undo()

process_commands()
