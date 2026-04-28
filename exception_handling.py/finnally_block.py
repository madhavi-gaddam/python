#finally runs always (error or not)
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")
###################################
# Q: Show message "Done" no matter what happens

try:
    num = int(input("Enter number: "))
    print(10 / num)
except:
    print("Error occurred")
finally:
    print("Done")












