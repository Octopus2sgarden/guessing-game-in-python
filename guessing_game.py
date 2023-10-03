import random
name = input('Hello! What is your name? ')
print(f'Ok, {name} I have a number in my mind between 1 and 100 wanna guess? ')

number = random.randint(1,100)

how_many_guesses = 10 
number_of_guesses = 1

for number_of_guesses in range(how_many_guesses):
    guess = int(input(f'{number_of_guesses + 1}. guess'))
    number_of_guesses +=1

    if guess < number:
        print("Too low ")
    elif guess > number:
        print("Too high ")
    else:
        break
if guess == number:
    print(f"Congrats!! {name} knew the number in {number_of_guesses} tries")
else:
    print(f"Sorry {name} you could not guess the number it was {number}")

