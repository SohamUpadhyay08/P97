import random as random
number = random.randint(1,9)
chances = 5
while chances > 0 :
    guess = int(input("guess your number : "))
    if number == guess : 
        print("Congrats!! You won")
        break
    else :
        chances -= 1
        print("try again")
if chances == 0 :
    print("better luck next time. The number was : ",number)
