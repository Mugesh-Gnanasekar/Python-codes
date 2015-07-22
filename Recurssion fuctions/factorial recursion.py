def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

num=input("Enter the number you want the Factorial for:  ")
answer=factorial(num)
print answer