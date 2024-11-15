


# number = int(input("Enter a number which you want to find how any even number in there : "))


# # Loop through numbers from 1 to 10
# # for number in range(1,number):
# #     if number % 2 == 0:  # Check if the number is even
# #         print(number+2)

# for k in range(0,number,2):
#     print(k+2)


try:
    Welcome_statement="Hey User"
    print(Welcome_statement.center(50," "))
    n=int(input("Enter a number: "))
    if n>0:
        if n%2==0:
            print("Even number!")
        else:
            print("Odd number!")
    else:
        print("Enter a positive number")
except Exception as e:
    print(e)