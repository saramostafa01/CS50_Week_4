import random

while True:
    try:
        n = int(input("Enter number: "))
        number = random.randint(1, n)
        while True:
            guess = int(input("Guess: "))
            if guess < number:
                print("Too small!")
                continue
            elif guess > number:
                print("Too large!")
                continue
            else:
                print("Just right!")
                break
        break
    except ValueError:
        pass