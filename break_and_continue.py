#  Using breake and countinue statements
hi = int(input("Enter the integer"))
for i in range(hi):
    if(i == 8):
        print(f"there you go {i}")
        continue
    if(i == 10 ):
        print(f"mai tu toot gya ")
        break
    print(i)
    i += 1   
