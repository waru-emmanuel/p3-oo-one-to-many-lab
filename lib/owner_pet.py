class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)




'''Pet Class:
PET_TYPES:  A class variable that holds valid pet types.
all:  A class variable that holds all instances of Pet.
__init__: Initializes the pet with a name, type, and optional owner. 
Validates the pet type and adds the pet to the owner's list and to the class variable all.


Owner Class:
__init__:  Initializes the owner with a name and an empty list for pets.
pets():  Returns the list of pets owned by the owner.
add_pet():  Validates if the added object is an instance of Pet, sets the owner of the pet, and adds it to the owner's pet list.
get_sorted_pets():  Returns the list of pets sorted by their names.'''