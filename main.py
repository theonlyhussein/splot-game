import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 4
COLS = 3

# Define the count of each symbol in the slot machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#Define the value of each symbol in the slot machine
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

"""
    Check the winnings and winning lines based on the slot machine columns.
    Args:
        columns (list): Columns of the slot machine.
        lines (int): Number of lines to bet on.
        bet (int): Bet amount on each line.
        values (dict): Symbol values in the slot machine.

    Returns:
        tuple: A tuple containing the total winnings and the list of winning lines.
"""
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        if all(column[line] == symbol for column in columns):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

"""
    Generate a random spin of the slot machine.
    Args:
        rows (int): Number of rows in the slot machine.
        cols (int): Number of columns in the slot machine.
        symbols (dict): Symbol counts in the slot machine.

    Returns:
        list: Columns of the slot machine spin.
"""
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [symbol for symbol, count in symbols.items() for _ in range(count)]
    columns = [[random.choice(all_symbols) for _ in range(rows)] for _ in range(cols)]
    return columns

"""
    Print the slot machine layout.
    Args:
        columns (list): Columns of the slot machine.
"""
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        print(' | '.join(column[row] for column in columns))

"""
    Prompt the user to enter the deposit amount.
    Returns:
        int: The deposit amount.
 """
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print("Amount must be greater than 0.")

"""
    Prompt the user to enter the number of lines to bet on.
    Returns:
        int: The number of lines.
"""
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            return int(lines)
        print("Enter a valid number of lines.")

"""
    Prompt the user to enter the bet amount.
    Returns:
        int: The bet amount.
"""
def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? $")
        if amount.isdigit() and MIN_BET <= int(amount) <= MAX_BET:
            return int(amount)
        print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")

"""
    Perform a spin of the slot machine.
    Args:
        balance (int): Current balance.

    Returns:
        int: The difference between the total winnings and the total bet amount.
"""
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

"""
    Main function to run the slot machine game.
"""
if __name__ == "__main__":
    main()