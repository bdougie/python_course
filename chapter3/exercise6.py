# Madilynn Douglas 2096750

#// Start of pseudo code
# Collect weight and height from the user and store date in variables
# calcualte the BMI variable using the height and weight variables
# print the newly calculated BMI variable
# end of pseudo code//


# Body Mass Index

def main():

	# collect weight input from user
	weight = int(input("What is your weight in lbs?: "))
	# collect height input from user
	height = int(input("What is your height in inches?: "))
	# call the overweight function
	overweight(weight, height)

#create a function called overweight
def overweight(weight, height):
	
	# calculate the BMI using the weigh and height variables, while creating a BMI variable
	BMI = weight * (703 / (height ** 2))
	# displays the BMI variable
	print("Your BMI is: ", BMI)

# call and print the overweight function
main()

