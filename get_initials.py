def get_initials(name):
    firstpart , secondpart= name.split()
    print(f"{firstpart.capitalize()[0]}.{secondpart.capitalize()[0]}")

name = input("Enter your first and last name")
get_initials(name)
