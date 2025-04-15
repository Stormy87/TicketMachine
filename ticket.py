class Ticket:
    def __init__(self, typ, kategoria, nazwa, cena):
        self.typ = typ
        self.kategoria = kategoria
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        return f"{self.typ.capitalize()} - {self.kategoria.capitalize()} - {self.nazwa}: {self.cena} zł"