# Madilynn Douglas 2096750

# 10. Write a program that uses nested loops to draw this pattern:

#/ start of the pseudo code. 
# start loop for 6 rows
# begin each column with #
# place a space between each column.
# end each column with #

##
# #
#  # 
#   # 
#    # 
#     #
#/ end of pseudo code

def main():
	# start a loop with 6 rows
	for row in range(6):
	# begin each column with #
		print('#', end='')
		# start the column loop with same amount of columns as rows
		for column in range(row):
		# place a space between each column.
			print(' ', end='')
		# end each column with # 
		print('#')

main()