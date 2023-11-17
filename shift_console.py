import numbers

def ask():
    """
    Function to prompt the user to choose a category (Perfumery, Pharmacy, or Cosmetics).
    It uses a while loop to ensure a valid category is selected.
    After a valid category is chosen, it calls the decorator function from the 'numbers' module.
    """
    print('Welcome to the Pharmacy')

    while True:
        print('[P] - Perfumery\n[PH] - Pharmacy\n[C] - Cosmetics')
        try:
            my_category = input('Choose your category: ').upper()
            ['P', 'PH', 'C'].index(my_category)
        except ValueError:
            print('That is not a valid option')
        else:
            break
    
    numbers.decorator(my_category)

def start():
    """
    Function to start the interaction with the user.
    It repeatedly calls the 'ask' function and asks the user if they want to take another turn.
    If the user chooses not to take another turn, the loop breaks, and a farewell message is printed.
    """
    while True:
        ask()
        try:
            another_turn = input('Do you want to take another turn? [Y] or [N]: ').upper()
            ['Y', 'N'].index(another_turn)
        except ValueError:
            print('That is not a valid option')
        else:
            if another_turn == 'N':
                print('Thanks for visiting')
                break

start()