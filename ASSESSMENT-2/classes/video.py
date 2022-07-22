from classes.helper import Helper

class Video:
    FILE_NAME = '../data/inventory.csv'
    NEXT_ID = [1]

    def __init__(self, title, rating, release_year, copies_available, id = None):
        self.id = Helper.get_id(id, Video)
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = int(copies_available)

    def __repr__(self):
        return f'Video: {self.id}, {self.title}'

    def __str__(self):
        #standardize title length for printability
        title = self.title
        while len(title) < 18:
            title += ' '

        return f'{self.id}\t{title}\t{self.rating}\t  {self.release_year}\t\t{self.copies_available}'

    def rented(self):  # sourcery skip: raise-specific-error
        if self.copies_available == 0: raise Exception('No copies available')
        self.copies_available -= 1

    def returned(self):
        self.copies_available += 1
    
    def available(self):
        return self.copies_available > 0

    @classmethod
    def load_all_videos(cls):
        return Helper.read_all(cls.FILE_NAME, cls)

    @classmethod
    def save_all_videos(cls, videos):
        return Helper.write_all(cls.FILE_NAME, videos)

    @classmethod
    def save_video(cls, new_video):
        return Helper.write_one(cls.FILE_NAME, new_video)

    @classmethod
    def get_vars(cls):
        return ['id', 'title', 'rating', 'release_year', 'copies_available']
    
    @staticmethod
    def get_video_data():
        video_data = {'title': input('Enter movie title:\n')}
        video_data['rating']  = input('Enter movie rating:\n')
        video_data['release_year'] = input('Enter movie release year:\n')
        video_data['copies_available'] = input('Enter # copies on hand:\n')
        return video_data