import random

MAX_ALLOWED_LINES = 3
MAX_ALLOWED_BIT = 100000
MIN_ALLOWED_BIT = 1

ROWS = 6
COLS = 3

# symbols that will be in the machine.
symbol_count = { 
                "A" : 2,
                "B" : 4,
                "C" : 6,
                "D" : 8}

#def make_machine_spin (rows, clos, symbols):



#Allowing user to enter balance
def request_deposit_balance():
    while True:
        amount = input("Who much would you like to depost? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount must be greater than zero.")
        else:
            print("Please provide a number.")
    return amount

# asking user for the number of lines they would like to bet on.
def request_number_of_lines():
    while True:
        lines  = input("Enter the number of lines to bet on (1-" + str(MAX_ALLOWED_LINES)+"): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_ALLOWED_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please provide a number.")
    return lines

# asking the user how much would they like to bet on each line.
def request_bet():
    while True:
        bet = input("Who much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_ALLOWED_BIT <= bet <= MAX_ALLOWED_BIT:
                break
            else:
                print(f"Your bet must best be between ${MIN_ALLOWED_BIT} - ${MAX_ALLOWED_BIT}.")
        else:
            print("Please provide a number.")
    return bet

def main():
    balance = request_deposit_balance()
    lines = request_number_of_lines()

    # making sure that the user is not betting more than there current balance
    while True:
     bet = request_bet() 
     total_betting = bet * lines

     if total_betting > balance:
        print (f"You do not have to bet ${bet}, your current balance is ${balance}")
     else:
        break

    print(f"You are betting ${bet} on {lines} lines.\nTotal bet = ${total_betting}")
main()

        

