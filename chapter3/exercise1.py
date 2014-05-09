# Madilynn Douglas 2096750

# Kilometer Converter

#// Start of pseudo code
# Input the kilometer 
# Calculate miles
# Display miles
# end of pseudo code//

def main():
	# Input for creating the kilometer variable
	kilometers = int(input("How many kilometers?: "))
	# convert the kilometers into miles
	converter(kilometers)

def converter(kilometers):

# The calculation for figuring out the miles from kilometers
	miles = kilometers * 0.6214
# print and the display of the converted miles
	print('Miles: ', miles)

# call the main function
main()

