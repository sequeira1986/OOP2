class Zvierat:
    def hlas(self):
        pass

    def pocet(self):
        raise NotImplementedError("Potrieda musi inplementovat tuto metodu")


class Pes(Zvierat):
    def hlas(self):
        return "haf"

    def pocet(self):
        return 4


class Kohut(Zvierat):
    def hlas(self):
        return "kotkodak"

    def pocet(self):
        return 2


class Macka(Zvierat):
    def hlas(self):
        return "Mnau"

    def pocet(self):
        return 4


def vydaj_zvuk(zviera):
    return zviera.hlas()


def pocet_nohy(zviera):
    return zviera.pocet()


pes = Pes()
macka = Macka()
kohut = Kohut()

for zviera in [pes, macka, kohut]:
    print(vydaj_zvuk(zviera))
    print(zviera.pocet())
    zviera.hlas()
