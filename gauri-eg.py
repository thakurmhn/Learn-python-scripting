

def addition():
    a = 4
    b = 6
    return a+b

def teacher():
    name = "Anita"

    return name


def multiply(num1, num2):
    return num1 * num2


def stat():
    return 0









print(f"Book price is {multiply(300, 7)}")




def calculate(num1, num2, operation='add'):
    if operation == 'add':
        print(num1 + num2)
    if operation == 'sub':
        if num1 > num2:
            print(num1 - num2)
        else:
            print(num2 - num1)
    if operation == 'multi':
        print(num1 * num2)

    if operation == 'div':
        print(num1 / num2)

calculate(54, 9, operation='sub')
















































#print(f"my teachers name is {teacher()} and age is {addition() + 30}")



