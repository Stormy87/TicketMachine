class Cart:
    def __init__(self):
        self.items = []

    def add_ticket(self, ticket):
        self.items.append(ticket)
        print(f"\nDodano do koszyka: {ticket}")

    def show_cart(self):
        if not self.items:
            print("\nKoszyk jest pusty.")
        else:
            print("\nKoszyk:")
            for ticket in self.items:
                print(ticket)

    def clear_cart(self):
        self.items.clear()
        print("\nKoszyk został opróżniony.")

    def calculate_total(self):
        return sum(ticket.cena for ticket in self.items)