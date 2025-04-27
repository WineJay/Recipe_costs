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

# main routine Goes here


# loop for testing purposes
while True:
    recipe_name = not_blank("Recipe Name: ")
    serving_size = num_check("Serving:", "integer")
    print(f"You are making {serving_size} {recipe_name}")
    print()
