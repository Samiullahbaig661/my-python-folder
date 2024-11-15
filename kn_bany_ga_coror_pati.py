# questions = [
#     "Who is the current Prime Minister of Pakistan?",
#     "What is the capital of France?",
#     "Which planet is known as the Red Planet?",
#     "Who wrote the play 'Hamlet'?",
#     "What is the square root of 64?"]
# correct_answers = ["shahbaz sharif",
#                    "paris",
#                    "mars",
#                    "william shakespeare",
#                    "8"]
# prizes = [10000, 20000, 30000, 40000, 50000]
# # add wining amount in this 
# total_amount = 0
# #for itration
# for i in range(len(questions)):
#     print(f"Question {i+1}: {questions[i]}")
#     user_answer = input("Enter your answer: ").lower()
#     #check condition 
#     if user_answer == correct_answers[i]:
#         print("Correct answer!")
#         total_amount += prizes[i]
#     else:
#         print("Wrong answer! The correct answer was:", correct_answers[i])
#         continue
#     # final wining amount at the end of the game
# print(f"Congratulations! You've won a total of Rs. {total_amount}.")




question = [[ "Who is the current Prime Minister of Pakistan?", 
             "A) nawaz","  B) shahbaz",
             "C) zardari","D) asim munir", 4 ],
             ["What is the capital of France?",
              "A) Berlin ","B) Madrid",
              "C) Paris","  D) Rome", 3],
             ["Which of the following is a programming language?",
              "A) Python","B) Snake",
              "C) Cobra"," D) Viper" ,2],
             ["What is the largest planet in our solar system?",
              "A) Earth","  B) Mars",
              "C) Jupiter","D) Saturn" , 3],
             [ "Who wrote the play 'Romeo and Juliet'?",
              "A) Mark Twain","     B) William Shakespeare",
              "C) Charles Dickens","D) Jane Austen", 1],
             ["What is the boiling point of water at sea level?" ,
              "A) 90°C"," B) 100°C",
              "C) 110°C","D) 120°C" , 4],
             ["Which element has the chemical symbol 'O'?",
              "A) Oxygen","B) Gold",
              "C) Silver","D) Helium", 1 ]
 ]
levels = [1000 , 2000 , 4000 , 8000 ,160000 , 320000 , 640000 ]
money = 0

for i in range (7):
    print(f"Question no {i+1} \n{question[i][0]} ")
    print(f"     {question[i][1]}          {question[i][2]}")
    print(f"     {question[i][3]}          {question[i][4]}")
    ans = int(input("enter the correct answer '1-4' "))
    if (ans == question[i][5]):
        print (f"correct answer you won your money price {levels[i]} rupees")
        money += levels[i]
    else:
        print(f"Wrong answer!!!! The corect answer is {question[i][4]} ") 
        break   
print(f"your winning amount is {money}")        