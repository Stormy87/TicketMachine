class Payment:
    def calculate_change(total, paid):
        return round(paid - total, 2)

    def process_payment(total):
        print(f"\nDo zapłaty: {total} zł")
        while True:
            try:
                paid = float(input("Podaj kwotę, którą płacisz: "))
                if paid >= total:
                    change = Payment.calculate_change(total, paid)
                    print(f"Transakcja zakończona. Twoja reszta: {change} zł")
                    return True
                else:
                    print("Podana kwota jest za mała. Spróbuj ponownie.")
            except ValueError:
                print("Nieprawidłowa kwota. Spróbuj ponownie.")