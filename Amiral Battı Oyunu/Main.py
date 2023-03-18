# Yunus Emre Ay / 21100011016 / Tel:05516524768 / E-posta:TR.yunus.emre.ay@gmail.com / <3
import random
while True:
    print("*****Amiral Battı Oyununa Hosgeldiniz*****\n\n")
    print("Oyuna başlamadan once 'Boyut'u belirlemeniz gerekmektedir.\n")
    print("Lutfen 'Boyut'u belirlerken en az '10' sayisini kullaniniz.\n")
    print("10'dan daha kucuk bir sayi kullandiginiz taktirde Boyut=10 alinarak isleme devam edilecektir.\n\n")
    boyut = int(input("Lutfen Boyut'u belirleyiniz --> :"))

    if boyut < 10:
        boyut = 10

    print("Boyut : {}\n\n".format(boyut))

    Oyun_Alani_Gizli=list()
    for i in range(boyut):
        Oyun_Alani_Gizli.append(["?"]*boyut)

    Oyun_Alani_Acik=list()
    for i in range(boyut):
        Oyun_Alani_Acik.append(["?"]*boyut)

    # Oyun_Alani_Gizli = [["?","?","?","?","?","?","?","?","?","?"], 0            { Gemilerin gorunur ekranda rahat bir sekilde
    #                     ["?","?","?","?","?","?","?","?","?","?"], 1              gorulebilmesi icin her cesit gemi icin farkli
    #                     ["?","?","?","?","?","?","?","?","?","?"], 2              bir harf ataması gerceklestirdim.
    #                     ["?","?","?","?","?","?","?","?","?","?"], 3
    #                     ["?","?","?","?","?","?","?","?","?","?"], 4              1 birimlik gemi --> A'harfi
    #                     ["?","?","?","?","?","?","?","?","?","?"], 5              2 birimlik gemi --> B'harfi
    #                     ["?","?","?","?","?","?","?","?","?","?"], 6              3 birimlik gemi --> C'harfi
    #                     ["?","?","?","?","?","?","?","?","?","?"], 7              4 birimlik gemi --> D'harfi }
    #                     ["?","?","?","?","?","?","?","?","?","?"], 8
    #                     ["?","?","?","?","?","?","?","?","?","?"]] 9
    #                       0   1   2   3   4   5   6   7   8   9
    #                                                                           ~~YANDA GORDUGUNUZ SEKILLER BENIM MATRISLERIMIN
    # Oyun_Alani_Acik = [["?","?","?","?","?","?","?","?","?","?"], 0             SEKILLERI.~~ (Matrislerimi 14-20 satirlari arasinda
    #                    ["?","?","?","?","?","?","?","?","?","?"], 1             for döngüleriyle olusturdum, bu sekiller sadece
    #                    ["?","?","?","?","?","?","?","?","?","?"], 2             gorselligi arttırabilmek icin)
    #                    ["?","?","?","?","?","?","?","?","?","?"], 3
    #                    ["?","?","?","?","?","?","?","?","?","?"], 4
    #                    ["?","?","?","?","?","?","?","?","?","?"], 5
    #                    ["?","?","?","?","?","?","?","?","?","?"], 6
    #                    ["?","?","?","?","?","?","?","?","?","?"], 7
    #                    ["?","?","?","?","?","?","?","?","?","?"], 8
    #                    ["?","?","?","?","?","?","?","?","?","?"]] 9
    #                      0   1   2   3   4   5   6   7   8   9
    #


    # 1.gemi --> Görünür ekrana 'A' olarak basılacak
    gemix1=random.randint(0,boyut-1)
    gemiy1=random.randint(0,boyut-1)
    Oyun_Alani_Acik[gemix1][gemiy1] = "A"

    # 2.gemi --> Görünür ekrana 'B' olarak basılacak
    gemi2_yon=random.randint(1,2) # 1 --> dikey / 2 --> yatay
    while True:
        gemix2=random.randint(0,boyut-1)
        gemiy2=random.randint(0,boyut-1)
        if Oyun_Alani_Acik[gemix2][gemiy2] == "?":
            if gemi2_yon == 1:
                if gemiy2 < boyut/2:
                    if Oyun_Alani_Acik[gemix2][gemiy2+1] == "?":
                        Oyun_Alani_Acik[gemix2][gemiy2] = "B"
                        Oyun_Alani_Acik[gemix2][gemiy2+1] = "B"
                        break
                    else:
                        continue
                else:
                    if Oyun_Alani_Acik[gemix2][gemiy2-1] == "?":
                        Oyun_Alani_Acik[gemix2][gemiy2] = "B"
                        Oyun_Alani_Acik[gemix2][gemiy2-1] = "B"
                        break
                    else:
                        continue

            else:
                if gemix2 < boyut/2:
                    if Oyun_Alani_Acik[gemix2+1][gemiy2] == "?":
                        Oyun_Alani_Acik[gemix2][gemiy2] = "B"
                        Oyun_Alani_Acik[gemix2+1][gemiy2] = "B"
                        break
                    else:
                        continue
                else:
                    if Oyun_Alani_Acik[gemix2-1][gemiy2] == "?":
                        Oyun_Alani_Acik[gemix2][gemiy2] = "B"
                        Oyun_Alani_Acik[gemix2-1][gemiy2] = "B"
                        break
                    else:
                        continue

    # 3.gemi --> Görünür ekrana 'C' olarak basılacak
    gemi3_yon=random.randint(1,2) # 1 --> dikey / 2 --> yatay
    while True:
        gemix3=random.randint(0,boyut-1)
        gemiy3=random.randint(0,boyut-1)
        if Oyun_Alani_Acik[gemix3][gemiy3] == "?":
            if gemi3_yon == 1:
                if gemiy3 < boyut/2:
                    if Oyun_Alani_Acik[gemix3][gemiy3+1] == "?":
                        if Oyun_Alani_Acik[gemix3][gemiy3+2] == "?":
                            Oyun_Alani_Acik[gemix3][gemiy3] = "C"
                            Oyun_Alani_Acik[gemix3][gemiy3+1] = "C"
                            Oyun_Alani_Acik[gemix3][gemiy3+2] = "C"
                            break
                        else:
                            continue
                    else:
                        continue
                else:
                    if Oyun_Alani_Acik[gemix3][gemiy3-1] == "?":
                        if Oyun_Alani_Acik[gemix3][gemiy3-2] == "?":
                            Oyun_Alani_Acik[gemix3][gemiy3] = "C"
                            Oyun_Alani_Acik[gemix3][gemiy3-1] = "C"
                            Oyun_Alani_Acik[gemix3][gemiy3-2] = "C"
                            break
                        else:
                            continue
                    else:
                        continue

            else:
                if gemix3 < boyut/2:
                    if Oyun_Alani_Acik[gemix3+1][gemiy3] == "?":
                        if Oyun_Alani_Acik[gemix3+2][gemiy3] == "?":
                            Oyun_Alani_Acik[gemix3][gemiy3] = "C"
                            Oyun_Alani_Acik[gemix3+1][gemiy3] = "C"
                            Oyun_Alani_Acik[gemix3+2][gemiy3] = "C"
                            break
                        else:
                            continue
                    else:
                        continue
                else:
                    if Oyun_Alani_Acik[gemix3-1][gemiy3] == "?":
                        if Oyun_Alani_Acik[gemix3-2][gemiy3] == "?":
                            Oyun_Alani_Acik[gemix3][gemiy3] = "C"
                            Oyun_Alani_Acik[gemix3-1][gemiy3] = "C"
                            Oyun_Alani_Acik[gemix3-2][gemiy3] = "C"
                            break
                        else:
                            continue
                    else:
                        continue

    # 4.gemi --> Görünür ekrana 'D' olarak basılacak
    gemi4_yon=random.randint(1,2) # 1 --> dikey / 2 --> yatay
    while True:
        gemix4=random.randint(0,boyut-1)
        gemiy4=random.randint(0,boyut-1)
        if Oyun_Alani_Acik[gemix4][gemiy4] == "?":
            if gemi4_yon == 1:
                if gemiy4 < boyut/2:
                    if Oyun_Alani_Acik[gemix4][gemiy4+1] == "?":
                        if Oyun_Alani_Acik[gemix4][gemiy4+2] == "?":
                            if Oyun_Alani_Acik[gemix4][gemiy4+3] == "?":
                                Oyun_Alani_Acik[gemix4][gemiy4] = "D"
                                Oyun_Alani_Acik[gemix4][gemiy4+1] = "D"
                                Oyun_Alani_Acik[gemix4][gemiy4+2] = "D"
                                Oyun_Alani_Acik[gemix4][gemiy4+3] = "D"
                                break
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    if Oyun_Alani_Acik[gemix4][gemiy4-1] == "?":
                        if Oyun_Alani_Acik[gemix4][gemiy4-2] == "?":
                            if Oyun_Alani_Acik[gemix4][gemiy4-3] == "?":
                                Oyun_Alani_Acik[gemix4][gemiy4] = "D"
                                Oyun_Alani_Acik[gemix4][gemiy4-1] = "D"
                                Oyun_Alani_Acik[gemix4][gemiy4-2] = "D"
                                Oyun_Alani_Acik[gemix4][gemiy4-3] = "D"
                                break
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue

            else:
                if gemix4 < boyut/2:
                    if Oyun_Alani_Acik[gemix4+1][gemiy4] == "?":
                        if Oyun_Alani_Acik[gemix4+2][gemiy4] == "?":
                            if Oyun_Alani_Acik[gemix4+3][gemiy4] == "?":
                                Oyun_Alani_Acik[gemix4][gemiy4] = "D"
                                Oyun_Alani_Acik[gemix4+1][gemiy4] = "D"
                                Oyun_Alani_Acik[gemix4+2][gemiy4] = "D"
                                Oyun_Alani_Acik[gemix4+3][gemiy4] = "D"
                                break
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    if Oyun_Alani_Acik[gemix4-1][gemiy4] == "?":
                        if Oyun_Alani_Acik[gemix4-2][gemiy4] == "?":
                            if Oyun_Alani_Acik[gemix4-3][gemiy4] == "?":
                                Oyun_Alani_Acik[gemix4][gemiy4] = "D"
                                Oyun_Alani_Acik[gemix4-1][gemiy4] = "D"
                                Oyun_Alani_Acik[gemix4-2][gemiy4] = "D"
                                Oyun_Alani_Acik[gemix4-3][gemiy4] = "D"
                                break
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue


    A_batti = 0
    B_batti = 0
    C_batti = 0
    D_batti = 0
    print("Oyunumuzda 2 farklı mod bulunmaktadir.\n\n1)Gizli mod:\n2)Acık mod:\n\nLutfen size uygun olani seciniz ---> ",end="")
    mod = int(input(""))
    vurus = 0
    isabet =0

    if mod == 1:
        print("***Gizli mod aktiflestirildi***")
        while True:
            saldiriy =int(input("Saldirmak istediginiz yerin X eksenini giriniz ==--->"))
            saldirix =int(input("Saldirmak istediginiz yerin Y eksenini giriniz ==--->"))
            if Oyun_Alani_Acik[saldirix][saldiriy] == "X" or Oyun_Alani_Acik[saldirix][saldiriy] == "*":
                print("\n~~Daha once saldirdiginiz bir noktaya saldirmaya calisiyorsunuz, lutfen farkı bir kordinat belirleyiniz")
                continue
            if Oyun_Alani_Acik[saldirix][saldiriy] == "A" or Oyun_Alani_Acik[saldirix][saldiriy] == "B" or Oyun_Alani_Acik[saldirix][saldiriy] == "C" or Oyun_Alani_Acik[saldirix][saldiriy] == "D":
                print("~~~Tebrikler bir gemi vurdunuz~~~")
                Oyun_Alani_Acik[saldirix][saldiriy] = "X"
                Oyun_Alani_Gizli[saldirix][saldiriy] = "X"
                isabet += 1

                A_sayac = 0
                B_sayac = 0
                C_sayac = 0
                D_sayac = 0

                for i in range(boyut):
                    for a in range(boyut):
                        if Oyun_Alani_Acik[i][a] == "A":
                            A_sayac += 1
                        if Oyun_Alani_Acik[i][a] == "B":
                            B_sayac += 1
                        if Oyun_Alani_Acik[i][a] == "C":
                            C_sayac += 1
                        if Oyun_Alani_Acik[i][a] == "D":
                            D_sayac += 1

                if A_sayac == 0 and A_batti == 0:
                    print("\\\\***Tebrikler Bir Gemiyi Tamamen Batirdiniz***//")
                    A_batti = 1
                elif B_sayac == 0 and B_batti == 0:
                    print("\\\\***Tebrikler Bir Gemiyi Tamamen Batirdiniz***//")
                    B_batti = 1
                elif C_sayac == 0 and C_batti == 0:
                    print("\\\\***Tebrikler Bir Gemiyi Tamamen Batirdiniz***//")
                    C_batti = 1
                elif D_sayac == 0 and D_batti == 0:
                    print("\\\\***Tebrikler Bir Gemiyi Tamamen Batirdiniz***//")
                    D_batti == 1
            else:
                print("~~~Maalesef isabet edemediniz~~~")
                Oyun_Alani_Acik[saldirix][saldiriy] = "*"
                Oyun_Alani_Gizli[saldirix][saldiriy] = "*"
            vurus += 1
            print("-----------------------------------------------------------------------\nOyun Alaninin Yeni Hali:")
            for i in range(boyut):
                print("    {}".format(i), end="")
            print("    X-Ekseni")
            for i in range(boyut):
                print("{} {}".format(i, Oyun_Alani_Gizli[i]))
            print("Y-Ekseni")
            if isabet == 10:
                print("\\\\Tebrikler bütün gemileri batirmayi basardiniz//")
                break
            if vurus == boyut*boyut//3:
                print("\\\\Malesef kaybettiniz//")
                break

        print("Toplam puaniniz : {} ".format(boyut*boyut//3-vurus))

    if mod == 2:
        print("***Acik mod aktiflestirildi***")
        while True:
            saldiriy = int(input("Saldirmak istediginiz yerin X eksenini giriniz ==--->"))
            saldirix = int(input("Saldirmak istediginiz yerin Y eksenini giriniz ==--->"))
            if Oyun_Alani_Acik[saldirix][saldiriy] == "X" or Oyun_Alani_Acik[saldirix][saldiriy] == "*":
                print("\n~~Daha once saldirdiginiz bir noktaya saldirmaya calisiyorsunuz, lutfen farkı bir kordinat belirleyiniz")
                continue
            if Oyun_Alani_Acik[saldirix][saldiriy] == "A" or Oyun_Alani_Acik[saldirix][saldiriy] == "B" or Oyun_Alani_Acik[saldirix][saldiriy] == "C" or Oyun_Alani_Acik[saldirix][saldiriy] == "D":
                print("~~~Tebrikler bir gemi vurdunuz~~~")
                Oyun_Alani_Acik[saldirix][saldiriy] = "X"
                Oyun_Alani_Gizli[saldirix][saldiriy] = "X"
                isabet += 1

                A_sayac = 0
                B_sayac = 0
                C_sayac = 0
                D_sayac = 0

                for i in range(boyut):
                    for a in range(boyut):
                        if Oyun_Alani_Acik[i][a] == "A":
                            A_sayac += 1
                        if Oyun_Alani_Acik[i][a] == "B":
                            B_sayac += 1
                        if Oyun_Alani_Acik[i][a] == "C":
                            C_sayac += 1
                        if Oyun_Alani_Acik[i][a] == "D":
                            D_sayac += 1

                if A_sayac == 0 and A_batti == 0:
                    print("\\\\***Tebrikler Bir Gemiyi Tamamen Batirdiniz***//")
                    A_batti = 1
                elif B_sayac == 0 and B_batti == 0:
                    print("\\\\***Tebrikler Bir Gemiyi Tamamen Batirdiniz***//")
                    B_batti = 1
                elif C_sayac == 0 and C_batti == 0:
                    print("\\\\***Tebrikler Bir Gemiyi Tamamen Batirdiniz***//")
                    C_batti = 1
                elif D_sayac == 0 and D_batti == 0:
                    print("\\\\***Tebrikler Bir Gemiyi Tamamen Batirdiniz***//")
                    D_batti = 1
            else:
                print("~~~Maalesef isabet edemediniz~~~")
                Oyun_Alani_Acik[saldirix][saldiriy] = "*"
                Oyun_Alani_Gizli[saldirix][saldiriy] = "*"
            vurus += 1
            print("-----------------------------------------------------------------------\nOyun Alaninin Yeni Hali:")
            for i in range(boyut):
                print("    {}".format(i), end="")
            print("    X-Ekseni")
            for i in range(boyut):
                print("{} {}".format(i, Oyun_Alani_Acik[i]))
            print("Y-Ekseni")
            if isabet == 10:
                print("\\\\Tebrikler bütün gemileri batirmayi basardiniz//")
                break
            if vurus == boyut*boyut // 3:
                print("\\\\Malesef kaybettiniz//")
                break

        print("Toplam puaniniz : {} ".format(boyut*boyut // 3 - vurus))

    tercih =input("Oyuna devam etmek istiyorsaniz lutfen '0' tusunu tusalyiniz, cikmak icin 'Enter' tusundan farkli"
                       "herhangi bir tusu tuslayiniz ---> ")
    if tercih != "0":
        break
