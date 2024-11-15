# x = 4 
# print(x)
# def hello():
#     x = 5 
#     print(f"hello sami how are you? : local : {x}")
# print(f"global : {x}")
# hello() 
# x = 5
# print(f"global : {x}")   



x = 10 
def my_function():
    global x 
    x = 15
    y = 5 
    print (y)
my_function()
print(x)