# Here taking the input (tree length) from the user
tree_length = int(input("Give me the tree length you want to display: "))


def print_stars(amount_stars):
    for i in range(amount_stars):
        print("*", end="")


def print_spaces(amount_spaces):
    for i in range(amount_spaces):
        print(" ", end="")


def display(tree_length):
    # initialize the stars with 1
    amount_stars = 1

    for i in range(tree_length):  # for length 5
        print_spaces(tree_length - i - 1)  # 5 - 0 - 1 = 4 spaces
        print_stars(amount_stars)  # prints 1 star
        print()  # return to line (by def it returns)
        amount_stars += 2  # incremente the amount by 2 each iteration


display(tree_length)  # revoke the function
