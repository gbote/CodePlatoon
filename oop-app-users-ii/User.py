# your improved User class goes here
class NewUser:
    def __init__(self, name, email_address, license_number): #once initiated, input info so that 
      self.name = name
      self.email_address = email_address
      self.drivers_license = license_number
      self.user_of_info = {'name': self.name, 'email address': self.email_address, 'license number': self.drivers_license} # create Dictionary
      self.posts = []
      self.number_of_posts = 0

    def __str__(self):
        return f"My name is {self.name}. My email address is {self.email_address}, and license number is {self.drivers_license}."

    def create_post(self, post):
      self.number_of_posts += 1
      post = f'POST {self.number_of_posts}:  {post}'
      self.posts.append(post) 

    def delete_post(self, selected_post):
      self.posts.pop(selected_post - 1)

Ivan = NewUser("Ivan", "LetsGetLoco@gmail.com", "654546")
Juan = NewUser('Juan', 'elvato@yahoo.com', "5646546432")

Ivan.create_post('Hello Everyone this is my first post!')
Ivan.create_post('Hello Everyone this is my second post!')
Ivan.create_post('Hello Everyone this is my third post!')

print(Ivan.posts)
Ivan.delete_post(1)
print(Ivan.posts)


bill = NewUser("Bill", "bill@bill.com", "IL7777777")
steve = NewUser("Steve", "steve@steve.com", "MN1111111")
bob = NewUser("Bob", "bob@bob.com", "WI3333333")
rachel = NewUser("Rachel", "rachel@rachel.com", "IL7474747")

print(bill)
print(steve)
print(bob)
print(rachel)

bill.create_post("This is Bill's 1st post!")
bill.create_post("This is Bill's 2nd post!")
bill.create_post("This is Bill's 3rd post!")

steve.create_post("This is Steve's 1st post!")
steve.create_post("This is Steve's 2nd post!")
steve.create_post("This is Steve's 3rd post!")

print(bill.posts)
print(steve.posts)

steve.create_post("This is Steve's 4th post!")
steve.delete_post(1)
print(steve.posts)