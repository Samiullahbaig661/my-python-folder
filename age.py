import datetime 
inp = int(input("Enter the year of the birth : "))
inp2 = int(input("Enter your month : "))
inp3 = int(input("Enter your day : "))
datee = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
montht = month - inp2
dayy =day - inp3
age = datee - inp 
if(montht < 0):
   montht =  montht*-1
if (dayy<0):
       dayy= dayy*-1
if(age > 18):
            
   print(f"congrates now you are able to put the vote because you are {dayy}/{montht}/{age} years old")
else: 
    print(f"sorry you are {dayy}/{montht}/{age} year old you are not to be able too put the vote to the any kind of party like PPP or PMLN so sorry")