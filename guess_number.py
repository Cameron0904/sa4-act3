number = 10
guess = 0
print("I'm thinking of a number...")
while guess != "q":
    guess = (input("What number am I thinking of? "))

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"Sorry that was incorrect. Try again!")

if guess == 'q':
    print(f'The number was {number}')