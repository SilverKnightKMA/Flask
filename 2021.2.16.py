###Welcome

my_name = "Tung"
print("Hello and welcome " + my_name + "!")

###Comments

# silverknightkma

###Print

print("Hello world!")

###Strings

print("Tung")
print('Tung')

###Variables

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "An english muffin"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = "An english muffin"
# Printing out dinner
print("Dinner:")
print(meal)

###Errors

#print('This message has mismatched quote marks!")
#print(Abracadabra)

print("This message has mismatched quote marks!")
print('Abracadabra')

###Numbers

# Define the release and runtime integer variables below:
release_year = 2021
runtime = 7200

# Define the rating_out_of_10 float variable below: 
rating_out_of_10 = 9.0

###Calculations

print(25 * 68 + 13 / 28)

###Changing Numbers

quilt_width = 8
#quilt_length = 12
quilt_length = 8
print(quilt_width*quilt_length)

###Exponents

# Calculation of squares for:
# 6x6 quilt
print(6 ** 2)
# 7x7 quilt
print(7 ** 2)
# 8x8 quilt
print(8 ** 2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6 ** 4)

###Modulo

my_team = (27%4)
print(my_team)
p26_team = (26%4)
print(p26_team)
p28_team = (28%4)
print(p28_team)

###Concatenation

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6
print(message)

###Plus Equals

total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price += nice_sweater + fun_books
print("The total price is", total_price)

###Multi-line Strings

to_you = """
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
"""
print(to_you)

###Review

my_age = 21
half_my_age = my_age/2
greeting = "Hello World!"
name = "SilverKnightKMA"
greeting_with_name = greeting+" "+name


###Receipts for Lovely Loveseats
#Adding In The Catalog
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_settee_price = 180.50
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15
sales_tax = .088
#Our First Customer
customer_one_total = 0
customer_one_itemization = ""
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description
customer_one_tax = sales_tax*customer_one_total
customer_one_total += customer_one_tax
print("Customer One Items: "+customer_one_itemization)
print("Customer One Total: ")
print(customer_one_total)