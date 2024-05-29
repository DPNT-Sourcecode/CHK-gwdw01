import re

base_prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}

discounts = {
    "A": [{
        "count": 5,
        "price": 200
    }, {
        "count": 3,
        "price": 130,
    }],
    "B": [{
        "count": 2,
        "price": 45
    }],
    "H": [{
        "count": 10,
        "price": 80
    }, {
        "count": 5,
        "price": 45
    }],
"K": [{
        "count": 2,
        "price": 45
    }],
}

bogos = {
    "E": {
        "count": 2,
        "discount": "B"
    },
    "F": {
        "count": 3,
        "discount": "F"
    }
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus == "":
        return 0

    valid_string_re = re.compile("[ABCDEF]+")
    if not valid_string_re.fullmatch(skus):
        return -1

    counts = {}
    result = 0

    for char in skus:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for bogo in bogos:
        bogo_count = counts.get(bogo, 0)
        free_items = bogo_count // bogos[bogo]["count"]
        items_left = max(0, counts.get(bogos[bogo]["discount"], 0) - free_items)

        counts[bogos[bogo]["discount"]] = items_left

    for sku in counts:
        if discounts.get(sku) is not None:
            discount_arr = discounts[sku]

            for discount_elem in discount_arr:
                item_bulk = counts[sku] // discount_elem["count"]
                if item_bulk != 0:
                    result += item_bulk * discount_elem["price"]
                    counts[sku] -= item_bulk * discount_elem["count"]

        result += counts[sku] * base_prices[sku]

    return result
