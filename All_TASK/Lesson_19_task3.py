class MyIterable:
    def __init__(self, *args):
        self.elements = list(args)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.elements):
            result = self.elements[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.elements[index]

# Example usage:
my_iterable = MyIterable(1, 2, 3, 4, 5)

# Using in for-in loop
for item in my_iterable:
    print(item)

# Retrieving elements using square brackets syntax
print(my_iterable[2])  # Output: 3
