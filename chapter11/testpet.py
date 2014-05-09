# Madilynn Douglas 2096750

#Start of Pseudocode

# import the pet class
# create inputs to name variables for age, name, and type
# the pet class with attributes in print function

# End of Pseudocode

# import pet class



def main():
	import pet

	# create the pet object
	pet = pet.Pet(name, animal_type, age) #UnboundLocalError: local variable 'name' referenced before assignment

	# collect data for variables
	name = input("What is you pet's name? ")
	animal_type = input("I can't quite see, What type of animal is that? ")
	age = input("And how old is your pet in years?")

	print("Let me see if I got this all correct", pet.name, "is a ", pet.animal_type, "and ", pet.age, "years old")

main()





