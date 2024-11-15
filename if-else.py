# apple = 210
# banana = 100
# orange  =  350
# mango = 300 
# guava = 200 
# pomogarnate = 400 
# grapes = 180
# budget = int(input("Enter your total budget"))
# buy_apple = float(input("how much apple you want(in kilo)"))
# buy2_apple = buy_apple*apple
# buy_banana =  float(input("how much banana you want(in kilo)"))
# buy2_banana = buy_banana*banana
# buy_orange =  float(input("how much orange you want(in kilo)"))
# buy2_orange = buy_orange*orange
# buy_mango =  float(input("how much mango you want(in kilo)"))
# buy2_mango = buy_mango*mango
# buy_pomogarnate =  float(input("how much pomogarnate you want(in kilo)"))
# buy2_pomogarnate = buy_pomogarnate*pomogarnate
# buy_grapes =  float(input("how much grapes you want(in kilo)"))
# buy2_grapes = buy_grapes*grapes
# buy_guava =  float(input("how much guava you want(in kilo)"))
# buy2_guava = buy_guava*guava

# buy2_pomogarnate = buy_pomogarnate*pomogarnate
# total = buy2_apple + buy2_banana + buy2_orange + buy2_mango + buy2_pomogarnate + buy2_grapes+buy2_guava
# if (budget<total):
#     print ("you have not a sufficient balence please increase your balence")
#     print("your budte is this : ", budget ,"and your total amount is this :",total)
#     print("this is the list of your fruits amount",buy2_apple,buy2_banana , buy2_orange , buy2_mango , buy2_pomogarnate , buy2_grapes,buy2_guava)
# else:
#     print("your buget is :", budget ,"your total amount of fruits is :",total, "and your remaining balence is :",budget-total)




    # Prices of fruits per kilo
fruit_prices = {
    "apple": 210,
    "banana": 100,
    "orange": 350,
    "mango": 300,
    "guava": 200,
    "pomegranate": 400,
    "grapes": 180
}
budget = int(input("Enter your total budget: "))
total_cost = 0
while True:
    fruit_name = input("Enter the fruit you want to buy (type 'done' to finish): ").lower()
    if fruit_name == 'done':
        break    
    if fruit_name in fruit_prices:
        quantity = float(input(f"How much {fruit_name} do you want (in kilos)? "))
        total_cost += quantity * fruit_prices[fruit_name]
    else:
        print("Sorry, we don't have that fruit.")
if total_cost > budget:
    print("You do not have sufficient balance. Please increase your budget.")
else:
    print(f"Your budget is: {budget}")
    print(f"Your total amount spent is: {total_cost}")
    print(f"Your remaining balance is: {budget - total_cost}")
