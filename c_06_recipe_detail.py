import pandas


# Functions go here

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


# dictionary
all_paid = []
all_ingredient = []

recipe_detail_dict = {
    'total spend': all_paid,
    'Ingredient': all_ingredient
}



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

    all_paid.append(price)

    # find how much per serving for each ingredient
    ingredient_cost = (price / brought) * amount

    # calculate the total spend
    print(f"You have brought ingredient worth of", ingredient_cost, f"(It is calculated on per "
                                                                    f"item or gram per  dollar)")
# panda
recipe_details_frame = pandas.DataFrame(recipe_detail_dict)

# total
total_paid = recipe_details_frame['total spend'].sum()

print(recipe_details_frame.to_string(index=False))
print()
print(F"you have spend: ${total_paid:.2f}")
