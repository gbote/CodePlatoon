from boggle_board import BoggleBoard

print('Welcome to Boggle Board')

board = BoggleBoard()

input('Ready to play? Press any key:')

x = 'Y'
z = 'Y'

while x == 'Y':
    board.shake()
    while z == 'Y':
        try:
            y = input('Type a word to search for:\n')
            if board.include_word(y):
                print(f'\n{y} was found on board!\n')
            else:
                print(f'\nOh no! {y} was not found\n')
        except Exception:
            print('didnt input valid word')
        z = input('Do you want to try another word? Press Y:\n')
        if z == 'Y': print(board)

    x = input('Do you want to try another board? Press Y:')
    z = 'Y'

print('Thanks for playing!')