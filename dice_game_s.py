from random import randint as randint


die_options = []

want_to_quit = False
want_to_change_die = True
want_throw_again = False

error_message = ""
input_not_resolved = True
mistake_was_made = False
acceptable_die_options = "0123456789"


def define_die():

    global die_options
    input_not_resolved = True

    while input_not_resolved:

        mistake_was_made = False
        die_options = input("Please enter all options on the die you would like to simulate, seperated by a comma: ").split(",")
        for options in die_options:
            for character in options:
                if character not in acceptable_die_options:
                    mistake_was_made = True

        if not mistake_was_made:
            input_not_resolved = False

        else:
            error_message = "Your die options aren't valid. Please try again."
            print(error_message)


def simulate_dice_roll (amount_of_throws):
    global die_options

    tally_result = []
    for option in die_options:
        tally_result.append(0)

    throw_result = []
    for times in range(amount_of_throws):
        throw_result.append(int(die_options[randint(0, len(die_options)-1)]))

    throw_result.sort()
    for result in throw_result:
        for option in range(len(die_options)):
            if result == int(die_options[option]):
                tally_result[option] += 1

    sorted_tally = tally_result[:]
    sorted_tally.sort()
    highest_amount = sorted_tally[-1]

    for option in range(len(die_options)):
        print(" "*(len(str(throw_result[-1]))-len(str(die_options[option]))) + die_options[option] + " |" + "*"*tally_result[option] + " "*(highest_amount-tally_result[option]) + "|" + str(tally_result[option]))


while not want_to_quit:

    if want_to_change_die:
        define_die()

    while input_not_resolved:
        mistake_was_made = False
        throws = input("Please enter the amount of times you would like to roll this die: ")
        for character in throws:
            if character not in "0123456789":
                mistake_was_made = True

        throws = int(throws)

        if not mistake_was_made and throws != 0:
            input_not_resolved = False

        else:
            error_message = "Your amount of throws is not a valid number. Please try again."
            print(error_message)

    input_not_resolved = True

    simulate_dice_roll(throws)

    while input_not_resolved:
        answer = input("Would you like to play again? (yes/no): ")
        if answer == "yes":
            want_throw_again = True
            input_not_resolved = False

        elif answer == "no":
            want_throw_again = False
            input_not_resolved = False

        else:
            error_message = "That's not a valid answer. Please try again."
            print(error_message)

    input_not_resolved = True

    if not want_throw_again:
        want_to_quit = True

    else:
        while input_not_resolved:
            answer = input("Would you like to change your die? (yes/no): ")
            if answer == "yes":
                want_to_change_die = True
                input_not_resolved = False

            elif answer == "no":
                want_to_change_die = False
                input_not_resolved = False

            else:
                error_message = "That's not a valid answer. Please try again."
                print(error_message)

        input_not_resolved = True
