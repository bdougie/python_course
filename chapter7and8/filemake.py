# Madilynn Douglas 2096750

#/ start of the pseudo code. 

# create loop that prints 5 numbers
# adds numbers to a list
# save the output to a file

#/ end of pseduo code.

import random # input random data
# create the main function
def main():
	number_list = []
	# begin the loop to create 5 random numbers
	for number in range(5):
		number = random.randint(1, 100) # create numbers only from 1 to 100
		number_list.append(number) # adds the number to an list

		# open a file to write numbers to
		outfile = open('mynumbers.txt', 'w')

		for number in number_list:
			# write number as a string in the file
			outfile.write(str(number) + '\n') # write the numbers to the file
		outfile.close() #close the file

	print('Here are your randomly generated numbers: ', number_list)
#call the main function 
main()