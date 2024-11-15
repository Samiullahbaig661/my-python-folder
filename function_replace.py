def replace(list1=[]):
    
   post1 = 2 
   post2 = 5
   post1 -= 1
   post2 -= 1 
   list1[post1],list1[post2]=list1[post2],list1[post1]
   print(list1)
    
list1 = [1,2,3,4,5]
replace(list1)