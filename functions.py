# making a function for look professional and amake a program easier

# required argument 

# def name(firstname , lastname, midilname =" "):
#     print(f"hello {firstname}{midilname} {lastname} i am percentage and mean calculator")
# def geometricmean (a,b):
#     gm = (a*b)/(a+b)
#     print(f"here is the geometric mean : {gm.__round__(2)}")
# def greaternumber (a,b):
#     if(a>b):
#         print("first number is greater")
#     else :
#         print("second number is greater") 
# def calculatepercent(a,b,firstname , lastname, midilname =" "):
#      c = ((a/b)*100)
#      print (f"{firstname}{midilname} {lastname} your inter percentage is : {c.__round__(2)}% ")
            
# fname = input("what is your first name : ")
# mname = input("what is your midle name : ")
# lname = input("what is your last name : ")
# s = int(input("enter the inter obtained marks : "))
# f = int(input("enter the inter max marks : "))
# name(fname,lname,mname)
# calculatepercent(s,f,fname,lname,mname)
# geometricmean(s,f)
# greaternumber(s,f)


###################################
 
# defult funtions


# def average (*numbers):
#     sum =0    
#     for i in numbers:
#       sum +=i
#     return (sum/len(numbers)).__round__(2)
# i = 0
# count =0
# while True:
#   numb =int(input("enter the numbers"))
#   i+=numb
#   count +=1
#   if numb == 0:
#     print (f"Average : ", c)
#     break
#   c = average(i/(count))



##########################

# def frequency(name):
#   for i in name:    
#      print(f'{name.count(i)} = {i}')


# name = "Listen"
# frequency(name)


###########3

# def replace (name=""):
#     name = "elephant"
#     name1 = name.replace("e","")
#     print(name1)

# replace()

##################$


# def replace(list1=[]):
    
#    post1 = 2 
#    post2 = 5
#    post1 -= 1
#    post2 -= 1 
#    list1[post1],list1[post2]=list1[post2],list1[post1]
#    print(list1)
    
# list1 = [1,2,3,4,5]
# replace(list1)



#########################


# def unique_elements(number):
#     unique_elements = set(list1)
#     for element in unique_elements:
#       print(element)
# list1 = [1,2,3,3,4,5,5]
# unique_elements(list1)

#########################


# def is_prime(num):
#    num =7 
#    if num/num == 1 and num/1 == num :
#       return True
#    else:
#       return False   
# num = 7
# num1 = is_prime(num)
# print(num1)

#########################


# def reverse_list(list1):
#   list2=list1[::-1]
#   print(list2)
# list4=[1,2,3,4,5]  
# reverse_list(list4)



# list1 = [1,2,3,4,5,6,7,8,9]
# list2 =[]
# for i in list1:
#     if i%2== 0:
#       print(i)
#       list2.append(i)
# print(list2)


#########################
      

# Function
# def countlowerupper(string):   
#    upp = 0
#    lowe = 0
#    for c in name :
#       if c.isupper():
#           upp +=1
#       if c.islower():
#           lowe +=1

#    print(f'number of uppercase letter is : {upp}') 
#    print(f'number of lowercase letter is : {lowe}')
# # main code
# name = "samiullahbaig"
# countlowerupper(name)

#########################

 #functions
# def multiply_elements(numbers):
#     a =1
#     for  i in numbers:
#          a *= i
#     return a
# #main code
# sample = [8,2,3,-1,7]
# multiplying_list_elsement=multiply_elements(sample)
# print(multiplying_list_elsement)

#########################

def wow():
      s = input("enter the string : ")
      s1 = set()
      for str in s:
        if s.count(str) >= 2:
          s1.add(str)
      print(" ".join(sorted(s1)))
print(__name__)      
if __name__ == "__main__":      
   wow()

