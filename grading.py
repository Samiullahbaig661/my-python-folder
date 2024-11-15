try:
  while True: 
     marks = int(input("Enter your inter marks out of (1100) "))
   
     per = (marks / 1100) * 100
     p = round(per,2)
     if(p >= 80 and p <=90):
        print(f"Congratulations! your grade is A+ 'EXCELLENT' with {p}% ")
     elif(p >= 70 and p <80):
        print(f"your grade is A 'GOOD' with {p}%")
     elif( p >= 60 and p <70 ):
        print(f"Your grade is B 'BEST' with {p}%")
     elif(p>=50 and p < 60):
       print(f"your grade is C 'SATISFACTORY' with {p}% ")
     elif(p >= 40 and p<50):
      print(f"your grade is D 'NOT SATISFACTORY' with {p}%")
     elif(p >= 33 and p < 40 ):
      print(f"your grade is E 'BAD' with {p}%")   
     elif(p < 33):
      print(f"your are fail and grade is 'F' 'FAIL' with {p}%") 
except:
     print ("some error occured")   


a = 50
if(a>60):
 print('number found at 0')
elif(a>=40):
   if(a>100):
     print("number found at 1")
   elif(a>60):
     print("found at 2") 
   elif(a>51):
     print("found at 3") 
   elif(a<=50):
     print("found at 4")
   else:
     print("not found")
else:
  print("not found")       




firstname = input("Enter your firstname : ").lower().strip()
lastname = input("Enter your lastname : ").lower().strip()
midlename = input("Enter your midelname : ").lower().strip()

if firstname == "sami" and lastname == "baig" and midlename == "ullah":
    print("the book is wrote by samiullah baig")
else:
    print("THe book has no auther")

