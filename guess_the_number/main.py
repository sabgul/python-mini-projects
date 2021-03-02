import random 

def guess(x): 
    random_number = random.randint(1, x)
    guess = 0 

    while guess != random_number: 
        guess = input(f'Guess a number between 1 and {x}: ')
        guess = int(guess)
        if guess < random_number:
            print('Guess was too low. Try again.')
        elif guess > random_number:
            print('Guess was too high. Guess again.') 
    print(f'Congrats, you have guessed the right number {random_number} correctly! ')            

# letting the computer guess any number we are thinking of 
def computer_guess(x):
    low = 1
    high = x 
    feedback = ''
    while feedback != 'c': # c -- correct 
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(f'Yes, the computer guessed the number you were thinking of ({guess}) correctly.')    



#guess(10)

computer_guess(10)
