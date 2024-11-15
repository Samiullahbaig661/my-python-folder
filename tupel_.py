# tup = (1,2,3,4,5,6,7,8,9)
# print(tup)
# print(tup[-4])
# tupu = tup[1:-2]
# tupu1 = tup[1:-1:2]
# print(tupu)
# print(tupu1)




###############33




country = ("spain", "pakistan", "india","malysia","honkkong")
number = (1,2,3,4,5)
countryies =  country +number 
print(countryies)

res = countryies.index(3 , 1,8)
print(f' index is {res}')


temp  =  list(country)
temp.append("russia")
temp.pop(3)
temp[0] = "afganistan"
country = tuple(temp)
print(country)

