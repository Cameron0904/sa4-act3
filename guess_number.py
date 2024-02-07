number = 10
guess = 0
print("I'm thinking of a number...")
count = 5
while guess != "q":
    if count == 0:
        print(f'The number was {number}')
        break
    guess = (input("What number am I thinking of? "))

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"Sorry that was incorrect. Try again!")
        count -=1
        print(f'You have {count} guesses left!')

if guess == 'q':
    print(f'The number was {number}')