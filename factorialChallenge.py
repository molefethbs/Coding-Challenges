def firstFactorial(num):

  for i in range(1,num):
    num *= i
  return num

# keep this function call here
print(firstFactorial(int(input())))