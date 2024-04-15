# writen by Igor Kurilov
import utils

def main_menu():
    while True:
        print("\nОберіть потрібне:")
        print("1 - Показати усі книжки")
        print("2 - Додати нову книжку")
        print("3 - Випадково вибрати книжку")
        print("0 - Вийти з довідника")

        choice = input("Зробить Ваш вибір: ")

        if choice == "1":
            utils.view_books()
        elif choice == "2":
            utils.add_book()
        elif choice == "3":
            utils.random_book()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Введіть коректне значення.")

if __name__ == "__main__":
    main_menu()