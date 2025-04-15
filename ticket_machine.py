import json


def load_prices():
    try:
        with open('prices.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Nie znaleziono pliku 'prices.json'.")
        exit()


def display_prices(prices):
    print("\nDostępne bilety:")
    for category, ticket_types in prices.items():
        print(f"\n{category.capitalize()}:")
        for ticket_type, options in ticket_types.items():
            print(f"  {ticket_type.capitalize()}:")
            for option, price in options.items():
                print(f"    {option.capitalize()}: {price:.2f} zł")

def get_choice(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        print("Nieprawidłowy wybór, spróbuj ponownie.")


def ticket_machine():
    prices = load_prices()
    cart = []
    total = 0.0

    while True:
        display_prices(prices)
        category = get_choice("Wybierz kategorię (normalny/ulgowy) lub 'k' aby zakończyć: ", ["normalny", "ulgowy", "k"])
        if category == 'k':
            break

        ticket_type = get_choice("Wybierz typ biletu (okresowy/czasowy/jednorazowy): ", ["okresowy", "czasowy", "jednorazowy"])
        options = list(prices[category][ticket_type].keys())
        option = get_choice(f"Wybierz opcję biletu ({'/'.join(options)}): ", options)
        ticket_price = prices[category][ticket_type][option]
        cart.append((category, ticket_type, option, ticket_price))
        total += ticket_price
        print(f"Dodano {option} bilet ({ticket_type}, {category}) za {ticket_price:.2f} zł. Suma: {total:.2f} zł.")

    if cart:
        print("\nKoszyk:")
        for item in cart:
            print(f"- {item[2].capitalize()} bilet ({item[1]}, {item[0]}): {item[3]:.2f} zł")
        print(f"Łączna kwota do zapłaty: {total:.2f} zł")

        payment_method = get_choice("Wybierz metodę płatności (gotówka/karta): ", ["gotówka", "karta"])
        if payment_method == "gotówka":
            while True:
                try:
                    cash = float(input("Podaj kwotę: "))
                    if cash >= total:
                        change = cash - total
                        print(f"Reszta: {change:.2f} zł. Dziękujemy za zakup!")
                        break
                    else:
                        print("Kwota niewystarczająca, spróbuj ponownie.")
                except ValueError:
                    print("Nieprawidłowa wartość, spróbuj ponownie.")
        else:
            print("Płatność kartą przyjęta. Dziękujemy za zakup!")

if __name__ == "__main__":
    ticket_machine()