import random 

def play():
    user = input("Choose one: 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        print("It's a tie!")
        return 'It\'s a tie'

    #  r > s, s > p, p > r
    if is_win(user, computer):
        print("You won!")
        return 'You won!'
    print("You lost, computer won!")    
    return 'You lost, computer won!'

def is_win(player, opponent):
    if((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')):
        return True 


play()        