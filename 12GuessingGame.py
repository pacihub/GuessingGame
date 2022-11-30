import random
import os
import time

# make a list of numbers from 1 to 100
numbers = [i for i in range(1,101)]

# generate a random number from a list
def gen_rand_numb(options):
    z = random.choice(options)
    return z

tries = 0
easy_level_tries = 10
hard_level_tries = 5

while True:
    game_opns = ['yes', 'no']
    # prompt user if they want to play. Verify the input is either YES or NO
    try:
        print("Welcome to the number guessing name.")
        play = input("Do you want to play? yes/no ")
        if play not in game_opns:
            raise ValueError

        if play == 'yes':
            # prompt user for difficulty level. Verify the user input is either 'easy' or 'hard'
            while True:
                levels = ['easy', 'hard']
                level = input('pick a level: [hard/easy] ')
                if level not in levels:
                    pass
                else:
                    break

            if level == 'easy':     # easy level gives 10 tries to the player
                print(f'You have {easy_level_tries} tries.')
                tries = easy_level_tries
            elif level == 'hard':
                print(f'You have {hard_level_tries} tries.')
                tries = hard_level_tries          # hard level gives 5 tries to the player
            print("I am thinking of a number between 0 and 100.")
            numba = gen_rand_numb(numbers)      # pick a random number between 0 and 100
    #        print('check: ', numba)

            # game loop. While the player still has tries left, they keep getting prompted.
            while tries > 0:
                try:
                    # keep prompting until player enters a positive number <= 100
                    guess = int(input('guess the number: '))
                    if guess > 100 or guess < 0:
                        raise ValueError
                    elif guess == numba:
                        print('you win')
                        time.sleep(1.3)         # 'you win' stays on screen for 1.3 seconds
                        os.system('clear')      # clears screen for new game
                        break

                    elif guess < numba:
                        tries -= 1
                        print(f'too small, you have {tries} tries left')
                        if tries == 0:
                            print('you lost. The number was: ',numba)
                    elif guess > numba:
                        tries -= 1
                        print(f'too large, you have {tries} tries left')
                        if tries == 0:
                            print('you lost. The number was:',numba)
                except ValueError:
                    pass

        else:
            print("See you later.")
            break
    # catches ValueError raised from not receiving yes/no as input to 'Do you want to play? and returns back loop top'
    except ValueError:
        continue
