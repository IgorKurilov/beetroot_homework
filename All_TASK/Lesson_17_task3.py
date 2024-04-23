class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def _simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    # Test addition
    result_addition = x + y
    print(result_addition)  # Output: 3/4

    # Test subtraction
    result_subtraction = x - y
    print(result_subtraction)  # Output: 1/4

    # Test multiplication
    result_multiplication = x * y
    print(result_multiplication)  # Output: 1/8

    # Test division
    result_division = x / y
    print(result_division)  # Output: 2/1 or 2.0 (float)

    # Test equality
    print(x + y == Fraction(3, 4))  # Output: True
