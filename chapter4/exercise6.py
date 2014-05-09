# Madilynn Douglas 2096750

#// start of pseudo code //#

# display all the values of coins and dollar
# gather the quantities of the coins 
# calculate how the total dollar amount of all coins collected
# display the total amount
# create if statement if the total is less than, great than, or eual to a dollar

#// end of pseudo code //#

# Global characetrs for coins
quarter_amount = 0.25
dime_amount = 0.10
nickel_amount = 0.05
penny_amount = 0.01
dollar_amount = 1.00

def main():
		# take the input of each coin and multiply the price by the quantity received
		quarters = int(input('How many quarters? '))
		# replace the value of the coins with the newly calculated price.
		quarters = quarters * quarter_amount

		dimes = int(input('How many dimes? '))
		# replace the value of the coins with the newly calculated price.
		dimes = dimes * dime_amount

		nickels = int(input('How many nickels? '))
		# replace the value of the coins with the newly calculated price.
		nickels = nickels * nickel_amount

		pennies = int(input('How many pennies? '))
		# replace the value of the coins with the newly calculated price.
		pennies = pennies * penny_amount

		# calculate the total of all coins. 
		total = quarters + dimes + nickels + pennies
		# print the total amount using the format operator
		print('The total of the amount you have is $', "{:.2f}".format(total))
		# calculate the difference between the total and the dollar amount
		difference = total - dollar_amount
		# if statement dependent on if the total and the dollar amount
		if total == dollar_amount:
			print('Conrats, you have a dollar')
		elif total < dollar_amount:
			print('Sorry you have', "{:.2f}".format(difference), 'less than a dollar')
		else:
			print('Sorry you have', "{:.2f}".format(difference), 'more than a dollar')

# call the main function
main()