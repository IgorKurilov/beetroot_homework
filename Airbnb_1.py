class Rental:
    def __init__(self, title, location, price_per_night, max_guests, amenities):
        self.title = title  # Назва помешкання
        self.location = location  # Розташування
        self.price_per_night = price_per_night  # Ціна за ніч
        self.max_guests = max_guests  # Максимальна кількість гостей
        self.amenities = amenities  # Зручності

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Location: {self.location}")
        print(f"Price per night: {self.price_per_night}")
        print(f"Max guests: {self.max_guests}")
        print(f"Amenities: {', '.join(self.amenities)}")

# Приклад використання:
rental1 = Rental("Cozy Apartment", "New York", 100, 4, ["Wi-Fi", "Kitchen", "TV"])
rental1.display_info()