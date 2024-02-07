number = 10
guess = 0
print("I'm thinking of a number...")
count = 5

while True:
    
    if count == 0:
        print(f'The number was {number}')
        break
    
    guess = (input("What number am I thinking of? "))

    if guess == 'q':
        break

    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    
    else:
        
        print(f"Sorry that was incorrect. Try again!")
        
        if int(guess) > number:
            print("The number is lower(hint)!")
        else:
            print("The number is higher(hint)!")
        
        count -=1
        print(f'You have {count} guesses left!')

if guess == 'q':
    print(f'The number was {number}')