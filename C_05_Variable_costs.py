import pandas


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def num_check(question, num_type="float", exit_code=None):
    """checks that the user enter th full word
    or the first letter of a word from a list of valid response"""

    if num_type == "integer":
        error = "Oops - please enter an integer more than zero."
        change_to = int
    else:
        error = "Oops - please enter a number more than zero."
        change_to = float
    while True:

        response = input(question)

        # check for the exit code
        if response == exit_code:
            return response

        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def get_expenses(exp_type, how_many):
    """Gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # lists for pandas
    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    # Expenses Dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item

    }

    # default amount to 1 for fixed expenses and to avoid PEP 8 error for variable expenses
    amount = 1

    # loop to get expenses
    while True:
        # get item name and check it's not blank
        item_name = not_blank("Ingredient Name: ")

        # check users enters at least one variable NOTE: if the conditions without the brackets are all in one line
        # and adds to the center the system will add brackets automatically
        if (exp_type == "variable" and item_name == "xxx") \
                and len(all_items) == 0:
            print("Oops - You have not entered anything. "
                  "You need at least one item. ")
            continue

        elif item_name == "xxx":
            break

        # get ingredient amount <enter. default to number of products being made

        amount = num_check(f"How much being used <enter for {how_many}>: ",
                           "integer", "")

        if amount == "":
            amount = how_many
        # get ingredients that was brought
        brought = num_check(f"How much did you buy?", "integer", "")

        if brought == "":
            brought = how_many

        cost = num_check("Price for one?", "float")

        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(cost)

    # make panda
    expense_frame = pandas.DataFrame(expenses_dict)

    # calculate the row cost
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    subtotal = expense_frame['Cost'].sum()

    # return all items for now so we can check the loop
    return expense_frame, subtotal


# Main routine goes here

quantity_made = num_check("Quantity being made: ",
                          "integer")

# print("Getting Variable cost...") (from c_04_expensive loop)
# variable_expenses = get_expenses("variable")
# num_variable = len(variable_expenses)
# print(f"You entered {num_variable} items")
print()

print("Getting Recipe Details..")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print(variable_panda)
print(variable_subtotal)
