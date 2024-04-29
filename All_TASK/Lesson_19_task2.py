def in_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0
    
    current = start
    while (step > 0 and current < end) or (step < 0 and current > end):
        yield current
        current += step

# Example usage:
for num in in_range(5):
    print(num)

for num in in_range(1, 10, 2):
    print(num)
