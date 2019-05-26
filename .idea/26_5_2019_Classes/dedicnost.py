
class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutna!".format(self.jmeno, jidlo))


class Kotatko(Zviratko):
    def zamnoukej(self):
        print("{}: Mnau!".format(self.jmeno))

    def snez(self, jidlo):
        print("({} na {} chvili fascinovane kouka)".format(self.jmeno, jidlo))
        super().snez(jidlo)

class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        jmeno = jmeno.replace('S', 'Sss')
        super().__init__(jmeno)





class Stenatko(Zviratko):
    def zastekej(self):
        print("{}: Haf!".format(self.jmeno))


micka = Kotatko('Micka')
azorek = Stenatko('Azorek')
micka.zamnoukej()
azorek.zastekej()
micka.snez('mys')
azorek.snez('kost')

standa = Hadatko('Stanislav')
standa.snez('mys')

zviratka = [Kotatko('Micka2'), Stenatko('Azor')]

for zviratko in zviratka:
    zviratko.snez('flakota')