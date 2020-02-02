"""SKILLS: FUNCTIONS

Please complete the following promps.
"""

#################### PART 1 ####################

"""PROMPT 1

Write a function that returns `True` if a town name matches the name of your
hometown.

Examples: (let's say my hometown is San Francisco)
    - 'Oakland' -> False
    - 'San Francisco' -> True

Arguments:
    - The name of a town (str)

Return:
    - True or False (bool)
"""

def is_hometown(city):
    """checks if passed argument, city, is my hometown, Alameda"""
    hometown = "Alameda"
    return city == hometown
        
# print(is_hometown('Oakland'))
# print(is_hometown('Alameda'))
# print(is_hometown('Palo Alto'))

"""PROMPT 2

Write a function that takes in a first and last name and returns a full name.

Examples:
    - 'Brighticorn', 'Hackbright' -> 'Brighticorn Hackbright'

Arguments:
    - First name (str)
    - Last name (str)

Return:
    - Full name (str)
"""

def make_full_name(first, last):

    return first + " " + last

# print(make_full_name("Omoefe", "Ogbeide"))


"""PROMPT 3

Write a function that prints a greeting.

If the person is from your hometown, print
    Hi <full name>, we're from the same place!

Otherwise, print
    Hi <full name>, I'd like to visit <town name>!

HINT: You can reuse the functions that you wrote in PROMPT 1 and Prompt 2.

Examples: (still assume my hometown is San Francisco)
    - 'Fido', 'Bark', 'Oakland' -> Hi Fido Bark, I'd like to visit Oakland!
    - 'Mel', 'M', 'San Francisco' -> Hi Mel M, we're from the same place!

Arguments:
    - First name (str)
    - Last name (str)
    - Hometown (str)
"""

def print_greeting(first, last, city):
    hometown = "Alameda"

    if city == hometown:
        print(f"Hi {first} {last}, we're from the same place!")

    else: 
        print(f"Hi {first} {last}, I'd like to visit {city}!")


# print_greeting("Omoefe", "Ogbeide", "Oakland")
# print_greeting("Omoefe", "Ogbeide", "Alameda")
# print_greeting("Rihanna", "Fenty", "Saint Michael Parish")

"""PROMPT 4

Write a function that returns True if a fruit is a berry.

Valid berries are:
    - strawberry
    - raspberry
    - blackberry
    - currant

Examples:
    - currant -> True
    - durian -> False

Arguments:
    - A fruit (str)

Return:
    - True or False (bool)
"""

def is_berry(fruit):
    """Checks to see if passed argument is a berry."""
    berries = ['strawberry', 'raspberry', 'blackberry', 'currant']

    return fruit in berries  

# print(is_berry('strawberry'))
# print(is_berry('mango'))
# print(is_berry('kiwi'))
# print(is_berry('blackberry'))


"""PROMPT 5

Write a function that returns the shipping cost of an item.

Berries cost $0 to ship. Everything else costs $5.

Arguments:
    - Something that needs to be shipped (str)

Return:
    - Shipping cost (int)
"""

def get_shipping_cost(item):
    """Get the shipping cost of an item"""

    berries = ['strawberry', 'raspberry', 'blackberry', 'currant']
       
    if item in berries:
        shipping_cost = 0

    else:
        shipping_cost = 5

    return shipping_cost

# print(get_shipping_cost('raspberry'))
# print(get_shipping_cost('car'))





"""PROMPT 6

Write a function that returns the total cost of something by applying
taxes and fees of various states.

States will be given as their two-letter abbreviations. For example,
California's abbreviation is 'CA'.

There are some states with special fees. All fees should be added to the new
subtotal *after* tax:
    - CA (California): add a 3% (0.03) tax for recycling
    - PA (Pennsylvania): add $2.00 safety fee
    - MA (Massachusettes):
        - add $1.00 for items with a base price of $100.00 or less
        - add $3.00 for items over $100.00

Arguments:
    - Base price (int)
    - Two-letter state abbreviation (str)
    - Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)

Return:
    - Total price after taxes and fees (float)
"""

def total_cost_taxes_and_fees(base_price, state_abr, tax_percentage=.05):
    """ Base price (int)
    - Two-letter state abbreviation (str)
    - Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)"""
    addtl_tax = 0
    fees = 0
    # base_cost = base_price + (base_price * tax_percentage)
    # total_cost = base_cost + (base_cost*addtl_tax) + fees

    if state_abr == 'CA':
        addtl_tax = .03
        base_cost = base_price + (base_price * tax_percentage)
        total_cost = base_cost + (base_cost * addtl_tax) + fees
        return total_cost
        # (f"CA total_cost {total_cost}")

    elif state_abr == 'PA':
        fees = 2.00
        base_cost = base_price + (base_price * tax_percentage)
        total_cost = base_cost + (base_cost * addtl_tax) + fees
        return total_cost
        # (f"PA total_cost {total_cost}")

    elif state_abr == 'MA':
        if base_price <= 100:
            fees = 1
            base_cost = base_price + (base_price * tax_percentage)
            total_cost = base_cost + (base_cost*addtl_tax) + fees
        else:
            fees = 3
            base_cost = base_price + (base_price * tax_percentage)
            total_cost = (base_cost + (base_cost*addtl_tax)) + fees
        return total_cost
        # (f"MA total_cost {total_cost}")

    else:
        base_cost = base_price + (base_price * tax_percentage)
        total_cost = base_cost + (base_cost*addtl_tax) + fees
        return total_cost
        # (f"Other total_cost {total_cost}")


# print(total_cost_taxes_and_fees(100, 'CA', .07))
# print(total_cost_taxes_and_fees(100, 'MA', .07))
# print(total_cost_taxes_and_fees(99, 'MA', .07))
# print(total_cost_taxes_and_fees(100, 'PA', .08))
# print(total_cost_taxes_and_fees(100, 'HI', .08))


# # print(total_cost_taxes_and_fees(100, 'CA', .08))
# # print(total_cost_taxes_and_fees(100, 'PA', .04))
# print(total_cost_taxes_and_fees(100, 'LA',))
# # print(total_cost_taxes_and_fees(100, 'HI', .09))




"""PROMPT 7

Write a function that takes in a list and *any* number of additional arguments.
The function should add all those items to the end of the  list and return
the list.

We haven't taught you how to do this! You'll need to do some research on your
own --- find a way to write a Python function that can take in an arbitrary
amount of arguments.

Arguments:
    - A list (list)
    - Additional args

Return:
    - A list with arguments added to the end (list)
"""

def add_to_list(items_list, *args):
        
    for arg in args:
        items_list.append(arg)

    return items_list

# print(add_to_list(['a','b','c'],'d', 'e', 'f'))

"""PROMPT 8

Write a function that takes in a word and returns a tuple. You'll do this in an
interesting way though, so make sure you read these directions thoroughly.

The tuple will contain two items:
    - The given word
    - The given word, multiplied 3 times

To do this, your function will create an *inner* function. The *inner*
function will multiply the given word by 3 and return it.

Then, the outer function will call the *inner* function to create a tuple.

Examples:
    - 'hi' -> ('hi', 'hihihi')

Arguments:
    - A word (str)

Return:
    - (word, wordx3) (tuple)
"""
def word_tripleword_tuple(given_word):
    # return (word, word * 3)
    word = given_word
    
    def inner_function(word):
        return word * 3
    
    def outer_function():
        return (word, inner_function(word))
    return outer_function()


# print(word_tripleword_tuple('hi'))