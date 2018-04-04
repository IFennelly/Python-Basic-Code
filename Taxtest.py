print "This is a tax calculator. Enter in the price of your item"
print "and the program will calculate how much it costs with tax."

#Create tax function that takes price and tax_rate as imputs and returns the total price
def calculate_tax(price, tax_rate):
    total = price + (price * tax_rate)
    total = round(total, 2)             #round it to 2 decimal places
    return total

#float is a variable type for decimals
my_price = float(raw_input("Price $"))
my_price_with_tax = calculate_tax(my_price,.015)
print "The price with tax: $", my_price_with_tax