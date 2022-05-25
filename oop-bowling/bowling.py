from player import Player

class Game:
    def __init__(self):
        self.current_frame = 0
        self.players = self.get_players()
        self.results = self.play()

    #region GET_PLAYERS()
    def get_players(self):
        all_players = []
        number_of_players = int(input("How many players? Select up to 5 players: "))
        while number_of_players < 1 or number_of_players > 5:
            number_of_players = input("Please select from 1 to 5 players: ")
        for i in range(number_of_players):
            player = Player(input(f"Enter player {i+1}'s name: "))
            all_players.append(player)
        return all_players
    #endregion

    # simulates a game and returns the scores for each player
    def play(self):
        while self.current_frame < 10:
            for player in self.players:
                player.roll_ball(self.current_frame)
            self.current_frame += 1

    # get player.score from each player and print it
    def get_final_scores(self):
        for player in self.players:
            print(f"{player.name} bowled {player.calculate_score()}")

    # still need to change 0's to dashes ('-')
    def print_pretty(self):
        for player in self.players:
            print()
            for i in range(len(player.frames)):
                # still need to fix the 10th frame so it prints spares and strikes
                if i == 9:
                    print(f"{player.frames[i].roll_1} | {player.frames[i].roll_2} | {player.frames[i].roll_3} ||")
                elif player.frames[i].mark == '/':
                    print(f" {player.frames[i].roll_1} | {player.frames[i].mark} ||", end='')
                elif player.frames[i].mark == 'X':
                    print(f"   | {player.frames[i].mark} ||", end='')
                else:
                    print(f" {player.frames[i].roll_1} | {player.frames[i].roll_2} ||", end='')
            for i in range(len(player.frames)):
                if i == 9:
                    print("----------||")
                else:
                    print("-------||", end='')
            # still need to use formatting to pad the cumulative score so it lines up right
            player.score = 0
            for i in range(len(player.frames)):
                player.score += player.frames[i].get_frame_total()
                if i == 9:
                    print(f"   {player.score}   ||")
                else:
                    if player.frames[i].mark == '/':
                        player.score += player.frames[i+1].roll_1
                    elif player.frames[i].mark == 'X':
                        player.score += player.frames[i+1].roll_1 + player.frames[i+1].roll_2
                    print(f"    {player.score} ||", end='')


game = Game()
game.get_final_scores()
game.print_pretty()