
def kerulet():
    kerulet: int = 0
    print('=====================================================')
    print('Kerületszámítás')
    print('Melyik síkidommal akarja végrehajtani a számítást?')
    print('1. Négyzet')
    print('2. Téglalap')
    valasztott: int = 0
    while valasztott <= 0 or valasztott > 2:
        print('')
        valasztott: int = int(input('Írd le mit választottál: '))
        if valasztott <= 0:
            print('')
            print('Az adat nem megfelelő.')
            continue
        if valasztott > 2:
            print('')
            print('Az adat nem megfelelő.')
            continue
    print('')
    print('=====================================================')

    if valasztott == 1:
        print('')
        print('Négyzet kerületszámítása')
        a: int = 0
        while a <= 0:
            print('')
            a: int = int(input('Írd le a négyzet oldalát cm-ben: '))
            if a <= 0:
                print('')
                print('Az adat nem megfelelő a számoláshoz.')
                continue
            kerulet = 4 * a
            print('')
            print(f'A négyzet kerülete: {kerulet}cm')
            print('')

    if valasztott == 2:
        print('')
        print('Téglalap kerületszámítás')
        print('')
        a: int = 0
        b: int = 0
        while a <= 0 or b <= 0:
            a: int = int(input('Írd le a téglalap a oldalát: '))
            if a <= 0:
                print('Az a adat nem megfelelő a számoláshoz.')
                continue
            b: int = int(input('Írd le a téglalap b oldalát: '))
            if b <= 0:
                print('A b adat nem megfelelő a számoláshoz.')
                continue
        kerulet = 2 * a + 2 * b
        print('')
        print(f'A téglalap kerülete: {kerulet}cm')
        print('=====================================================')


def main():
    kerulet()


if __name__ == "__main__":
    main()