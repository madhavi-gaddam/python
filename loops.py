#Loops repeat a block of code multiple times
for i in range(1, 6):
    print(i)
##################
for i in range(2, 11, 2):
    print(i)
###################
numbers = [10, 20, 30]

for n in numbers:
    print(n)

##################################################
#WHILE LOOP
#Runs until condition becomes False

i = 1

while i <= 5:
    print(i)
    i += 1
#BREAK STATEMENT
#STOPS LOOP IMMEDIEATELY
for i in range(1, 10):
    if i == 5:
        break
    print(i)


#continue Statement

#Skips current iteration

for i in range(1, 6):
    if i == 3:
        continue
    print(i)












