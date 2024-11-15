# MAP
def cube(x):
    return x*x*x
print (cube(2))
print("--------------------------")
listt = [2,3,2,4,3,5,6,7,2]
litrt =list( map(cube,listt))
print(litrt)
print("--------------------------")


# FILTER

def filterr(a):
    return a>2
newnewl = list(filter(filterr , listt))
nene = list(map(cube , newnewl))
print(newnewl)
print("--------------------------")
print(nene)


# reduce

from functools import reduce

lisst = [2,1,3,2,5,3,6]
def multiply(x,y):
    return x*y
multi = reduce(multiply , lisst )
print (multi)