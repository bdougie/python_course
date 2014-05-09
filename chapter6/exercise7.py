# Madilynn Douglas 2096750

#/ start of the pseudo code. 

# set values for the even and odd counts to 0
# create a for loop with a range 100 numbers
# within the loop identify if the number is even by dividing by 2
# odds are any numbers not divided by 2
# print how numbers are odd and how are even

#/ end of pseudo code

import random

# call the main function
def main():
	# create a variable so he user can enter a number
	num = int(input('How many numbers?: '))
	# set the odds conut to zero
	evens = 0
	# set the evens count to zero
	odds = 0
		# creates the 100 random numbers and is not limited to 1 to 100
	for number in range(num):
		number = random.randint(1, 100)
		# identify if the number is divisble by 2, if true it is even.
		if number % 2 == 0:
			# increase the count by 1 if true
			evens += 1
		# everything else is odds
		else:
			# increase the odds count by 1
			odds += 1

	# print the statement showing the final counts for each.
	print('There are ', odds, ' odd numbers and ', evens, ' even numbers')

main()
