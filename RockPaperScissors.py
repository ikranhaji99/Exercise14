import random

def game_function():
    #player's input, choice
    player = input('Rock (R), Paper (P) or Scissors (S)? Enter your choice: ')
    #computer's input, choice
    computer_range = list(range(0, 3))
    random.shuffle(computer_range)
    computers_move = computer_range[:1]
    #the two moves together:
    return player, computers_move

result = game_function()
print(result)

#winner outcome
if result == ('R', [0]):
    print("That's a draw (RR)!")
elif result == ('R', [1]):
    print('Sorry, computer won (RP)!')
elif result == ('R', [2]):
    print('You won (RS)!')
elif result == ('P', [0]):
    print('You won (PR)!')
elif result == ('P', [1]):
    print("That's a draw (PP)!")
elif result == ('P', [2]):
    print('Sorry, computer won (PS)!')
elif result == ('S', [0]):
    print('Sorry, computer won (SR)!')
elif result == ('S', [1]):
    print('You won (SP)!')
elif result == ('S', [2]):
    print("That's a draw (SS)!")
else:
    print('Wrong input!')