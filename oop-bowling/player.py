import random
from frame import Frame

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.frames = []

    #region
    def roll_ball(self, frame_number):

        current_frame = Frame(frame_number)
        current_roll = 0
        pins_remaining = 10
        still_rolling = True

        is_10th = frame_number == 9
        while still_rolling:
            current_roll += 1
            pins_down = random.randint(0, pins_remaining)
            pins_remaining -= pins_down

            if current_roll == 1:
                current_frame.roll_1 = pins_down
            elif current_roll == 2:
                current_frame.roll_2 = pins_down
            else:
                current_frame.roll_3 = pins_down

            # determine if strike/spare
            if pins_remaining == 0:
                if current_roll == 1:
                    if is_10th:
                        pins_remaining = 10
                    else:
                        still_rolling = False
                    current_frame.mark = 'X'

                elif current_roll == 2:
                    if is_10th:
                        if current_frame.mark is None:
                            current_frame.mark = '/'
                        pins_remaining = 10
                    else:
                        current_frame.mark = '/'
                        still_rolling = False

                else:
                    still_rolling = False

            elif current_roll == 2 and (not is_10th or current_frame.mark is None) or current_roll != 2 and current_roll == 3:
                still_rolling = False
        self.frames.append(current_frame)
    #endregion

    def calculate_score(self):
        for i in range(len(self.frames)):
            if i == 9:
                self.score += self.frames[i].get_frame_total()
                return self.score
            self.score += self.frames[i].get_frame_total()
            if self.frames[i].mark == '/':
                self.score += self.frames[i+1].roll_1
            elif self.frames[i].mark == 'X':
                self.score += self.frames[i+1].roll_1 + self.frames[i+1].roll_2