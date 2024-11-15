#print("hello world")
#print(5)
#print(17*13)
#print("my name is samiullah baig\nI\tam 19.5 year old ")
# x1 = 5.332
# print(x1)
# name= "samiullah baig"
# print(type(name))
# true=1==1
# print(true)

# [(x,y) for x in [1,2,3] for y in [1,5,2] 
#  if x  !=  y
#    print(x,y)
#  ]


# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y or x==y :
#             combs.append((x, y))

# print(combs)
# liset = []
# lists = [1,2,3,4],[5,6,7]
# for num in lists:
#     for lis in num :
#          print(lis)
#          liset.append(lis)
# print(liset)
# liset = []
# lists = [1,2,3,4],[5,6,7]
# lissss = [lis for num in lists for lis in num ]
# print(lissss)
        

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# rrrr = [[row[i] for row in matrix] for i in range(4)]
# print(rrrr)



# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# rrrrrr=[]
# for i in range(4):
#     rows= []
#     for row in matrix:
#         rows.append(row[i])
#     rrrrrr.append(rows)   
# print(rrrrrr)






# roll_no= [13,50,51,52,53,15]
# names = ["bilal" , "roshan" , "samavia" , "sami"  , "sana" , "dawood"]
# for r, n in zip(roll_no,names):
#   print(f"what is your name : my name is {n} ", f"what is is your roll no : it is {r}")