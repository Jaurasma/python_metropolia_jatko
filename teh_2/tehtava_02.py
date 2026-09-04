# Tehtävä 2 opintolaskuri

def kysy_kurssi():
    print("Anna kurssin nimi (lopeta lopettaa)")
    nimi = input("Nimi: ")
    if nimi.lower() == "lopeta":
        return None

    if nimi == "":
        print("Virheellinen syöte. Kurssin nimi ei voi olla tyhjä.")
        return False

    opintopisteet = int(input("Opintopisteet: "))
    if not 0 <= opintopisteet <= 20:
        print("Virheellinen syöte. Opintopisteiden tulee olla välillä 0-20.")
        return False

    arvosana = int(input("Arvosana: "))
    if not 1 <= arvosana <= 5:
        print("Virheellinen syöte. Arvosanan tulee olla välillä 1-5.")
        return False

    return {
        "nimi": nimi,
        "opintopisteet": opintopisteet,
        "arvosana": arvosana
    }


def laske_opintopisteet(kurssit):
    return sum(kurssi["opintopisteet"] for kurssi in kurssit)


def laske_keskiarvo(kurssit):
    summa = sum(kurssi["arvosana"] for kurssi in kurssit)
    return summa / len(kurssit)

def laske_painotettu_keskiarvo(kurssit):
    painotettu_summa = sum(kurssi["arvosana"] * kurssi["opintopisteet"] for kurssi in kurssit)
    opintopisteet_yhteensa = laske_opintopisteet(kurssit)

    if opintopisteet_yhteensa == 0:
        return 0

    return painotettu_summa / opintopisteet_yhteensa


def tulosta_kurssit(kurssit):
    print("Suoritetut kurssit:")
    for i in range(len(kurssit)):
        kurssi = kurssit[i]
        print(f"{i + 1}. {kurssi['nimi']}({kurssi['opintopisteet']}op): {kurssi['arvosana']}")


def main():
    kurssit = []
    while True:
        kurssi = kysy_kurssi()
        if kurssi is None:
            break
        if kurssi is False:
            continue
        kurssit.append(kurssi)

    print(f"Opintopisteet yhteensä {laske_opintopisteet(kurssit)}")

    if len(kurssit) > 0:
        tulosta_kurssit(kurssit)
        print(f"Arvosanojen keskiarvo: {laske_keskiarvo(kurssit):.1f}")
        print(f"Arvosanojen painotettu keskiarvo: {laske_painotettu_keskiarvo(kurssit):.1f}")

if __name__ == "__main__":
    main()