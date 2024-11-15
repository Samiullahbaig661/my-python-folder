
enter  = int ( input ("Enter a number which you find a factorial : "))
i =1
a= 1
del a
while enter>= i:
    a = a *i 
    i+=1
print (f"The factorial of {enter} is : {a}")

#############33333333333333333333333333333333333333

def factorial(n):
    if n == 0 or n ==1:
        return 1 
    else:
        return n * factorial(n-1)
    

print(factorial(6))    