dic1 = {1 : "abdul basit"  , 2 : "abdul rafay",52 :"samiullah baig" , 13 : "bilal ahmed" , 14 : "danish rasool" , 15 : "Dawood danish"}
dic2 =  {30 : "mughees saleem" , 53 :"sana" , 50 : "Rooshan sheikh" , 51 : "samavia najam"}
dic1.update(dic2)
print(dic1)
print(len(dic1))
print("------------------")
dic1.pop(1)
print(dic1)
print(len(dic1))
print("------------------")
dic1.popitem()
print(dic1)
print(len(dic1))
print("------------------")

del dic1[53]
print(dic1)
print(len(dic1))




