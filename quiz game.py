import time
print("Welcome to the Simple Quiz Game!")
time.sleep(1)
chances=1
print("You will have", chances, "chances to answer correctly.\nplease put the alphabet of the answer\n")
time.sleep(2)
Score=0
Question_1=print("1. How many Elements in the Periodic Table?\n(a) 116\n(b) 117\n(c) 118\n(d) 119\n\n ")
answer_1='c'
for i in range(chances):
    answer=input("Answer: ")
    if(answer.lower()==answer_1):
        print("correct! Good Job.\n")
        Score=Score+1
        break
    else:
        print("Incorrect! \n")
        time.sleep(0.5)
        print('The correct answer is ',answer_1,'\n\n ')
time.sleep(1)
Question_2=print("2. What is the Most abudant gas in Earth's atmosphere?\n(a) Nitrogen\n(b) Oxygen\n(c) Carbon-dioxide\n(d) Hydrogen\n\n ")
answer_2='a'
for i in range(chances):
    answer=input("Answer: ")
    if(answer.lower()==answer_2):
        print("correct! Good Job.\n")
        Score=Score+1
        break
    else:
        print("Incorrect! \n")
        time.sleep(0.5)
        print('The correct answer is ',answer_2,'\n\n ')
time.sleep(1)
Question_3=print("3. How many bones are in the Human body?\n(a) 206\n(b) 207\n(c) 208\n(d) 209\n\n ")
answer_3='a'
for i in range(chances):
    answer=input("Answer: ")
    if(answer.lower()==answer_3):
        print("correct! Good Job.\n")
        Score=Score+1
        break
    else:
        print("Incorrect! \n")
        time.sleep(0.5)
        print('The correct answer is ',answer_3,'\n\n ')
time.sleep(1)

if Score >= 2:
    print("Well done! Your score was", Score)
else:
    print("Better luck next time! Your score was", Score)

play_again = input("Do you want to play again? (yes/no): ")
if play_again.lower() != 'yes':
    print("Thank you for playing the Simple Quiz Game!")
    