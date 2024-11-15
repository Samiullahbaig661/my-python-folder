while True:
    order = input( ">").lower()
    if order == "start":
        print('game is started')
        print ('your firt mission is to pickup the carfrom given location  write "COMPLETED"')
    if order == "start":
            print ("Car is alredy started.....!")
    elif order == "completed":
        print ("Congratulations")
    elif order != "completed":
        print ("you have not completed your first mission ")
        print('do it first')

