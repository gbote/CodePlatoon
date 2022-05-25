import itertools
from dice import Dice

class BoggleBoard:
  dice_values = [
        'AAEEGN', 'ELRTTY', 'AOOTTW', 'ABBJOO',
        'EHRTVW', 'CIMOTU', 'DISTTY', 'EIOSST',
        'DELRVY', 'ACHOPS', 'HIMNQU', 'EEINSU',
        'EEGHNW', 'AFFKPS', 'HLNNRZ', 'DEILRX'
  ]

  def __init__(self):
    self.board = [[],[],[],[]]
    for dice_num, (row, _) in enumerate(itertools.product(self.board, range(4))):
      row.append(Dice(self.dice_values[dice_num]))
    print(self)

  def __str__(self):  # sourcery skip: avoid-builtin-shadow
    # print out the current board in the correct format
    str = 'Current Board: \n'
    for index,row in enumerate(self.board):
      for i in range(4):
        val = row[i].get_value()
        tab = "  " # custom tab
        if val == 'Q':
          tab = 'u ' #custom tab accounting for the 'u'
        str += val + tab
      if index != 3:
        str += '\n'

    return str

  def shake(self):
    for row, i in itertools.product(self.board, range(4)):
      row[i].roll()
    print(self)