def unique_elements(elements):
    i  =  set(elements)
    for element in i:
      print(element)
elements = []
while True:
    enter = input("enter the number for enter in list")
    if enter == "":
       break
    elements.append(enter)
    

unique_elements(elements)