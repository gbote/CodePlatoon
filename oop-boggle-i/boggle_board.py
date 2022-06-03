import random

class BoggleBoard:

  boggle_dice = [
    "AAEEGN","ELRTTY","AOOTTW","ABBJOO",
    "EHRTVW","CIMOTU","DISTTY","EIOSST",
    "DELRVY","ACHOPS","HIMNQU","EEINSU",
    "EEGHNW","AFFKPS","HLNNRZ","DEILRX"
  ]

  def __init__(self):
    self.letters = [
      ["_","_","_","_"],
      ["_","_","_","_"],
      ["_","_","_","_"],
      ["_","_","_","_"]
    ]

  def __str__(self):
    return (f'{" ".join(self.letters[0])}\n{" ".join(self.letters[1])}\n{" ".join(self.letters[2])}\n{" ".join(self.letters[3])}')

  def shake(self):
    each_boggle_dice = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    for i in range(len(self.letters)):
      for j in range (len(self.letters[i])):
        random_dice = random.choice(each_boggle_dice)
        letter_to_add_to_board = BoggleBoard.boggle_dice[each_boggle_dice.index(random_dice)][random.randint(0,5)]
        if letter_to_add_to_board == "Q":
          self.letters[i][j] = "Qu"
        else:
          self.letters[i][j] = letter_to_add_to_board
        each_boggle_dice.remove(random_dice)