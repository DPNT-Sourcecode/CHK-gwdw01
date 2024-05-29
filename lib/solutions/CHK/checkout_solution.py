import re

base_prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

discounts = {
    "A": [{
        "count": 3,
        "price": 130
    }, {
        "count": 5,
        "price": 200,
    }],
    "B": {
        "count": 2,
        "price": 45
    }
}

bogos = {
    "E": {
        "count": 2,
        "discount": "B"
    }
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    valid_string_re = re.compile("[ABCDE]*")
    if not valid_string_re.fullmatch(skus):
        return -1

    counts = {}
    result = 0

    for char in skus:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for sku in counts:
        count = counts[sku]

        if sku == "A":
            a_bulks = count // 3
            result += a_bulks * 130
            a_remainder = count % 3
            result += a_remainder * 50
        elif sku == "B":
            a_bulks = count // 2
            result += a_bulks * 45
            a_remainder = count % 2
            result += a_remainder * 30
        elif sku == "C":
            result += count * 20
        elif sku == "D":
            result += count * 15

    return result





