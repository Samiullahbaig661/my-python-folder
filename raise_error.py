a = int(input("Enter a number between 5 and 9: "))
b = input("Enter a string (e.g., 'quit' to skip the error): ").lower()

if a < 5 or a > 9:
    if b != "quit":
        raise ValueError("The value must be between 5 and 9.")
    else:
        print("No error raised because you entered 'quit'.")
else:
    print(f"You entered: {a}")

