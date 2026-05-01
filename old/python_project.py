"""https://youtu.be/th4OBktqK1I?si=ayjqQMrJdL_F2z4Q"""

import random

"""These global constants are used here so that when we want to change the number, 
it can be done here easily."""

MAX_LINES = 3  # Global Constant. 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 8,
    "B" : 5,
    "C" : 2,
    "D" : 6
}  

symbol_value = {
    "A" : 9,
    "B" : 2,
    "C" : 8,
    "D" : 4
}  

def check_winnings(columns, lines, bet, values):
    """This is for checking if the symbols match and calculates the winnings for each bet."""

    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) # +1 because LINE is index.

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """This is for specifying the functions of the slot machine."""

    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # This slice, creates a copy
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")

        print()

def deposit(): 
    """For collecting user input deposit amount"""
    
    while True:
        amount = input("How much would you like to deposit? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    """For collecting the number of lines the user wants to bet."""

    while True:
        lines = input("Enter the no.of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    """For collecting the amount of money they would like to bet."""

    while True:
        amount = input("How much would you like to bet on each line? ₹")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ₹{MIN_BET} and ₹{MAX_BET}")
        else:
            print("Please enter a number.")
    
    return amount

def spin(balance):
    lines = get_number_of_lines()

    while True: # Here we write some functions for checking some rules.
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough amount to bet, current balance - ₹{balance}")

        else:
            break

    print(f"You are betting ₹{bet} on {lines}. Total bet : ₹{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ₹{winnings}")
    print(f"You won on lines: ", *winning_lines) #unpack operator

    return winnings - total_bet

def main():
    """This is to combine all the functions and run the project as one."""

    balance = deposit()
    while True:
        print(f"Current balance is ₹{balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ₹{balance}")
    

main()  