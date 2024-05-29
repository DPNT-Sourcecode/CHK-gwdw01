import re

base_prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

discounts = {
    "A": {
        "count": 3,
        "price": 130
    },
    "B": {
        "count": 2,
        "price": 45
    }
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    valid_string_re = re.compile("[ABCD]+")
    if not valid_string_re.fullmatch(skus):
        return -1



