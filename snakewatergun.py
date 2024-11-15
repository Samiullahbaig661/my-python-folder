import random
while(True):
    choice = ["R","P","S"]
    user_inp = input("Please enter R for rock , P for paper , S for seassor : ").upper()
    computerchoice = random.choices(choice)
    if(user_inp == choice):
        print("game Tie")    
    if user_inp not in choice:
        print("Invalid charecter")
    elif(user_inp == "R" and computerchoice == "S") or \
        (user_inp == "S" and computerchoice == "P") or \
        (user_inp == "p" and computerchoice == "R"):
        print("you win ")
    else:
        print("you loose")       

    