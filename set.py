# sami = {'sami',19,'degree',True,'degree'}
# print(sami)
# list1 = list(sami)
# print(list1)
# if 193 in list1:
#   print('found')
# else:
#   print("nhi milla")
# ##########33
# #   MMMMETHODS
# sami1 = sami.copy()
# sami1.pop()
# print(sami1)
# print("-----------------------")
# sami.difference(sami1)
# print(sami)
# sami.clear()
# print(sami)



s = {1,2,5,6}
s1 = {5,2,7,9}


s8 = s.pop()
print(s8)

s7 = s.symmetric_difference(s1)
print(s7)

s1.symmetric_difference_update(s)
print(f"here is {s1}")



s.intersection_update(s1)
print(s)
s.add(22)
s5 = s.intersection(s1)
print(s5)
print(s)
print(s.union(s1))
print(s.issuperset(s1))
print(s1.issubset(s))
s.discard(5)
print(s)
s.add(5)
print(s)
print("--------------------")
print(s.issuperset(s1))
s2 = s.copy()
s3 = s1.copy()
# s2.add(5,2,6)
# s3.add(1,2,5,6)
print(s2)
print(s3)
print(s2.issubset(s3))

s.update(s1)
print(s)



