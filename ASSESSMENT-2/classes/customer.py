from classes.helper import Helper
import re

class Customer:
    FILE_NAME = '../data/customers.csv'
    NEXT_ID = [1]

#region magic methods
    def __init__(self, account_type, first_name, last_name, id=None, current_video_rentals = ''):
        self.id = Helper.get_id(id, Customer)
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals
        self.max_rentals = self.set_max_rentals()
        self.num_rentals = 0

    def __repr__(self):
        return f'{self.id}, {self.first_name} {self.last_name}'

    def __str__(self):
        format_videos = self.current_video_rentals.replace('/','\n')
        account_str = ''
        if self.account_type == 'sx': account_str = 'Standard'
        elif self.account_type == 'sf': account_str = 'Standard Family'
        elif self.account_type == 'px': account_str = 'Premium'
        elif self.account_type == 'pf': account_str = 'Premium Family'

        return f'\nName:\t{self.first_name} {self.last_name}\nAvailable Rentals: {self.max_rentals-self.num_rentals}\nAccount Type: {account_str}\n\nRentals Out:\n{format_videos}'
#endregion   
#region regular methods
    def set_max_rentals(self):
        """Used on instance initialization or when changing customer account types"""
        if self.account_type == 'px' or self.account_type == 'pf':
            return 3
        else:
            return 1

    def can_rent_more(self):
        return (self.max_rentals-self.num_rentals) > 0
    
    def has_no_videos(self):
        return self.num_rentals == 0

    def allowed_rating(self, rating):
        if rating == 'R':
            if self.account_type == 'sf' or self.account_type == 'pf':
                return False
        return True

    def has_video(self, title):
        movies = self.current_video_rentals.split('/')
        return True if title in movies else False
    
    def has_ratedR(self, inventory):
        customer_movies = self.current_video_rentals.split('/')
        for movie in customer_movies:
            for video in inventory:
                if movie == video.title and video.rating == 'R':
                    return True
        return False
    
    def rent_movie(self, title):
        if self.num_rentals + 1 > self.max_rentals: raise Exception('Customer cant rent more than max allowed')
        self.num_rentals += 1
        if self.num_rentals > 1: self.current_video_rentals += '/'
        self.current_video_rentals += title
    
    def return_video(self, title):
        if self.num_rentals == 0: raise Exception('Customer has no videos to return')
        self.num_rentals -= 1
        movies = self.current_video_rentals.split('/')
        movies.remove(title)
        self.current_video_rentals = '/'.join(movies)
#endregion
#region class/static methods
    @classmethod
    def get_vars(cls):
        return ['id', 'account_type', 'first_name', 'last_name','current_video_rentals']

    @classmethod
    def load_all_customers(cls):
        customer_list = Helper.read_all(cls.FILE_NAME, cls)

        # set customers number of already rented movies as they are loaded
        for customer in customer_list:
            rental_array = customer.current_video_rentals.split('/')
            num_current_rentals = len(rental_array)
            if num_current_rentals == 1 and rental_array[0] == '':
                num_current_rentals = 0
            customer.num_rentals = num_current_rentals
        return customer_list

    @classmethod
    def save_all_customers(cls, customers):
        return Helper.write_all(cls.FILE_NAME, customers)
    
    @classmethod
    def save_customer(cls, new_customer):
        return Helper.write_one(cls.FILE_NAME, new_customer)

    @staticmethod
    def get_customer_data():
        customer_data = {}
        customer_data['first_name'] = input('Enter customer first name:\n')
        customer_data['last_name']  = input('Enter customer last name: \n')
        customer_data['account_type'] = Customer.get_account_type()
        return customer_data

    @staticmethod
    def get_account_type(compare_type=None):
        """Helper to get account type. Optional arguement (must be of string type) to ensure the same account type that is passed in is not passed back out."""

        account_types = ['sx', 'px', 'sf', 'pf']
        valid = False
        new_account_type = ''
        account_choice = input('Choose account type (Q to quit to menu):\n1 - Standard\n2 - Premium\n3 - Standard Family\n4 - Premium Family\n>>> ')
        # gets customer account type and handles invalid input
        while not valid:
            if account_choice == 'Q': return None
            elif re.search(r'\A[1-4]\Z', account_choice) != None: #ensures only 1-4 entered
                new_account_type = account_types[int(account_choice)-1]
                if new_account_type == compare_type:
                    account_choice = input('Customer already has that account type, choose another: ')
                else: 
                    valid = True
            else:
                account_choice = input('Not a valid account type, try again\n>>> ')
        
        return new_account_type
#endregion
