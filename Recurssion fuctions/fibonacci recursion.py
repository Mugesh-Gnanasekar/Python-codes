def Fibonacci(first_value,second_value,n):
    if n==1:
        return first_value
    elif n==2:
        return second_value
    else:
        return Fibonacci(first_value,second_value,n-1)+Fibonacci(first_value,second_value,n-2)



first_value=input("Enter the first value:  ")
second_value=input("Enter the second value:  ")
index= input("Enter the position of the Fibonacci series you want:  ")

answer=Fibonacci(first_value,second_value,index)
print answer