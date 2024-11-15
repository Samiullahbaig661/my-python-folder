# def dou(x):
#   return  x*2
# print(dou(3))

def appl (fx,value):
    return 34 + fx(value)
# double = lambda x : x*2
# print(double(10))

cub = lambda x : x*x*x
def cube(x):
    return x*x*x


# avg = lambda f,g : (f+g)/2
# print(avg(3,5))

# avg = lambda f,g,k : (f+g-k)
# print(avg(3,5,7))


print(appl(cub , 2 ))
print(appl( cube , 2 ))
