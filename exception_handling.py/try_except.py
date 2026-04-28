#an exception is an error that happens while your program is running.

#try and except
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except:
    print("Something went wrong!")


#Q: Take user input and avoid crash if input is not a number

try:
    num = int(input("Enter number: "))
    print("You entered:", num)
except:
    print("Invalid input!")


#Catching Specific Exceptions
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


#Q: Handle both invalid input and division by zero.
try:
    num = int(input("Enter number: "))
    result = 100 / num
    print(result)
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


