# Madilynn Douglas 2096750

#/ start of the pseudo code. 

# open the file mynumbers.txt
# converts the numbers to integers
# calculate and print te total.

#/ end of pseduo code.

def main():
	# opens the file
	infile = open('mynumbers.txt', 'r')
	# reads the contents
	numbers = infile.readlines()
	# Close the file.
	infile.close()

	# set index to 0
	index = 0
	# loop to remvoe \n from the items in the list
	while index < len(numbers):
		numbers[index] = numbers[index].rstrip('\n')
		index += 1

	# set total to zero
	total	= 0
	print('Remember the numbers you just generated?')
	# loop to find the total of the integers
	for number in numbers:	
		total += int(number) # the numbers are converter to integers
		print(number)

	print('The total of all numbers in mynumbers.txt is: ',total)

main()