class Rental:
    def __init__(self, title, location, price_per_night, max_guests, amenities):
        self.title = title  # Назва помешкання
        self.location = location  # Розташування
        self.price_per_night = price_per_night  # Ціна за ніч
        self.max_guests = max_guests  # Максимальна кількість гостей
        self.amenities = amenities  # Зручності
        self.bookings = []  # Список бронювань

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Location: {self.location}")
        print(f"Price per night: {self.price_per_night}")
        print(f"Max guests: {self.max_guests}")
        print(f"Amenities: {', '.join(self.amenities)}")

    def book(self, guest_name, start_date, end_date):
        # Перевірка наявності вільних дат
        for booking in self.bookings:
            if start_date <= booking['end_date'] and end_date >= booking['start_date']:
                print("Ці дати вже заброньовані.")
                return False
        # Додавання бронювання
        self.bookings.append({
            'guest_name': guest_name,
            'start_date': start_date,
            'end_date': end_date
        })
        print("Бронювання успішно здійснено.")
        return True

# Приклад використання:
rental1 = Rental("Cozy Apartment", "New York", 100, 4, ["Wi-Fi", "Kitchen", "TV"])
rental1.display_info()

# Бронювання помешкання
rental1.book("John Doe", "2024-05-10", "2024-05-15")