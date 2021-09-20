def factorial(fact):
    for i in range(1,fact):
        fact = fact * i
    return fact

fact = int(input("Enter number: "))
print(factorial(fact))
