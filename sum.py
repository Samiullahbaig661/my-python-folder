# num1= (input("enter you num "))
# if num1 > 0: 
#     print (num1)
# else: 
#     print("not valid")
num1 = input("Enter your number: ")

if num1.isdigit():  # Check if input is numeric
    num1 = int(num1)  # Convert the input to an integer
    if num1 > 0:
        print(num1)
    else:
        print("Number is not positive.")
else:
    print("Invalid input! Please enter a valid integer.")
