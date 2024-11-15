while True:
    x = int(input("Enter the integer: ")) 
    
    match x:
        case 0:
            print("This is not 30")
        case 10:
            print("This is 10")
        case 20:
            print("This is 20")
        case _:
            print("Not a match")

    sami = input("Enter the name (or type 'exit' to stop): ")
    if sami.lower() == "exit":
        break
print("Loop exited!")
