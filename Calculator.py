import math
class Calculator:
    # Function to add two numbers
    def add(self,num1, num2):
        return num1 + num2

# Function to subtract two numbers
    def subtract(self,num1, num2):
        return num1 - num2

# Function to multiply two numbers
    def multiply(self,num1, num2):
        return num1 * num2

# Function to divide two numbers
    def divide(self,num1, num2):
        return num1 / num2

# Function to square a number
    def square(self,num1):
        return num1 * num1

# Function to find square root using math function
    def squareroot(self,num1):
        return math.sqrt(num1)


if __name__ == "__main__":
 # Getting the two numbers from the user    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    

    c = Calculator()

    select = 1
    while select !=0:
        print("Please select operation -\n" 
        "1. Add\n" 
        "2. Subtract\n" 
        "3. Multiply\n"  "4. Divide\n" "5. Square\n" "6. Squareroot\n")
    
   
    # Take input from the user
        select = input("Select operations form 1, 2, 3, 4 , 5 ,6 :")

     
        if select == '1':
            print(c.add(num1,num2))

        elif select == '2':
            print(c.subtract(num1,num2))

        elif select == '3':
            print(c.multiply(num1,num2))

        elif select == '4':
            print(c.divide(num1,num2))

        elif select == '5':
            print(c.square(num1))
    
        elif select =='6' :
            print(c.squareroot(num1))
    
        else:
            print("Invalid input")