#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    def __init__(self, name="Unknown", breed="Mastiff"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name

    def set_name(self, name):
        # Check if name is a string and its length is between 1 and 25 characters
        #if empty string
        # breakpoint()
        if name == "":
            print("Name must be string between 1 and 25 characters.")
        elif not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
        elif not (1 <= len(name) < 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        # Check if breed is in the list of approved breeds
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

    breed = property(get_breed, set_breed)




# fido = Dog("")
# print(fido.name) # returns empty string 

# snoopy = Dog("k")
# print(snoopy.name) # returns k

# fido.breed = "Corgi"
# print(fido.breed)  # Using the property