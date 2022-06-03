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
    return(f'{" ".join(self.letters[0])}\n{" ".join(self.letters[1])}\n{" ".join(self.letters[2])}\n{" ".join(self.letters[3])}')

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
    self.show_board()
    self.new_game()

  def new_game(self):
    want_to_play = "yes"
    while want_to_play == "yes":
          user_input = input("Please enter a word: ")
          if self.include_word(user_input):
                print("Good job! Found that word")
          else:
                print("Sorry. That word is not found")
          want_to_play = input("Keep going? ")

  def show_board(self):
    print(f'{" ".join(self.letters[0])}\n{" ".join(self.letters[1])}\n{" ".join(self.letters[2])}\n{" ".join(self.letters[3])}')

  def include_word(self, word):
    word = word.upper()
    for i in range(len(self.letters)):
          for j in range (len(self.letters[i])):
                if self.letters[i][j] == word[0] and BoggleBoard.search(self,i,j,0,word):
                      return True
    return False

  def search(self, i, j , count, word):
    if count == len(word):
          return True

    if i < 0 or i >= len(self.letters) or j < 0 or j >= len(self.letters[i]) or self.letters[i][j] != word[count]:
          return False

    temp_letter = self.letters[i][j]
    self.letters[i][j] = " "
    is_found = BoggleBoard.search(self,i + 1, j, count + 1, word) or BoggleBoard.search(self,i - 1, j, count + 1, word) or BoggleBoard.search(self,i, j + 1, count + 1, word) or BoggleBoard.search(self, i, j - 1, count + 1, word) or BoggleBoard.search(self, i - 1, j - 1, count + 1, word) or BoggleBoard.search(self, i - 1, j + 1, count + 1, word) or BoggleBoard.search(self, i + 1, j - 1, count + 1, word) or BoggleBoard.search(self, i + 1, j + 1, count + 1, word)

    self.letters[i][j] = temp_letter
    return is_found