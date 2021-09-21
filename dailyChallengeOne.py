import sys

myList = []
print("Enter numbers to append in a list\nTo stop appending the list, ENTER 99")
print("_________________________________")
enteredNumber = int(input("Enter a number: "))

if enteredNumber == 99:
    print("You stopped the program!")
    sys.exit()

while enteredNumber != 99:
    myList.append(enteredNumber)
    enteredNumber = int(input("Enter another number: "))

k = int(input("Enter k: "))
print("_________________________")
print("Your list : ",myList)
print("-------------------------")
print("Numbers that equals k are")
for i in myList:
    for j in myList:
        if k == i + j:
            print(i," and ",j," = k : true")
