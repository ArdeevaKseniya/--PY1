import random
import string


def get_random_password() -> str:

    amount_symbols = 8
    symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return random.sample(symbols, amount_symbols)


print("".join(get_random_password()))
# Последняя строка