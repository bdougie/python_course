# Madilynn Douglas 2096750

# Start of Pseudocode

# Created the class called Pet.
# initialize the age and animal type
# create get and set methods for each attribute

# End of Pseudocode

class Pet:
  # initializes the age and animal type
  def __init__(self, name, animal_type, age):
    self.__name = name 
    self.__animal_type = animal_type
    self.__age = age 

  def set_name(self, name):
    self.__name = name

  def set_animal_type(self, animal_type):
    self.__animal_type = animal_type

  def set_age(self, age):
    self.__age = age

  def get_name(self):
    return self.__name

  def get_animal_type(self):
    return self.__animal_type

  def get_age(self):
    return self.__age

