# your User class goes here
class NewUser:
    def __init__(self, name, email, license):
        self.name = name
        self.email = email
        self.license = license

    def __str__(self):
        return f"My name is {self.name}. My email address is {self.email}, and my license number is {self.license}."


bill = NewUser("Bill", "bill@bill.com", "IL7777777")
steve = NewUser("Steve", "steve@steve.com", "MN1111111")
bob = NewUser("Bob", "bob@bob.com", "WI3333333")
rachel = NewUser("Rachel", "rachel@rachel.com", "IL7474747")

print(bill)
print(steve)
print(bob)
print(rachel)