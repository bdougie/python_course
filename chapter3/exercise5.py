# Madilynn Douglas 2096750

# Property Tax

#// Start of pseudo code
# Ask for the property value
# calculate 60% of the value as the assessed value
# end of pseudo code//

def main():

		#idetify the property value using a input
		property_value = int(input('What is the property value: '))
		#call the property function
		property(property_value)


#create the property function
def property(property_value):
	
		#idetify the assessment value using a the property value * 60%
		assessment_value = property_value * .60
		#property tax identified calculation (every $100 is 64 cents in tax)
		property_tax = (assessment_value / 100) * .64

		#Print the newly calculated values for property tax and assessment values.
		print('Assessment Value: ', assessment_value)
		print('Property Tax: ', property_tax)

main()