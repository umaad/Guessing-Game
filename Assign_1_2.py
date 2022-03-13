import random


def guessing_game():
    rand_num = random.randint(1, 100)  # we generating a random int 1, 100
    counter = 0
    while True:
        guess_num = int(input('Guess a number b/w 1 to 100'))
        counter += 1
        if rand_num > guess_num:
            print('Guess something bigger!')
        elif rand_num < guess_num:
            print('Guess something smaller')
        else:
            print(f'the game is over , and it took you {counter} time to guess it')
            break  # is a keyword to break out of anyloop when you needed


def guessing_game_partb():
    rand_num = random.randint(1, 100)  # we generating a random int 1, 100
    counter = 0
    counter1 = 0
    player1Name = input('Player1 Enter Your Name: ')
    player2Name = input('Player2 Enter Your Name: ')
    player = random.randint(1, 2)

    while True:
        if player == 1:
            guess_num = int(input(f'Player1 {player1Name}! Guess a number b/w 1 to 100'))
            counter += 1
            player = 2
        else:
            guess_num = int(input(f'Player2 {player2Name}! Guess a number b/w 1 to 100'))
            counter1 += 1
            player = 1
        if rand_num > guess_num:
            print('Guess something bigger!')

        elif rand_num < guess_num:
            print('Guess something smaller')

        else:
            if player == 2:
                print(f'the game is over , and it took {player1Name} {counter} times to guess it')
                print(f' {player1Name} Wins!')
                break
            else:
                print(f'the game is over , and it took {player2Name} {counter1} times to guess it')
                print(f' {player2Name} Wins!')
                break  # is a keyword to break out of anyloop when you needed


def guessing_game_parta():
    rand_num = random.randint(1, 100)  # we generating a random int 1, 100
    counter = 0
    counter1 = 0
    player1Name = input('Player1 Enter Your Name: ')
    player2Name = input('Player2 Enter Your Name: ')

    while True:
        guess_num = int(input('Guess a number b/w 1 to 100'))
        counter += 1
        if rand_num > guess_num:
            print('Guess something bigger!')
        elif rand_num < guess_num:
            print('Guess something smaller')
        else:
            print(f'the game is over , and it took {player1Name} {counter} times to guess it')
            break  # is a keyword to break out of anyloop when you needed
    while True:
        guess_num1 = int(input('Guess a number b/w 1 to 100'))
        counter1 += 1
        if rand_num > guess_num1:
            print('Guess something bigger!')
        elif rand_num < guess_num1:
            print('Guess something smaller')
        else:
            print(f'the game is over , and it took {player2Name} {counter1} times to guess it')
            if counter < counter1:
                print(f'Player {player1Name} wins!!')
            elif counter > counter1:
                print(f'Player {player2Name} wins!!')
            elif counter == counter1:
                print(f'There is a tie!!')
            else:
                print(f'Something went wrong!!')
            break  # is a keyword to break out of anyloop when you needed


# one player guessing game
guessing_game()
# turn by turn guessing game
guessing_game_parta()
# alternate turn guessing game
guessing_game_partb()
