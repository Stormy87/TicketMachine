import json
from ticket import Ticket
from cart import Cart
from payment import Payment

class AutomatBiletowy:
    def __init__(self, cennik_file):
        self.cennik = self.wczytaj_cennik(cennik_file)
        self.koszyk = Cart()

    def wczytaj_cennik(self, plik):
        with open(plik, 'r', encoding='utf-8') as f:
            return json.load(f)

    def wyswietl_cennik(self):
        print("\nDostępne bilety:")
        for typ, kategorie in self.cennik.items():
            print(f"\n{typ.capitalize()}:")
            for kategoria, bilety in kategorie.items():
                print(f"  {kategoria.capitalize()}:")
                for nazwa, cena in bilety.items():
                    print(f"    {nazwa}: {cena} zł")

    def dodaj_do_koszyka(self):
        while True:
            typ = input("\nWybierz typ biletu (n - normalny, u - ulgowy): ").lower()
            if typ in ['n', 'u']:
                typ = 'normalny' if typ == 'n' else 'ulgowy'
                break
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

        kategorie = list(self.cennik[typ].keys())
        for i, kategoria in enumerate(kategorie):
            print(f"{i + 1}. {kategoria.capitalize()}")
        while True:
            wybor_kategorii = input("Wybierz kategorię biletu (cyfra): ")
            if wybor_kategorii.isdigit() and 1 <= int(wybor_kategorii) <= len(kategorie):
                kategoria = kategorie[int(wybor_kategorii) - 1]
                break
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

        bilety = list(self.cennik[typ][kategoria].keys())
        for i, bilet in enumerate(bilety):
            print(f"{i + 1}. {bilet} - {self.cennik[typ][kategoria][bilet]} zł")
        while True:
            wybor_biletu = input("Wybierz bilet (cyfra): ")
            if wybor_biletu.isdigit() and 1 <= int(wybor_biletu) <= len(bilety):
                nazwa = bilety[int(wybor_biletu) - 1]
                break
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

        bilet = Ticket(typ, kategoria, nazwa, self.cennik[typ][kategoria][nazwa])
        self.koszyk.add_ticket(bilet)
        print(f"\nDodano do koszyka: {nazwa} - {self.cennik[typ][kategoria][nazwa]} zł")

    def dokonaj_platnosci(self):
        total = self.koszyk.calculate_total()
        if Payment.process_payment(total):
            self.koszyk.clear_cart()

    def uruchom(self):
        while True:
            print("\n1. Wyświetl cennik")
            print("2. Dodaj bilet do koszyka")
            print("3. Pokaż koszyk")
            print("4. Dokonaj płatności")
            print("5. Wyjdź")
            wybor = input("Wybierz opcję (cyfra): ")

            if wybor == '1':
                self.wyswietl_cennik()
            elif wybor == '2':
                self.dodaj_do_koszyka()
            elif wybor == '3':
                self.koszyk.show_cart()
            elif wybor == '4':
                total = self.koszyk.calculate_total()
                if Payment.process_payment(total):
                    self.koszyk.clear_cart()
            elif wybor == '5':
                print("Dziękujemy za skorzystanie z automatu biletowego!")
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    automat = AutomatBiletowy('prices.json')
    automat.uruchom()