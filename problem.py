# Find the factorial of a given number
n = int(input("Enter your number"))
factorial = 1
while(n>0):
    factorial *= n
    n -= 1
print(factorial)