from classes.customer import Customer
from classes.video import Video
from classes.helper import Helper
import re

class Store: 
    def __init__(self, name, location = 'Bend, Oregon'):
        self.name = name
        self.location = location
        self.customers = Customer.load_all_customers()
        self.inventory = Video.load_all_videos()

    def __str__(self):
        return f'{self.name} Video Store in {self.location}'

    def display_inventory(self):
        print('ID\tTitle\t\t\tRating\t  Release Year\tCopies Available')
        for video in self.inventory:
            print(video)

    def display_all_customers(self):
        Helper.clear_console()
        print('Customers: ')
        for customer in self.customers:
            print(customer.__repr__())
    
    def display_customer_videos(self):
        customer = self.get_customer()
        if customer == None: return
        print(customer)
        input('\nPress any key to return to menu')

    def add_customer(self):
        Helper.clear_console()

        #gather necessary info
        customer_data = Customer.get_customer_data()
        if customer_data == None: return #user quit out of menu
        new_customer = Customer(**customer_data) 

        #update internal/external
        self.customers.append(new_customer)
        self.customers = sorted(self.customers, key = lambda x:x.id)
        self.save()

    def rent(self):
        customer = self.get_customer()
        if customer == None: return

        if not customer.can_rent_more():
            input('This customer has already rented the maximum allowed. They must return rentals before renting more.\nPress any key to return to main')
            return
        Helper.clear_console()
        self.display_inventory()
        serving = True
        while serving:
            movie = self.get_video()
            if movie == 'Q': return
            elif customer.has_video(movie.title):
                print('\nCustomer already has this movie rented and cannot rent more than one of a movie. Try a different movie')
            elif movie.available():
                if customer.allowed_rating(movie.rating):
                    customer.rent_movie(movie.title)
                    movie.rented()
                    if not customer.can_rent_more(): 
                        serving = False
                    else:
                        serving = True if input('\nDoes the customer have more videos to rent out?\n\nPress Y to rent another video: ') == 'Y' else False
                else: 
                    print('\nCustomer account not allowed rated R. Try another movie')
            else:
                print('\nThat video is not in stock. Try another movie')
        self.save()

    def return_videos(self):
        customer = self.get_customer()
        if customer == None: return

        if customer.has_no_videos():
            input('\nCustomer has no rentals out now. Press any key to return to menu')
            return
        
        Helper.clear_console()
        print(customer)

        serving = True
        while serving:
            movie = self.get_video()
            if movie == 'Q': return
            elif not customer.has_video(movie.title):
                print('\nCustomer does not have that movie rented out. Try another movie')
            else:
                customer.return_video(movie.title)
                movie.returned()
                if customer.has_no_movies():
                    serving = False
                else:
                    serving = True if input('\nDoes the customer have more videos to return?\n\nPress Y to rent another video: ') == 'Y' else False
        self.save()

    def change_customer_account(self):
        """Upgrade or downgrade a customer account between standard and premium or between normal and family"""

        #initialize values
        Helper.clear_console()
        customer = self.get_customer()
        if customer == None: return
        Helper.clear_console()
        print(customer, '\n') #print customer for user convienence, shows data and movies they have out 

        account = Customer.get_account_type(customer.account_type)
        if account == None: return

        #customer cant downgrade to standard type with more than 1 rental out
        if (account == 'sx' or account == 'sf') and customer.num_rentals > 1:
            input('\nCustomer has too many rentals to downgrade to standard account.\nThey must return movies until they have at most 1 rental out, then try again.\n\nPress any key to return to menu ')
            return
        #customer cant change to family account with a rated R rented out
        elif (account == 'sf' or account == 'pf') and customer.has_ratedR(self.inventory):
            input('\nCustomer has Rated R movies rented.\nThey must return any Rated R movies, then try again.\n\nPress any key to return to menu ')
            return
        #all good, set new account type and update number of rentals they can have
        else:
            customer.account_type = account
            customer.max_rentals = customer.set_max_rentals()

        self.save()

    def delete_customer_account(self):
        Helper.clear_console()
        customer = self.get_customer()
        if customer == None: return

        #customer must return all rentals before closing account
        if customer.num_rentals > 0:
            input('\nThis customer still has rentals out. Return all rentals before deleting account.\n\nPress any key to return to menu')
            return
        
        Helper.return_id(customer.id, Customer)
        self.customers.remove(customer)
        self.save()
        input('\nCustomer deleted. Press any key to return to menu')

    def add_videos(self):
        Helper.clear_console()

        #gather necessary info
        video_data = Video.get_video_data()
        if video_data == None: return #user quit out of menu
        new_video = Video(**video_data) 

        #update internal/external
        self.inventory.append(new_video)
        self.inventory = sorted(self.inventory, key = lambda x:x.id)
        self.save()

    def remove_videos(self):
        Helper.clear_console()
        video = self.get_video()
        if video == None: return
        
        Helper.return_id(video.id, Video)
        self.inventory.remove(video)
        self.save()
        print(Video.NEXT_ID)
        input('\nTitle removed. Press any key to return to menu')

    def save(self):
        Customer.save_all_customers(self.customers)
        Video.save_all_videos(self.inventory)
       
    def get_customer(self):
        """Helper returns customer instance matching input ID or None if customer ID doesnt exist"""

        Helper.clear_console()
        self.display_all_customers()
        id = input('\nEnter Customer ID or Q to return to menu: ')
        while True:
            if re.search(r'\A[1-9]+\Z|Q', id) != None:
                if id == 'Q': return None
                for person in self.customers:
                    if person.id == int(id):
                        return person
            id = input('\nCustomer not found, try again with a valid Customer ID or Q to return to menu: ')

    def get_video(self):
        while True:
            movie = input('\nEnter movie title or Q to main menu: ')
            if movie == 'Q': return 'Q'
            for video in self.inventory:
                if video.title == movie: return video
            print('\nNot a valid movie title, try again')
        