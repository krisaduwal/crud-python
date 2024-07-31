print("my calculator!")
# class Calculator:
#     def __init__(self, n1, n2):
#         self.n1 = n1
#         self.n2 = n2
    
#     def 

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print("operations: ")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("enter choice: ")

    if choice in ('1', '2', '3', '4'):
        try:
            n1 = int(input("enter first number"))
            n2 = int(input("enter second number"))
        except ValueError:
            print("invalid input, enter a number")

        if choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))
        elif choice == '2':
            print(n1, "-", n2, "=", substract(n1, n2))
        elif choice == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))
        elif choice == '4':
            print(n1, "/", n2, "=", divide(n1, n2))
    else:
            print("enter a valid input")
    