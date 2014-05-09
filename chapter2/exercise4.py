# Madilynn Douglas 2096750

#Start of Pseudocode

# Input the price of each item
# Calculate the subtotal assuming the sale tax is 6 percent
# Calculate the total of all items purchased
# Diplay Total

# Input the price of each item
#rint('Enter the price of the item in using decimal')
one = int(input('What is the price of item one: '))
two = int(input('What is the price of item two: '))
three = int(input('What is the price of item three: '))
four = int(input('What is the price of item four: '))
five = int(input('What is the price of item five: '))

# Calculate the subtotal assuming the sale tax is 6 percent

subtotal = one + two + three + four + five
tax = subtotal * .06

# Display Subtotal and tax

print('Total tax is: ', tax)
print('The subtotal is: ', subtotal)


#displaying the total

final_total = subtotal + tax 

print('The final total is: ', final_total)

