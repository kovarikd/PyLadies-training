class Kotatko:   
    def __init__(self, jmeno):
        # Je volana pri vytvareni objektu
        self.jmeno = jmeno
        self.zivoty = 9

    def __str__(self):
        # V pripade potreby prevadi objekt na retezec
        return "<Kotatko jmenem {}>".format(self.jmeno)

    def zamnoukej(self):
        print("{}: Mnau").format(self.jmeno)

    def snez(self, jidlo):
        if jidlo == 'ryba':
            self.zivoty += 1
        print("{}: Mnau mnau! {} mi chutna".format(self.jmeno, jidlo))

    def je_ziva(self):
        if self.zivoty == 0:
            print('{} je mrtvy!'.format(self.jmeno))
        else:
            print("{} je zivy a ma {} zivotu!".format(self.jmeno, self.zivoty))

    def uber_zivot(self):
        self.zivoty -= 1
        

mourek = Kotatko(jmeno = 'Mourek')
mourek.snez("Ryba")
mourek.je_ziva()
mourek.uber_zivot()
mourek.je_ziva()
mourek.snez('ryba')
mourek.je_ziva()


micka = Kotatko(jmeno = "Micka")

print(mourek)


