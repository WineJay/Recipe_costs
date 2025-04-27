import pandas
import math


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


def int_check(question):
    """checks that the user enter an integer. """

    error = "Oops - please enter an integer. "

    while True:
        try:
            # Return the response if it's an integer
            response = int(input(question))
            return response

        except ValueError:
            print(error)


def instructions():
    make_statement("Instructions", "ℹ️")
    """Instructions for using Recipe Cost Calculator"""

    print('''

For each recipe enter...
- Ingredient name
- The amount
- How much did you buy?
- Price for one

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
    amount = num_check(f"How much are you using (in grams or no unit): ")

    brought = num_check(f"How much did you buy (also in grams or no units): ")

    price = num_check(f"How much did you pay?: ")

    # output error message / success message
    if brought < amount:
        print(f"You haven't brought enough")
        break

    # find how much per serving for each ingredient
    each_ingredient_per_dollar = (price / brought)

    # calculate the total spend
    print(f"You have brought ingredient worth of", each_ingredient_per_dollar * amount, f"(It is calculated on per "
                                                                                        f"item or gram per  dollar)")
    print()

