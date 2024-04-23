stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Compute the total price of each item
total_price_by_item = {item: stock[item] * prices[item] for item in stock}

print(total_price_by_item)