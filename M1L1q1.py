"""

"""

def do_something(email):
    a = len(email)
    upper = 0
    lower = 0
    digits = 0

    for c in email:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digits += 1

    other = a - upper - lower - digits
    u = (upper / a) * 100
    l = (lower / a) * 100
    d = (digits / a) * 100
    o = (other / a) * 100

    print(f"{u:.3f}%")
    print(f"{l:.3f}%")
    print(f"{d:.3f}%")
    print(f"{o:.3f}%")

if __name__ == "__main__":
    input_val = input()
    do_something(input_val)
