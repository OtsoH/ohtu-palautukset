class Komento:
    def suorita(self):
        pass

    def kumoa(self):
        pass


class Summa(Komento):
    def __init__(self, sovelluslogiikka, lue_arvo):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_arvo = lue_arvo
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        arvo = int(self._lue_arvo())
        self._sovelluslogiikka.plus(arvo)

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)


class Erotus(Komento):
    def __init__(self, sovelluslogiikka, lue_arvo):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_arvo = lue_arvo
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        arvo = int(self._lue_arvo())
        self._sovelluslogiikka.miinus(arvo)

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)


class Nollaus(Komento):
    def __init__(self, sovelluslogiikka, lue_arvo):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_arvo = lue_arvo
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)


class Kumoa(Komento):
    def __init__(self, sovelluslogiikka, lue_arvo):
        pass

    def suorita(self):
        pass

    def kumoa(self):
        pass