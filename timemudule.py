import time 
# timeee = time.strftime('%H:%M:%S')
# print(timeee)
hour= int(time.strftime('%H'))
# hour= int(input('Enter hour'))
# print(hour)
if hour >=5 and hour < 12:
    print("good morning ")
if hour >=12 and hour < 18:
    print("good Afternoon ")
if hour >=18 and hour < 0:
    print("good evening ")
if hour >=0 and hour < 5:
    print("mid night")    