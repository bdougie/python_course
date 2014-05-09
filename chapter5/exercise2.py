# Madilynn Douglas 2096750

#/ start of the pseudo code. 

# set calories_burned = 3.9 per minute
# start the execise loop for 30 minutes
# calculate the minutes burned for 10, 15, 20, 25, and 30 mins.
# print calories burned for 10, 15, 20, 25, and 30 mins.

#/ end of pseudo code

# define the main function
def main():
	#set the caloric_rate
	caloric_rate = 3.9
	# begine loop by identifying the range and step operator
	for time in range(10, 31, 5):
		# calculate the calories
		calories =	time * caloric_rate
		# print the calories burned in the amount of minutes
		print(calories, 'burned in', time, 'minutes')

main()		
