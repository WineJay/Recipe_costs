from typing import Any

import pandas

from tabulate import tabulate


# Functions go here

def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def num_check(question, num_type="float"):
    """checks that the user enter th full word
    or the first letter of a word from a list of valid response"""

    if num_type == "float":
        error = "Please enter an number more than 0"
    else:
        error = "Please enter an integer more than 0"

    while True:
        try:

            if num_type == "float":
                response = float(input(question))
            else:
                response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def instructions():
    make_statement("Instructions", "ℹ️")
    """Instructions for using Recipe Cost Calculator"""

    print('''

    For each recipe enter...
    - Ingredient name
    - The amount
    - The units
    - How much did you buy?
    - The unit brought
    - Price you paid

    After entering the amount and the units of that amount you are going to use. You can use either the same units 
    or the units which smaller or larger. An good example would be using kilo but brought grams. Or using kilogram and 
    brought grams. However you use it make sure to add the price you paid for brought. This will calculate the correct 
    amount. The program will accept <blank> for units too as some ingredients may not have any.
    
    The units that the program will accept are kg, kilo, g, grams, mL, ml, l, L.

    The program will first record the price you spent on the ingredient then the total spent then at last ingredient per 
    serving.

    Once you have entered the exit code ('xxx'), the program will display the ingredient
    information and the total cost.

        ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """checks that the user enter th full word
    or the first letter of a word from a list of valid response"""

    while True:

        response = input(question).lower()

        for entry in valid_answers:

            # check if the response is the entire word
            if response == entry:
                return entry

            # check if it's the first letter
            elif response == entry[:num_letters]:
                return entry

        print(f"Please choose an option from {valid_answers}")


def unit_check(question, valid_answers= ('kg', 'kilo', 'g', 'grams', 'mL', 'l', 'ml', '', 'L')) -> str | Any:
    """ checks the units the user has entered
    this also helps the calculator to do calculation such as Grams to kilograms.
        """
    while True:

        response = input(question).lower()

        for entry in valid_answers:

            # check if the response is the entire word
            if response == entry:
                return entry


def currency(x):
    """formats number as currency ($#,##)"""
    return "${:.2f}".format(x)

# recipe cost dictionary
all_ingredient = []
all_used = []
all_used_unit = []
all_brought = []
all_brought_unit = []
all_buy = []
all_worth = []

recipe_cost_dict = {
    "Ingredient": all_ingredient,
    "Used": all_used,
    "Units": all_used_unit,
    "Brought": all_brought,
    ".Units.": all_brought_unit,
    "Price": all_buy,
    "Worth": all_worth
}

# main routine Goes here
make_statement(f"Recipe Cost", "🍳")
print()

want_instructions = string_check("Do you want to see the instructions?")
if want_instructions == "yes":
    instructions()

# loop for testing purposes

recipe_name = not_blank("Recipe Name: ")
serving_size = num_check("Serving:", "integer")
print(f"You are making {serving_size} {recipe_name}")
print()
while True:
    ingredient = not_blank(f"Ingredient: ")
    # if name is exit code, break out of loop
    if ingredient == "xxx":
        break

        # using units
    amount = num_check(f"How much are you using: ")

    units_used = unit_check(f"What is your units for this ingredient: ")

    brought = num_check(f"How much did you buy : ")

    units_brought = unit_check(f"What is your units for this: ")

    price = num_check(f"How much did you pay?: $ ")

    # find how much per serving for each ingredient
    each_ingredient_per_dollar = (price / brought)

    if  units_used == "kg":
        each_ingredient_per_dollar = ((price / brought) * 1000)

    if  units_used == "kilo":
        each_ingredient_per_dollar = ((price / brought) * 1000)

    if  units_used == "l":
        each_ingredient_per_dollar = ((price / brought) * 1000)

    if  units_used == "L":
        each_ingredient_per_dollar = ((price / brought) * 1000)

    if units_brought == "kg":
        each_ingredient_per_dollar = (price / (brought * 1000))

    if units_brought == "kilo":
        each_ingredient_per_dollar = (price / (brought * 1000))

    if units_brought == "L":
        each_ingredient_per_dollar = (price / (brought * 1000))

    if units_brought == "l":
        each_ingredient_per_dollar = (price / (brought * 1000))

    if units_brought == units_used:
        each_ingredient_per_dollar = (price / brought)

    print(f"You have got ingredient worth of ${(each_ingredient_per_dollar * amount):.2f}")
    print()

    # appends to add items along with
    all_ingredient.append(ingredient)
    all_used.append(amount)
    all_used_unit.append(units_used)
    all_brought.append(brought)
    all_brought_unit.append(units_brought)
    all_buy.append(price)
    all_worth.append(each_ingredient_per_dollar * amount)
# using the pandas
recipe_cost_frame = pandas.DataFrame(recipe_cost_dict)
# calculate total spent and worth
recipe_cost_string = (recipe_cost_frame.to_string(index=False))

total_paid = recipe_cost_frame['Price'].sum()
total_using = recipe_cost_frame['Worth'].sum()
per_serving = total_using / serving_size

# apply currency formatting to currency columns.
add_dollars = ['Price', 'Worth']
for var_item in add_dollars:
    recipe_cost_frame[var_item] = recipe_cost_frame[var_item].apply(currency)


# print area
print()
make_statement(f"Let's Calculate the totals!", "-")

# printing with tabulate for better looks
print(tabulate(recipe_cost_frame[['Ingredient', 'Used', 'Units', 'Brought', '.Units.', 'Price', 'Worth']],
               headers='keys',
               tablefmt="fancy_grid", showindex=False))
print()
# totals of ingredient cost, worth, and per serving
print(f"Total to shop for these ingredients: ${total_paid:.2f}")
print(f"You are using ingredient worth a total of: ${total_using:.2f}")
print(f"Per serving it would cost you: ${per_serving:.2f}")

print()
