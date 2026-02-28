import random 
n = random.randint(0, 10)
guess = int(input("guess a number between 0 andd 10 :"))
guess = 0
while True:
    if n == guess:
        print("topdingiz")
        break
    guesses = guesses +1
    if guess >=3:
        print("yutqazdingiz ")
        break

