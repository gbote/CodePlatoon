import itertools
class ContactList():

    def __init__(self, name, contacts = None):
        if contacts is None:
            contacts = []
        self.name = name
        self.contacts = contacts

    def add_contact(self, contact):
        self.contacts.append(contact)

    def __str__(self):
        return (f"{self.name}: {self.contacts}")

    def remove_contact(self, name):
        for index, contact in enumerate(self.contacts):
            if contact["name"] == name:
                self.contacts.pop(index)
                break

    def find_shared_contacts(self, common_contact):
        shared_contacts = []
        for first, second in itertools.product(range(len(self.contacts)), range(len(common_contact.contacts))):
            if (self.contacts[first]["name"] == common_contact.contacts[second]["name"]):
                shared_contacts.append(self.contacts[first])
            return f"{shared_contacts}"


friends = [
    {'name': 'Alice', 'number': '867-5309'},
    {'name': 'Bob', 'number': '555-5555'}
]


work_buddies = [
    {'name': 'Alice', 'number': '867-5309'},
    {'name': 'Carlos', 'number': '555-5555'}
]

my_friends = ContactList("Friends", friends)
work_friends = ContactList("Coworkers", work_buddies)

friends_i_work_with = my_friends.find_shared_contacts(work_friends)
# friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]

print(friends_i_work_with)

print(my_friends)

my_friends.add_contact({"name": "Bill", "number": "777-7777"})

print(my_friends)

my_friends.remove_contact("Alice")

print(my_friends)

my_friends.add_contact({"name": "Alice", "number": "867-5309"})