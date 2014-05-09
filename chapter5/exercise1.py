# Madilynn Douglas 2096750

#/ start of the pseudo code. 

# start day loop 
	# ask how bugs collected for day
# end the loop after day 7 
# calculate total of bugs collected
# print the new amount of bugs

#/ end of pseudo code

# define the main function
def main():
	# set the bug count to zero
	bugs = 0
	# begin the for loop with a range of 7 days
	for day in range(7):
		# ask for the input of the amount of bugs collected
		new_bugs = int(input("How bugs were collected today? "))
		# add the new bug amount to the bugs variable
		bugs = bugs + new_bugs
	# print the amount of bugs collected at the end of 7 days.	
	print('The amount of bugs collected after 7 days: ', bugs)

main()
