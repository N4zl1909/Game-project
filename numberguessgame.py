import random

oyundurumu = True

while oyundurumu:
    corap = random.randint(1, 100)
    hak = 10

    while True:
        if hak > 0:
            tahmin = int(input("Tahminini gir: "))
        else:
            print("Kazanamadın! Oyun bitti. Sayı: {}".format(corap))
            break

        fark = abs(tahmin - corap)

        if tahmin != corap:
            hak -= 1


            if fark <= 3:
                print("ÇOK SICAK ")
            elif fark <= 10:
                print("SICAK ")
            elif fark <= 20:
                print("SOĞUK ")
            else:
                print("ÇOK SOĞUK ")

            print("Kalan hak: {}".format(hak))
        else:
            print("Kazandınız!  Doğru sayı: {}".format(corap))
            break

    devam = input("Oyuna devam etmek istiyor musun? (E/H): ")
    if devam == "E" or devam == "e":
        continue
    elif devam == "H" or devam == "h":
        print("Tekrar görüşmek üzere!")
        oyundurumu = False
