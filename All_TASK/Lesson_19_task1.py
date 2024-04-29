def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

# Example usage:
items = ['apple', 'banana', 'cherry']
for index, item in with_index(items, 1):
    print(index, item)
