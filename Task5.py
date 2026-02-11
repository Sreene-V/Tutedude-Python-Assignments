def fac(num):
    fact = 1
    while num > 1:
        fact *= num
        num -= 1
    return fact

n=int(input("Enter a number :"))

print(f"The factorial of {n} is {fac(n)}")
