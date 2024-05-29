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
        "count": 5,
        "price": 200
    }, {
        "count": 3,
        "price": 130,
    }],
    "B": [{
        "count": 2,
        "price": 45
    }]
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
    if skus == "":
        return 0

    valid_string_re = re.compile("[ABCDE]+")
    if not valid_string_re.fullmatch(skus):
        return -1

    counts = {}
    result = 0

    for char in skus:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    e_count = counts["E"]
    free_bs = e_count // 2
    bs_left = max(0, counts["B"] - free_bs)

    counts["B"] = bs_left

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


