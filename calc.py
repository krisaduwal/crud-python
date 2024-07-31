print("operations: ")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

class Calculator():
    def __init__(self, n1, n2):
        self.n1=n1
        self.n2=n2

    def add(self):
        return n1 + n2

    def substract(self):
        return n1 - n2

    def multiply(self):
        return n1 * n2

    def divide(self):
        return n1 / n2
    

# n1 = int(input("enter first number: "))
# n2 = int(input("enter second number: "))

while True:
    choice = input("enter choice: ")

    if choice in ('1', '2', '3', '4'):
        try:
            n1 = int(input("enter first number: "))
            n2 = int(input("enter second number: "))
            cal = Calculator(n1, n2)

        except ValueError:
            print("invalid input, enter a number")

        if choice == '1':
            print("sum: ", cal.add())
        elif choice == '2':
            print("differene: ", cal.substract())
        elif choice == '3':
            print("product: ", cal.multiply())
        elif choice == '4':
            print("result: ", cal.divide())
    else:
            print("enter a valid input")
    