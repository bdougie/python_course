# Madilynn Douglas 2096750

#/ start of the pseudo code. 

# 6. Test Average and Grade

# grades input test scores into variable called total
# grade += total
# calculate average by dividing by 5
# using if/else identify if the average is an A-F
# print your letter grade average

#/ end of pseudo code

# call the main function
def main():
	# set the total to zero
	total = 0
	# start loop to collect only 5 grades
	for grades in range(5):
		# grade input
		grade = int(input('Enter your 5 grades: '))
		# determine the grade level
		what_grade = determine_grade(grade)
		# print the letter grade 
		print('Your grade is: ', what_grade) 
		# at each inputted grade to the total
		total += grade
	# set the avg variable as the average calculation
	avg = calc_average(total)
	# set the variable for the function determining what th egrade is
	what_grade = determine_grade(avg)

	print('Your average grade is: ', avg)
	print('Your grade is: ', what_grade)

# define the average calculation function
def calc_average(total):
	# calculate average using the total from the main function
	avg = total / 5
	return avg
# define the function identifying the letter grade 
def determine_grade(grade):
	avg = grade # set avg as grade
	# if/else statements for identying the letter grade average.
	if avg >= 90:
		return 'A'
	elif avg >= 80:
		return 'B'
	elif avg >= 70:
		return 'C'
	elif avg >= 60:
		return 'D'
	elif avg <= 59:
		return 'F'
# all the main function
main()
