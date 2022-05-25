from boggle_board import BoggleBoard

print('Welcome to Boggle Board')

board = BoggleBoard()

x = input('Ready to play? ')

while(x != 'N'):
    board.shake()
    x = input('Want to play again? ')