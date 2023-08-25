def numeric_check(variable_input):
    try:
        int(variable_input)
    except ValueError:
        return False
    else:
        return True


def positive_check(variable_input):
    try:
        int(variable_input)
    except ValueError:
        return False
    except TypeError:
        return False
    else:
        if int(variable_input) > 0:
            return True
        else:
            return False


def player_check(player_1, player_2, player_entered):
    if player_1 == player_entered:
        return True
    elif player_2 == player_entered:
        return True
    else:
        return False


def allowed_check(variable_input):
    allowed = [1, 2, 3]
    try:
        variable_input = int(variable_input)
    except ValueError:
        return False
    if int(variable_input) in allowed:
        return True
    else:
        return False

import random

player_1 = "John"
player_2 = "Jack"
pencils = input("How many pencils would you like to use:\n")
# Numeric / Positive check for pencils.
pencils_numeric = numeric_check(pencils)
pencils_positive = positive_check(pencils)


while (not pencils_numeric) or (not pencils_positive):
    while not pencils_numeric:
        pencils = input("The number of pencils should be numeric\n")
        pencils_numeric = numeric_check(pencils)
        pencils_positive = positive_check(pencils)

    while pencils_numeric and (not pencils_positive):
        pencils = input("The number of pencils should be positive\n")
        pencils_numeric = numeric_check(pencils)
        pencils_positive = positive_check(pencils)
pencils = int(pencils)


starter = input("Who will be the first (John, Jack):\n")
# Check if first players name is input correctly.
starter_correct = player_check(player_1, player_2, starter)

while not starter_correct:
    starter = input(f"Choose between '{player_1}' and '{player_2}'\n")
    starter_correct = player_check(player_1, player_2, starter)


while True:
    if starter == player_1:
        remove = input("|" * pencils + f"\n{starter}'s turn!\n")
        remove_numeric = numeric_check(remove)
        remove_allowed = allowed_check(remove)
        while (not remove_numeric) or (not remove_allowed):
            remove = input("Possible values: '1', '2' or '3'\n")
            remove_numeric = numeric_check(remove)
            remove_allowed = allowed_check(remove)
            # The block above only checks if the input value is allowed (int and 1-3)
        remove = int(remove)

        while pencils - remove < 0:
            remove = input(f"Too many pencils were taken\n")
            remove_numeric = numeric_check(remove)
            remove_allowed = allowed_check(remove)
            while (not remove_numeric) or (not remove_allowed):
                remove = input("Possible values: '1', '2' or '3'\n")
                remove_numeric = numeric_check(remove)
                remove_allowed = allowed_check(remove)
            remove = int(remove)
    else:
        for i in range(1, 4):
            if pencils in list(range(1, pencils + 1))[i::4]:
                remove = i
        if pencils in list(range(1, pencils + 1))[4::4]:
            remove = random.randrange(1, 3)
        if pencils == 1:
            remove = 1
        print("|" * pencils + f"\n{starter}'s turn:\n{remove}")

    if pencils - remove == 0:
        if starter == player_1:
            starter = player_2
        else:
            starter = player_1
        print(f"{starter} wins!")
        break
    elif pencils - remove > 0:
        pencils -= remove

    if starter == player_1:
        starter = player_2
    else:
        starter = player_1

