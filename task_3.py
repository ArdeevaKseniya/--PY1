def get_random_password() -> str:

    import random
    import string
    amount_symbols = 8
    symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return random.sample(symbols, amount_symbols)


print("".join(get_random_password()))
