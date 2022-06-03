from PersonClassFile import Person, AnotherClass
from ComputerClassFile import Computer
from SomeFolder.AnotherClass import YetAnotherClass


print(AnotherClass)
print(YetAnotherClass)

alice = Person('alice', 'influencer')

alice.work()



toaster = Computer(1)
compy386 = Computer(4)

toaster.compute()
compy386.compute()

# this class inherits from BOTH Person and COMPUTER
class MarkZuckerBorg(Person, Computer):
    def __init__(self, name, job, number_of_cores):
        # super(Person).__init__(name,job)
        Person.__init__(self, name, job)
        Computer.__init__(self, number_of_cores)

    def work(self):
        for n in range(self.number_of_cores):
            Person.work(self)

zuck = MarkZuckerBorg('Mark', 'hacker', 8)
zuck.work()