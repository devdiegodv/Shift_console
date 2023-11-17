import numbers

def ask():
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