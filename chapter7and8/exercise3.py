# Madilynn Douglas 2096750

#/ start of the pseudo code. 
# Get the amount of rainfall for each month of each year using a loop.
# Display the average, total, and per month with highest, 
#/ end of pseduo code.

def main():
	#set variables
	amount = []
	total = 0

	print('There are 12 months in a year, please enter the amount of rainfall for each month in inches')

	# begin loop to ask rainfall amount for months 1-12
	for month in range(12):
		rain = int(input("Enter the amount of rain for the months Jan-Dec on seprate lines: ")) # collect the rain
		amount.append(rain) # add rainfall to the amount list
		total += rain

	# set more variables
	average = total/12
	highest = max(amount)
	lowest = min(amount)
	# find out the index of the highest and lowest amounts
	h_index = amount.index(highest)
	l_index =	amount.index(lowest)
	
	# Print the values
	print('Total rainfall for the year is:', total, 'inches')
	print('Average rainfal for year is:', average, 'inches')
	print('The month with the highest rainfall is:', highest, 'inches in month', l_index + 1)
	print('The month with the lowest rainfall is:', lowest, 'inches in month', h_index + 1)
		
main()