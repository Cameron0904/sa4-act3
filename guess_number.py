number = 10
guess = 0
print("I'm thinking of a number...")
while guess != "q":
    guess = (input("What number am I thinking of? "))

    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"Sorry that was incorrect. Try again!")
        if int(guess) > number:
            print("The number is lower(hint)!")
        else:
            print("The number is higher(hint)!")



if guess == 'q':
    print(f'The number was {number}')