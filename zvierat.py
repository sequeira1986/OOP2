class Zvierat:
    def hlas(self):
        raise  NotImplementedError("Potrieda musi inplementovat tuto metodu")
    def pocet(self):
        raise  NotImplementedError("Potrieda musi inplementovat tuto metodu")


class Pes(Zvierat):
    def hlas(self):
    def pocet(self):
        return "haf"
        return "4"

class kohut(Zvierat):
    def hlas(self):
    def pocet(self):
        return "kotkodak"
        return "2"

class Macka(Zvierat):
    def hlas2(self):
    def pocet(self):
        return "Mnau"
        return "4"

def vydaj_zvuk(zviera):
    return  zviera.hlas()

def pocet_nohy(pocet_nohy):
    return pocet_nohy.pocet()

pes = Pes()
macka = Macka()
kohut = kohut()

for zviera in [pes, macka, kohut]:
    print(vydaj_zvuk(zviera))
    print(zviera.hlas())
    zviera.hlas()


