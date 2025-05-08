# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """checks that the user enter th full word
    or the first letter of a word from a list of valid response"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")

    # main routine goes here


def instructions():
    make_statement("Instructions", "ℹ️")
    """Instructions for using Recipe Cost"""

    print('''

    For each recipe enter...
    - Ingredient name
    - The amount
    - The units
    - How much did you buy?
    - The unit brought
    - Price you paid

    After entering the ingredient and amount, you may enter any units for the first one. But the last one, you need to put 
    either the same units or use units such as kilo or kg after using grams or g. Or, if you entered mL first, make sure the 
    last one is also mL or L. If you put larger unit first and then an unit which is small, the programme will have an error
    and won't calculate the right price just like any other calculator.  

    The program will first record the price you spent on the ingredient then the total spent then at last ingredient per 
    serving.

    Once you have entered the exit code ('xxx'), the program will display the ingredient
    information and the total cost.

        ''')


# Main Routine goes here

# Ask user if they want to see the instructions and display them if necessary

make_statement("Recipe Cost Calculator", "🍳")

print()
want_instructions = string_check("Do you want to see the instructions?")
if want_instructions == "yes":
    instructions()

print()
print("program continues...")
