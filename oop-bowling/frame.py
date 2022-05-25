class Frame:
    def __init__(self, frame_number):
        self.frame_number = frame_number
        self.roll_1 = 0
        self.roll_2 = 0
        self.roll_3 = 0
        self.total = 0
        self.mark = None

    # for ease of calculating the total later
    def get_frame_total(self):
        return self.roll_1 + self.roll_2 + self.roll_3