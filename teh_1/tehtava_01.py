

# Tekstin värit terminaalia varten
NOLLAUS = "\033[0m"
PUNAINEN = "\033[91m"
VIHREÄ = "\033[92m"
KELTAINEN = "\033[93m"
SYAANI = "\033[96m"
LIHAVOITU = "\033[1m"


def tervetuloa():
    kurssitulostus = (
        f"\n{LIHAVOITU}{SYAANI}SUORITETUT KURSSIT{NOLLAUS}\n"
        f"{SYAANI}------------------{NOLLAUS}\n"
    )
    kurssien_määrä = 0
    pisteiden_summa = 0
    arvosanojen_summa = 0
    painotettu_arvosanojen_summa = 0
    print(f"\n{LIHAVOITU}{SYAANI}=========================")
    print("      OPINTOLASKURI")
    print(f"========================={NOLLAUS}")
    print(f"Kirjoita kurssin nimeksi '{LIHAVOITU}lopeta{NOLLAUS}', kun olet valmis.\n")

    while True:
        kurssin_nimi = input(f"{KELTAINEN}Kurssin nimi:{NOLLAUS} ")
        if kurssin_nimi == "":
            print(f"  {PUNAINEN}Virhe: kurssin nimi ei voi olla tyhjä.{NOLLAUS}\n")
            continue
        if kurssin_nimi.lower() == "lopeta":
            break
        try:
            opintopisteet = int(input(f"{KELTAINEN}Opintopisteet (1-30):{NOLLAUS} "))
            arvosana = float(input(f"{KELTAINEN}Arvosana (1-5):{NOLLAUS} "))
            if 0 < opintopisteet <= 30 and 1 <= arvosana <= 5:
                pisteiden_summa += opintopisteet
                arvosanojen_summa += arvosana
                kurssien_määrä += 1
                painotettu_arvosanojen_summa += arvosana * opintopisteet
                kurssitulostus += (
                    f"{kurssien_määrä:>2}. {kurssin_nimi:<25} "
                    f"{opintopisteet:>2} op   arvosana {arvosana:.0f}\n"
                )
                print(f"  {VIHREÄ}Kurssi lisätty!{NOLLAUS}\n")

            else:
                print(
                    f"  {PUNAINEN}Virhe: opintopisteiden tulee olla 1-30 "
                    f"ja arvosanan 1-5.{NOLLAUS}\n"
                )
        except ValueError:
            print(
                f"  {PUNAINEN}Virhe: anna opintopisteet ja arvosana "
                f"numeroina.{NOLLAUS}\n"
            )
        pass
    if kurssien_määrä > 0:
        print(kurssitulostus)
        arvosanojen_keskiarvo = arvosanojen_summa / kurssien_määrä
        paintotettu_arvosanojen_keskiarvo = painotettu_arvosanojen_summa / pisteiden_summa
        print(f"{LIHAVOITU}{SYAANI}YHTEENVETO{NOLLAUS}")
        print(f"{SYAANI}----------{NOLLAUS}")
        print(f"Kursseja:                       {VIHREÄ}{kurssien_määrä}{NOLLAUS}")
        print(f"Opintopisteitä yhteensä:        {VIHREÄ}{pisteiden_summa}{NOLLAUS}")
        print(f"Arvosanojen keskiarvo:          {VIHREÄ}{arvosanojen_keskiarvo:.1f}{NOLLAUS}")
        print(
            f"Painotettu keskiarvo:           "
            f"{VIHREÄ}{paintotettu_arvosanojen_keskiarvo:.1f}{NOLLAUS}\n"
        )
    else:
        print(
            f"\n{KELTAINEN}Ei lisättyjä kursseja. "
            f"Opintopisteitä yhteensä: 0{NOLLAUS}\n"
        )

def main():
    tervetuloa()

if __name__ == "__main__":
    main()
