# calculator.py

# This function adds two numbers
def add(x, y):
  return x + y

# This function subtracts two numbers
def subtract(x, y):
  return x - y

# This function multiplies two numbers
def multiply(x, y):
  return x * y

#This function divides two numbers
def divide(x, y):
  if y == 0:
    return "Error! Division by zero not possible"
  return x / y

def main():
    # Main function to run the calculator CLI
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

        elif choice == '5':
            print("Exiting Calculator. Goodbye!")
            break
        else:
            print("Invalid Input. Please enter a valid choice.")

if __name__ == "__main__":
    main()
