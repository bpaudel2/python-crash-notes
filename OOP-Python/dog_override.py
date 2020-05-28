class Dog:
    species = 'mammal'

class SomeBreed(Dog):
    pass 

class SomeOtherBreed(Dog):
    species = 'reptiles'

frank = SomeBreed()
print(frank.species)

beans = SomeOtherBreed()
print(beans.species)