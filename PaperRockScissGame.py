import random

while True:

    print('Welcome in paper, rock and scissors game! ')
    user_option = input('Choose ur option: ')
    user_option = str(user_option)
    user_option = user_option.lower()
    options = ['paper', 'rock', 'scissors']
    computer_option = random.choice(options)

    if user_option not in options:
        print('Wrong answer! ')
    else:
        print('U chose: ', user_option)
        print('Computer chose: ', computer_option)
        if user_option != computer_option:
            if user_option == 'rock':
                if computer_option == 'paper':
                    print('U loose!')
                elif computer_option == 'scissors':
                    print('U win!!!')
            if user_option == 'paper':
                if computer_option == 'rock':
                    print('U win!!!')
                elif computer_option == 'scissors':
                    print('U loose!')
            if user_option == 'scissors':
                if computer_option == 'paper':
                    print('U win!!!')
                elif computer_option == 'rock':
                    print('U loose!')
        elif user_option == computer_option:
            print('Draw!')
        print()
