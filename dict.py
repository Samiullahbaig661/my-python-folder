# dic = {
#        "spoon" : "metal",
#        'age' : 19,       
#        "sami":"human being",
#        "semester": "first sem",
#        "cast" : "mughal"
#        }
# for i in dic:
#     if 'sami' in  dic  :    
#      print(dic['sami'])
#      exit(0)
# print(dic["sami"])/
# for i in (dic):
#    print(f"the key {i} and the value of tht key is {dic[i]}")
#    if 'human being' == dic[i]:
     
#      print ("ohhh! Wow you are a human being",i)
     
# for key in dic.keys():
#     print(f' the value corrsponding to the key...{key}... is ...{dic[key]}...')
      
# dic.items()
# print(dic)
# for key , value in dic.items():
#      print(f' the value corrsponding to the key...{key}... is ...{value}...')
      


# rrr =  [(x,y) for x in [1,2,3] for y in [1,5,2]  if x  !=  y]
   
# print(rrr)

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




# a = (1,2,3,4,5)
# oupt = {x : x**2 for x in a}
# print(oupt)





#try at home to improve
educational_status = input("enter educational status (ongoing/dropout):")
matriculation = input("Status of matriculation (done/not done):")
saylani_test = input("Status of test (pass/fail):")
if educational_status.lower() == "ongoing":
  if (saylani_test.lower() == "pass" and matriculation.lower() == "done"):
      print("you are eligible for addmision")
  else:
     print("you are not elegible for addmmision")
else:
    print("sorry you are not eligible for the test")