# You should re-use and modify your old BoggleBoard class to support the new requirements
import itertools
from dice import Dice

class BoggleBoard:
  dice_values = [
        'AAEEGN','ELRTTY','AOOTTW','ABBJOO',
        'EHRTVW','CIMOTU','DISTTY','EIOSST',
        'DELRVY','ACHOPS','HIMNQU','EEINSU',
        'EEGHNW','AFFKPS','HLNNRZ','DEILRX'
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

  def include_word(self, word):
    # search board, find each of first letter:
    #   -for each of first letter:
    #       -find each of second letter touching it
    #       -for each of these:
    #           -find each of third letter touching it
    #            ...
    #    
    def find_letters(letter):
      #finds all letters matching input on board and returns list of indices
      arr = []
      for i,row in enumerate(self.board):
        arr.extend([i,j] for j in range(len(row)) if row[j].get_value() == letter)
      return arr

    def is_touching(a,b):
      return any(a[0] + i == b[0] and a[1] + j == b[1] and (a != 0 or b != 0)
                 for i, j in itertools.product(range(-1, 2), range(-1, 2)))

    # recursively solves for finding letter combo matches to prevent 'finding' a letter thats been previously found
    def solve(prev_index, str, prev_matches = None):
      if prev_matches is None:
        prev_matches = []
      working_letter_indexs = find_letters(str[0])
      touching = [
          each for each in working_letter_indexs
          if is_touching(prev_index, each) and each not in prev_matches
      ]
      #now have a list of the current letter indexes that touch the previous letter
      if len(str) == 1 and not touching:
        return False
      elif len(str) == 1:
        return True
      else:
        for index, item in enumerate(touching):
          if len(prev_matches) != 0 and index > 0: prev_matches.pop()
          prev_matches.append(prev_index)
          if solve(item, str[1:],prev_matches):
              return True
        return False


    #FINAL DRIVING CODE
    word = word.replace('QU','Q') # handles Qu case
    # find each of first letter
    first_letter_indexs = find_letters(word[0])
    #handling case of 1 letter passed in
    if len(word) == 1:
      if first_letter_indexs == []:
        return False
      else:
        return True

    previous_match = []
    #for each of first letter find each of second letter that touches
    for index, element in enumerate(first_letter_indexs):
      if len(previous_match) != 0 and index > 0: previous_match.pop()
      previous_match.append(element)
      if solve(element, word[1:]) == True:
        return True
    return False