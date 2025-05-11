import random
number = random.randint(1,100)
while True:

    guess = int(input("guess the number between 1 and 100 :"))

    if(guess < number):
        print("Too low!Try again")

    elif(guess > number):
        print("Too high!Try again")
    else:
        print("Congratulations quickly you have guessed it")
        break