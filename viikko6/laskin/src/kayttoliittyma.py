from tkinter import ttk, constants, StringVar
from komennot import Summa, Erotus, Nollaus, Kumoa


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._edellinen_komento = None

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento("Summa")
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento("Erotus")
        )

        nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            command=lambda: self._suorita_komento("Nollaus")
        )

        kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            command=lambda: self._suorita_komento("Kumoa")
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        nollaus_painike.grid(row=2, column=2)
        kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento_nimi):
        if komento_nimi == "Kumoa":
            if self._edellinen_komento:
                self._edellinen_komento.kumoa()
                self._edellinen_komento = None
        else:
            komento_luokat = {
                "Summa": Summa,
                "Erotus": Erotus,
                "Nollaus": Nollaus
            }

            komento = komento_luokat[komento_nimi](
                self._sovelluslogiikka,
                self._lue_syote
            )
            komento.suorita()
            self._edellinen_komento = komento

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovelluslogiikka.arvo())


