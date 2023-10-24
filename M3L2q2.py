"""
Check string prefix
You are given a list of passwords, where each password consists of lowercase letters from 'a' to 'z' inclusive. The set of passwords is said to be a 'GOOD PASSWORD' if no password is a prefix of another password in the set, except for identical passwords (which are considered prefixes of each other). In this case, print 'GOOD PASSWORD'. Otherwise, print 'BAD PASSWORD' on the first line, followed by the first pair of passwords where one password is a prefix of the other.
Consider the following list of words: ['apple', 'banana', 'application', 'bananas'].
In this case, the word 'banana' is a prefix of 'bananas'.
So we would print: 'BAD PASSWORD'
Now let's take another example with a different set of words: ['cat', 'dog', 'elephant']. In this scenario, none of the strings are prefixes of each other.
Therefore, we can conclude that: GOOD PASSWORD
Exercise-1
Input:
abc zxy pqr

Output:
GOOD PASSWORD
Exercise-2
Input:
abc abczxy abcpqr

Output:
BAD PASSWORD
"""

def check_passwords(passwords):
    password_list = passwords.split()
    for i in range(len(password_list)):
        for j in range(len(password_list)):
            if i == j or len(password_list[i]) > len(password_list[j]):
                continue
            if password_list[j].startswith(password_list[i]):
                return "BAD PASSWORD"
    return "GOOD PASSWORD"

if __name__ == "__main__":
    a=input()
    print(check_passwords(a))
