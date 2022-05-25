class GuessingGame():
    def __init__(self, target_num):
        self.target_num = target_num
        self.last_guess = None

    def solved(self):
        return self.last_guess == self.target_num

    def guess(self, player_guess):
        self.last_guess = int(player_guess)

        if self.last_guess == self.target_num:
            return "Correct"

        elif self.last_guess > self.target_num:
            return "Too High"

        else:
            return "Too Low"