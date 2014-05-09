# Madilynn Douglas 2096750

#// start of pseudo code //#

# Ask for the weight from the user
# calculate the shipping charge based on the weight, using a if statement
# print shipping charge

#// end of pseudo code //#

def main():
		weight = float(input('what is the weight of the package?'))

		# If statement providing the the corresponding shipping charge rate based on weight
		if weight < 2:
			charge = 1.10
		elif weight >= 2 and weight < 6:
			charge = 2.20
		elif weight >= 6 and weight < 10:
			charge = 3.70
		else:
			charge = 3.80

		shipping_cost = charge * weight

		print('Shipping total is $',  "{:.2f}".format(shipping_cost))

# call the main function			
main()