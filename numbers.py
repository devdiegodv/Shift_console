def perfumery_numbers():
    """
    Generator function for perfumery numbers.

    Yields: str
        Strings representing perfumery numbers in the format "P - {n}" where n is in the range 1 to 9999.
    """
    for n in range(1, 10000):
        yield f"P - {n}"

def pharmacy_numbers():
    """
    Generator function for pharmacy numbers.

    Yields: str
        Strings representing pharmacy numbers in the format "F - {n}" where n is in the range 1 to 9999.
    """
    for n in range(1, 10000):
        yield f"F - {n}"

def costemetics_numbers():
    """
    Generator function for cosmetics numbers.

    Yields: str
        Strings representing cosmetics numbers in the format "C - {n}" where n is in the range 1 to 9999.
    """
    for n in range(1, 10000):
        yield f"C - {n}"

p = perfumery_numbers()
ph = pharmacy_numbers()
c = costemetics_numbers()

def decorator(category):
    """
    Decorator function that prints a message with the category and the next number in the corresponding sequence.

    Parameters:
        category (str): A string representing the category ('P' for perfumery, 'PH' for pharmacy, or any other for cosmetics).
    """
    print('\n' + '*' * 23)
    print('Your number is: ')

    if category == 'P':
        print(next(p))
    elif category == 'PH':
        print(next(ph))
    else:
        print(next(c))
    print('Wait and you will be attended')
    print('*' * 23 + '\n')