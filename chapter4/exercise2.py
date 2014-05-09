# Madilynn Douglas 2096750

#// start of pseudo code //#

# collect the info for each rectangle.
# find the area of each rectangle length * width
# write the statement
# if rectangle one > rectangle two
		# then write rectangle one is greater 
# else
		# write rectangle two is greater 	

#// end of pseudo code ??# 

def main():
		#gather the lengths and widths for both rectangle one and two
		length_one =  int(input('The length of rectangle one is : '))
		width_one =  int(input('The width of rectangle one is : '))
		# set the variable for rectangle one
		rectangle_one = area_1 = length_one * width_one
		print('Area of the first rectangle: ', rectangle_one)


		length_two = int(input('The length of rectangle two is : '))
		width_two = int(input('The width of rectangle two is : '))
		# set the variable for rectangle two
		rectangle_two = area_2 = length_two * width_two
		print('Area of the second rectangle: ', rectangle_two)


		# if statement that prints whichever rectangle area is larger. 
		if rectangle_one > rectangle_two:
			print('rectangle one is greater')
		elif rectangle_two < rectangle_one:
			print('rectangle two is greater ')
		else:
			print('both rectangles are equal')

#call the main function
main()