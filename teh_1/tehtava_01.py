
def tervetuloa():
    kurssitulostus = "Suoritetut kurssit:\n"
    kurssien_määrä = 0
    pisteiden_summa = 0
    arvosanojen_summa = 0
    painotettu_arvosanojen_summa = 0
    print("Tervetuloa opintolaskuriin!")
    while True:
        print("Anna kurssin nimi (lopeta lopettaa): ")
        kurssin_nimi = input("Nimi: ")
        if kurssin_nimi == "":
            print("Kurssin nimi ei voi olla tyhjä. Yritä uudelleen.")
            continue
        if kurssin_nimi.lower() == "lopeta":
            break
        try:
            opintopisteet = int(input("Syötä opintopisteet: "))
            arvosana = float(input("Syötä arvosana (1-5): "))
            if 0 < opintopisteet <= 30 and 1 <= arvosana <= 5:
                pisteiden_summa += opintopisteet
                arvosanojen_summa += arvosana
                kurssien_määrä += 1
                painotettu_arvosanojen_summa += arvosana * opintopisteet
                kurssitulostus += f"{kurssien_määrä}. {kurssin_nimi}({opintopisteet}op): {arvosana:.0f}\n"

            else:
                print("Virheellinen syöte. Opintopisteiden tulee olla välillä 0-30 ja arvosanan välillä 1-5.")
        except ValueError:
            print("Virheellinen syöte. Yritä uudelleen.")
        pass
    if kurssien_määrä > 0:
        print(f"Opintopisteet yhteensä: {pisteiden_summa}")
        print(kurssitulostus)
        arvosanojen_keskiarvo = arvosanojen_summa / kurssien_määrä
        paintotettu_arvosanojen_keskiarvo = painotettu_arvosanojen_summa / pisteiden_summa
        print(f"Arvosanojen keskiarvo: {arvosanojen_keskiarvo:.1f}")
        print(f"Arvosanojen painotettu keskiarvo: {paintotettu_arvosanojen_keskiarvo:.1f}")
    else:
        print("Opintopisteet yhteensä: 0")

def main():
    tervetuloa()

if __name__ == "__main__":
    main()