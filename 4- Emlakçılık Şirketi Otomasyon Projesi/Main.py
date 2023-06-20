# Yunus Emre Ay / E-posta:TR.yunus.emre.ay@gmail.com
# Yazmıs Oldugum Koda Benim Icıme Cok Sindi Umarım Sizde Begenirsiniz.


def Ekleme():
    def id_kontrol():
        Dosya = open("Main.txt", "r", encoding="UTF-8")
        id_tutucu = set()
        id = 101
        for i in Dosya:
            id_tutucu.add(int(i[3:6]))
        while True:
            if id not in id_tutucu:
                Dosya.close()
                return id
            id += 1

    id = id_kontrol()
    Dosya = open("Main.txt", "a", encoding="UTF-8")
    Dosya.write("id:{} / ".format(id))
    print("Eklemek Istediginiz Ilan Hangisi?")
    Hangisi1 = input("1)Ev\n2)Araba\n---> ")
    if Hangisi1 == "1":
        Dosya.write("Ev / ")
    elif Hangisi1 == "2":
        Dosya.write("Araba / ")
    print("Eklemek Istediginiz Ilan Hangisi?")
    Hangisi2 = input("1)Satilik\n2)Kiralik\n---> ")
    if Hangisi2 == "1":
        Dosya.write("Satilik / ")
    elif Hangisi2 == "2":
        Dosya.write("Kiralik / ")
    fiyat = input("Ilaninizin Fiyatini Giriniz\n"
                  "(Aralara Nokta koyarak Max 10 Karakter Olacak Sekilde, Ornek --> 11.111.111)\n---> ")
    while len(fiyat) < 10:
        fiyat += " "
    Dosya.write("Fiyat:{} TL / ".format(fiyat))
    if Hangisi1 == "1":
        OdaSayisi = input("Oda Sayisi Bilgisini Giriniz\n(Araya '+' Koyarak Max 3 Karakter Olacak Sekilde, Ornek --> 3+1)\n---> ")
        while len(OdaSayisi) < 3:
            OdaSayisi += " "
        Dosya.write("OdaSayisi:{} / ".format(OdaSayisi))
    elif Hangisi1 == "2":
        Marka = input("Arabanın Marka Bilgisini Giriniz\n(Lutfen Turkce Karakter Kullanmayiniz, Turkce Karakterler Dosya Islemlerinde "
                      "1 byte Yerine 2 byte Sayildigi Icın Hatalara Sebep Olmaktadir)\n(Max 10 Karakter Olacak Sekilde, Ornek --> Mercedes)\n---> ")
        while len(Marka) < 10:
            Marka += " "
        Dosya.write("Marka:{} / ".format(Marka))
    if Hangisi1 == "1":
        KacM2 = input("Eviniz Kac m2 Giriniz\n(Max 3 Karakter Olacak Sekilde, Ornek --> 130)\n---> ")
        while len(KacM2) < 3:
            KacM2 += " "
        Dosya.write("m2:{} / ".format(KacM2))
    elif Hangisi1 == "2":
        Model = input("Arabanızın Model Yilini Giriniz\n(Max 4 Karakter Olacak Sekilde, Orndek --> 2016)\n---> ")
        while len(Model) < 4:
            Model += " "
        Dosya.write("Model:{} / ".format(Model))
    if Hangisi1 == "1":
        Kat = input("Eviniz Bulundugu Kati Giriniz\n(Max 2 Karakter Olacak Sekilde, Ornek --> 12)\n---> ")
        while len(Kat) < 2:
            Kat += " "
        Dosya.write("Kat:{} / ".format(Kat))
    elif Hangisi1 == "2":
        print("Arabanizla Ilgili Olan Secenegi Seciniz")
        Degisen = input("1)Degisen Parca Var\n2)Degisen Parca Yok\n---> ")
        if Degisen == "1":
            Dosya.write("Degisen:Var / ")
        elif Degisen == "2":
            Dosya.write("Degisen:Yok / ")
    if Hangisi1 == "1":
        YapilisYili = input("Evinizin Yapilis Yilini Giriniz\n(Max 4 Karakter Olacak Sekilde, Ornek --> 2013)\n---> ")
        while len(YapilisYili) < 4:
            YapilisYili += " "
        Dosya.write("YapilisYili:{}      .".format(YapilisYili))
    elif Hangisi1 == "2":
        print("Arabanizla Ilgili Olan Secenegi Seciniz")
        Boya = input("1)Boya Var\n2)Boya Yok\n---> ")
        if Boya == "1":
            Dosya.write("Boya:Var")
        elif Boya == "2":
            Dosya.write("Boya:Yok")
    Dosya.write("\n")
    Dosya.close()

def Listeleme():
    Dosya = open("Main.txt", "r", encoding="UTF-8")
    print(Dosya.read(), end = "")
    Dosya.close()

def Guncelleme():
    Dosya = open("Main.txt", "+r", encoding="UTF-8")
    Guncellenecek_id = input("Guncellemek Istediginiz Ilanin id Numarasını Giriniz\n---> ")
    byte_bulucu = 0
    for i in Dosya:
        if Guncellenecek_id == i[3:6]:
            break
        byte_bulucu += 105
    Dosya.seek(byte_bulucu + 9)
    Ev_Ar = Dosya.read(2)

    if Ev_Ar == "Ev":
        print("""Degistirmek Istediginiz Kaydın Turu "Ev" \n""")
        Guncellemek = input("1)Satilik/Kiralik Durumunu Degistirmek Icın\n2)Fiyat Bilgisini Degistirmek Icın\n"
                            "3)Oda Sayisi Bilgisini Degistirmek Icın\n4)m2 Bilgisini Degistirmek Icın\n5)Kat Bilgisini Degistirmek Icın\n"
                            "6)Yapilis Yili Bilgisini Degistirmek Icın\n---> ")

        if Guncellemek == "1":
            Dosya.seek(byte_bulucu + 14)
            tut = Dosya.read(7)
            if tut == "Satilik":
                Dosya.seek(byte_bulucu + 14)
                Dosya.write("Kiralik")
            else:
                Dosya.seek(byte_bulucu + 14)
                Dosya.write("Satilik")
        elif Guncellemek == "2":
            Dosya.seek(byte_bulucu + 30)
            Dosya.write("          ")
            Dosya.seek(byte_bulucu + 30)
            fiyat = input("Ilaninizin Fiyatini Giriniz\n"
                          "(Aralara Nokta koyarak Max 10 Karakter Olacak Sekilde, Ornek --> 11.111.111)\n---> ")
            Dosya.write(fiyat)
        elif Guncellemek == "3":
            Dosya.seek(byte_bulucu + 56)
            Dosya.write("   ")
            Dosya.seek(byte_bulucu + 56)
            OdaSayisi = input("Oda Sayisi Bilgisini Giriniz\n(Araya '+' Koyarak Max 3 Karakter Olacak Sekilde, Ornek --> 3+1)\n---> ")
            Dosya.write(OdaSayisi)
        elif Guncellemek == "4":
            Dosya.seek(byte_bulucu + 65)
            Dosya.write("   ")
            Dosya.seek(byte_bulucu + 65)
            KacM2 = input("Eviniz Kac m2 Giriniz\n(Max 3 Karakter Olacak Sekilde, Ornek --> 130)\n---> ")
            Dosya.write(KacM2)
        elif Guncellemek == "5":
            Dosya.seek(byte_bulucu + 75)
            Dosya.write("  ")
            Dosya.seek(byte_bulucu + 75)
            Kat = input("Eviniz Bulundugu Kati Giriniz\n(Max 2 Karakter Olacak Sekilde, Ornek --> 12)\n---> ")
            Dosya.write(Kat)
        elif Guncellemek == "6":
            Dosya.seek(byte_bulucu + 92)
            Dosya.write("    ")
            Dosya.seek(byte_bulucu + 92)
            YapilisYili = input("Evinizin Yapilis Yilini Giriniz\n(Max 4 Karakter Olacak Sekilde, Ornek --> 2013)\n---> ")
            Dosya.write(YapilisYili)

    else:
        print("""Degistirmek Istediginiz Kaydın Turu "Araba" \n""")
        Guncellemek = input("1)Satilik/Kiralik Durumunu Degistirmek Icın\n2)Fiyat Bilgisini Degistirmek Icın\n"
                            "3)Marka Bilgisini Degistirmek Icin\n4)Model Bilgisini Degistirmek Icin\n5)Degisen Parca Bilgisini Degistirmek Icin\n"
                            "6)Boya Bilgisini Degistirmek Icin\n---> ")

        if Guncellemek == "1":
            Dosya.seek(byte_bulucu + 17)
            tut = Dosya.read(7)
            if tut == "Satilik":
                Dosya.seek(byte_bulucu + 17)
                Dosya.write("Kiralik")
            else:
                Dosya.seek(byte_bulucu + 17)
                Dosya.write("Satilik")
        elif Guncellemek == "2":
            Dosya.seek(byte_bulucu + 33)
            Dosya.write("          ")
            Dosya.seek(byte_bulucu + 33)
            fiyat = input("Ilaninizin Fiyatini Giriniz\n"
                          "(Aralara Nokta koyarak Max 10 Karakter Olacak Sekilde, Ornek --> 11.111.111)\n---> ")
            Dosya.write(fiyat)
        elif Guncellemek == "3":
            Dosya.seek(byte_bulucu + 55)
            Dosya.write("          ")
            Dosya.seek(byte_bulucu + 55)
            Marka = input("Arabanin Marka Bilgisini Giriniz\n(Lutfen Turkce Karakter Kullanmayiniz, Turkce Karakterler Dosya Islemlerinde "
                          "1 byte Yerine 2 byte Sayildigi Icin Hatalara Sebep Olmaktadir)\n(Max 10 Karakter Olacak Sekilde, Ornek --> Mercedes)\n---> ")
            Dosya.write(Marka)
        elif Guncellemek == "4":
            Dosya.seek(byte_bulucu + 74)
            Dosya.write("    ")
            Dosya.seek(byte_bulucu + 74)
            Model = input("Arabanızın Model Yilini Giriniz\n(Max 4 Karakter Olacak Sekilde, Orndek --> 2016)\n---> ")
            Dosya.write(Model)
        elif Guncellemek == "5":
            Dosya.seek(byte_bulucu + 89)
            tut = Dosya.read(3)
            if tut == "Var":
                Dosya.seek(byte_bulucu + 89)
                Dosya.write("Yok")
            else:
                Dosya.seek(byte_bulucu + 89)
                Dosya.write("Var")
        elif Guncellemek == "6":
            Dosya.seek(byte_bulucu + 100)
            tut = Dosya.read(3)
            if tut == "Var":
                Dosya.seek(byte_bulucu + 100)
                Dosya.write("Yok")
            else:
                Dosya.seek(byte_bulucu + 100)
                Dosya.write("Var")

    Dosya.close()

def Silme():
    Dosya = open("Main.txt", "+r", encoding="UTF-8")
    Silinecek_id = input("Silmek Istediginiz Ilanin id Numarasını Giriniz\n---> ")
    Silinecek_Satırın_Baslangıc_Byteı = 0
    for i in Dosya:
        if Silinecek_id == i[3:6]:
            break
        Silinecek_Satırın_Baslangıc_Byteı += 105
    Dosya.seek(Silinecek_Satırın_Baslangıc_Byteı + 105)
    tut = Dosya.read()
    Dosya.truncate(Silinecek_Satırın_Baslangıc_Byteı)
    Dosya.seek(Silinecek_Satırın_Baslangıc_Byteı)
    Dosya.write(tut)
    Dosya.close()

def Filtreleme():
    Filtre = list()
    Eleme = set()

    Dosya = open("Main.txt", "r", encoding="UTF-8")
    Ev_Ar = input("""Hangi Filtreleme Secenegini Aktiflestirmek Istiyorsunu?\n1)Ev\n2)Araba\n---> """)
    if Ev_Ar == "1":
        for elma in Dosya:
            if elma[9:11] == "Ev":
                Eleme.add(elma[3:6])

        print("Ev Icın Hangi Filtreleme Seceneklerini Kullanmak Istıyorsanız Seciniz\n(Aynı Anda Birden Fazla Secenek Secmek Icın "
              "Lutfen Sectiginiz Secenekler Arasinda ',' Virgul Kullaniniz, Ornek --> 1,2,3)\n")
        Filtre += input("1)Satilik/Kiralik Durumunu Filtrelemek Icın\n2)Fiyat Bilgisini Filtrelemek Icın\n"
                        "3)Oda Sayisi Bilgisini Filtrelemek Icın\n4)m2 Bilgisini Filtrelemek Icın\n5)Kat Bilgisini Filtrelemek Icın\n"
                        "6)Yapilis Yili Bilgisini Filtrelemek Icın\n---> ").split(",")
        for i in Filtre:
            if i == "1":
                print("Filtrelemek Istediginiz Ilan Hangisi?")
                Filt1 = input("1)Satilik\n2)Kiralik\n---> ")
                if Filt1 == "1":
                    Dosya.seek(0)
                    for a in Dosya:
                        if a[9:11] == "Ev" and a[14:21] == "Satilik":
                            continue
                        else:
                            Eleme.discard(a[3:6])
                elif Filt1 == "2":
                    Dosya.seek(0)
                    for a in Dosya:
                        if a[9:11] == "Ev" and a[14:21] == "Kiralik":
                            continue
                        else:
                            Eleme.discard(a[3:6])
            elif i == "2":
                fiyat = ""
                fiyat = str(fiyat)
                alt, ust = input("Ilanlarin Fiyatini Filtrelemek Icın Alt Ve Ust Sinirlari Giriniz\n(Sinirlari Girerken "
                                 "Sinirlar Arasinda Lutfen ',' Kullaniniz ve Alt ve Ust sinirlari Sirasiyla Giriniz,"
                                 "Ayrica Sinirlari Girerken Sayilari '.' Nokta Kullanmadan Direkt Giriniz, Ornek --> 500000,800000)\n---> ").split(",")
                alt = int(alt)
                ust = int(ust)
                Dosya.seek(0)
                for a in Dosya:
                    fiyat = ""
                    if a[9:11] == "Ev":
                        tut1 = a[30:40]
                        for b in tut1:
                            if b != "." and b != " ":
                                fiyat += b
                        fiyat1 = int(fiyat)
                        if alt <= fiyat1 and fiyat1 <= ust:
                            continue
                        else:
                            Eleme.discard(a[3:6])
            elif i == "3":
                Oda_Sayisi = 0
                alt_oda, ust_oda = input("Ilanlarin Oda Sayisini Filtrelemek Icın Alt Ve Ust Sinirlari Giriniz(3+1 = 4 Kabul Edilmektedir)\n(Sinirlari Girerken "
                                         "Sinirlar Arasinda Lutfen ',' Kullaniniz ve Alt ve Ust sinirlari Sirasiyla Giriniz, Ornek --> 3,7)\n---> ").split(",")
                alt_oda = int(alt_oda)
                ust_oda = int(ust_oda)
                Dosya.seek(0)
                for a in Dosya:
                    Oda_Sayisi = 0
                    if a[9:11] == "Ev":
                        tut2 = a[56:59]
                        for b in tut2:
                            if b != "+" and b != " ":
                                tut3 = int(b)
                                Oda_Sayisi += tut3
                        if alt_oda <= Oda_Sayisi and Oda_Sayisi <= ust_oda:
                            continue
                        else:
                            Eleme.discard(a[3:6])
            elif i == "4":
                alt_m2, ust_m2 = input("m2 Bilgisini Filtrelemek Icın Alt Ve Ust Sinirlari Giriniz\n(Sinirlari Girerken "
                                       "Sinirlar Arasinda Lutfen ',' Kullaniniz ve Alt ve Ust sinirlari Sirasiyla Giriniz, Ornek --> 120,180)\n---> ").split(",")
                alt_m2 = int(alt_m2)
                ust_m2 = int(ust_m2)
                Dosya.seek(0)
                for a in Dosya:
                    if a[9:11] == "Ev":
                        Mevcut_m2 = int(a[65:68])
                        if alt_m2 <= Mevcut_m2 and Mevcut_m2 <= ust_m2:
                            continue
                        else:
                            Eleme.discard(a[3:6])

            elif i == "5":
                alt_kat, ust_kat = input("Kat Bilgisini Filtrelemek Icın Alt Ve Ust Sinirlari Giriniz\n(Sinirlari Girerken "
                                         "Sinirlar Arasinda Lutfen ',' Kullaniniz ve Alt ve Ust sinirlari Sirasiyla Giriniz, Ornek --> 11,22)\n---> ").split(",")
                alt_kat = int(alt_kat)
                ust_kat = int(ust_kat)
                Dosya.seek(0)
                for a in Dosya:
                    if a[9:11] == "Ev":
                        Mevcut_kat = int(a[75:77])
                        if alt_kat <= Mevcut_kat and Mevcut_kat <= ust_kat:
                            continue
                        else:
                            Eleme.discard(a[3:6])
            elif i == "6":
                alt_yil, ust_yil = input("Yapilis Yili Bilgisini Filtrelemek Icın Alt Ve Ust Sinirlari Giriniz\n(Sinirlari Girerken "
                                         "Sinirlar Arasinda Lutfen ',' Kullaniniz ve Alt ve Ust sinirlari Sirasiyla Giriniz, Ornek --> 2010,2015)\n---> ").split(",")
                alt_yil = int(alt_yil)
                ust_yil = int(ust_yil)
                Dosya.seek(0)
                for a in Dosya:
                    if a[9:11] == "Ev":
                        Mevcut_yil = int(a[92:96])
                        if alt_yil <= Mevcut_yil and Mevcut_yil <= ust_yil:
                            continue
                        else:
                            Eleme.discard(a[3:6])
    elif Ev_Ar == "2":
        for elma in Dosya:
            if elma[9:14] == "Araba":
                Eleme.add(elma[3:6])

        print("Araba Icın Hangi Filtreleme Seceneklerini Kullanmak Istıyorsanız Seciniz\n(Aynı Anda Birden Fazla Secenek Secmek Icın "
              "Lutfen Sectiginiz Secenekler Arasinda ',' Virgul Kullaniniz, Ornek --> 1,2,3)\n")
        Filtre += input("1)Satilik/Kiralik Durumunu Filtrelemek Icın\n2)Fiyat Bilgisini Filtrelemek Icın\n"
                        "3)Marka Bilgisini Filtrelemek Icin\n4)Model Bilgisini Filtrelemek Icin\n5)Degisen Parca Bilgisini Filtrelemek Icin\n"
                        "6)Boya Bilgisini Filtrelemek Icin\n---> ").split(",")

        for i in Filtre:
            if i == "1":
                print("Filtrelemek Istediginiz Ilan Hangisi?")
                Filt2 = input("1)Satilik\n2)Kiralik\n---> ")
                if Filt2 == "1":
                    Dosya.seek(0)
                    for a in Dosya:
                        if a[9:14] == "Araba" and a[17:24] == "Satilik":
                            continue
                        else:
                            Eleme.discard(a[3:6])
                elif Filt2 == "2":
                    Dosya.seek(0)
                    for a in Dosya:
                        if a[9:14] == "Araba" and a[17:24] == "Kiralik":
                            continue
                        else:
                            Eleme.discard(a[3:6])
            elif i == "2":
                fiyat = ""
                fiyat = str(fiyat)
                alt, ust = input("Ilanlarin Fiyatini Filtrelemek Icın Alt Ve Ust Sinirlari Giriniz\n(Sinirlari Girerken "
                                 "Sinirlar Arasinda Lutfen ',' Kullaniniz ve Alt ve Ust sinirlari Sirasiyla Giriniz,"
                                 "Ayrica Sinirlari Girerken Sayilari '.' Nokta Kullanmadan Direkt Giriniz, Ornek --> 500000,800000)\n---> ").split(",")
                alt = int(alt)
                ust = int(ust)
                Dosya.seek(0)
                for a in Dosya:
                    fiyat = ""
                    if a[9:14] == "Araba":
                        tut1 = a[33:43]
                        for b in tut1:
                            if b != "." and b != " ":
                                fiyat += b
                        fiyat1 = int(fiyat)
                        if alt <= fiyat1 and fiyat1 <= ust:
                            continue
                        else:
                            Eleme.discard(a[3:6])
            elif i == "3":
                MarkaF = input("Marka Bilgisini Filtrelemek Icın Istedigiz Marka Tipini Aynen Giriniz\n(Ornek --> Mercedes)\n---> ")
                while len(MarkaF) < 10:
                    MarkaF += " "

                Dosya.seek(0)
                for a in Dosya:
                    if a[9:14] == "Araba":
                        Mevcut_Marka = a[55:65]
                        if Mevcut_Marka == MarkaF:
                            continue
                        else:
                            Eleme.discard(a[3:6])
            elif i == "4":
                alt_yil, ust_yil = input("Model Bilgisini Filtrelemek Icın Alt Ve Ust Sinirlari Giriniz\n(Sinirlari Girerken "
                                         "Sinirlar Arasinda Lutfen ',' Kullaniniz ve Alt ve Ust sinirlari Sirasiyla Giriniz, Ornek --> 2010,2015)\n---> ").split(",")
                alt_yil = int(alt_yil)
                ust_yil = int(ust_yil)
                Dosya.seek(0)
                for a in Dosya:
                    if a[9:14] == "Araba":
                        Mevcut_yil = int(a[74:78])
                        if alt_yil <= Mevcut_yil and Mevcut_yil <= ust_yil:
                            continue
                        else:
                            Eleme.discard(a[3:6])
            elif i == "5":
                print("Filtrelemek Istediginiz Ilan Hangisi?")
                Filt3 = input("1)Degisen Parca Var\n2)Degisen Parca Yok\n---> ")
                if Filt3 == "1":
                    Dosya.seek(0)
                    for a in Dosya:
                        if a[9:14] == "Araba" and a[89:92] == "Var":
                            continue
                        else:
                            Eleme.discard(a[3:6])
                elif Filt3 == "2":
                    Dosya.seek(0)
                    for a in Dosya:
                        if a[9:14] == "Araba" and a[89:92] == "Yok":
                            continue
                        else:
                            Eleme.discard(a[3:6])
            elif i == "6":
                print("Filtrelemek Istediginiz Ilan Hangisi?")
                Filt4 = input("1)Boya Var\n2)Boya Yok\n---> ")
                if Filt4 == "1":
                    Dosya.seek(0)
                    for a in Dosya:
                        if a[9:14] == "Araba" and a[100:103] == "Var":
                            continue
                        else:
                            Eleme.discard(a[3:6])
                elif Filt4 == "2":
                    Dosya.seek(0)
                    for a in Dosya:
                        if a[9:14] == "Araba" and a[100:103] == "Yok":
                            continue
                        else:
                            Eleme.discard(a[3:6])

    Dosya.seek(0)
    for i in Dosya:
        if i[3:6] in Eleme:
            print(i, end="")
    Dosya.close()

def Piyasa_Bilgilendirme():
    Dosya = open("Main.txt", "r", encoding="UTF-8")
    Piyasa = {"SatilikA" : 0, "KiralikA" : 0, "SATF" : 0, "KATF" : 0, "SatilikE" : 0, "KiralikE" : 0, "SETF" : 0, "KETF" : 0}
    for i in Dosya:
        if i[9:11] == "Ev":
            if i[14:21] == "Satilik":
                Piyasa["SatilikE"] += 1
                fiyat = ""
                tut1 = i[30:40]
                for b in tut1:
                    if b != "." and b != " ":
                        fiyat += b
                fiyat1 = int(fiyat)
                Piyasa["SETF"] += fiyat1
            elif i[14:21] == "Kiralik":
                Piyasa["KiralikE"] += 1
                fiyat = ""
                tut1 = i[30:40]
                for b in tut1:
                    if b != "." and b != " ":
                        fiyat += b
                fiyat1 = int(fiyat)
                Piyasa["KETF"] += fiyat1
        elif i[9:11] == "Ar":
            if i[17:24] == "Satilik":
                Piyasa["SatilikA"] += 1
                fiyat = ""
                tut1 = i[33:43]
                for b in tut1:
                    if b != "." and b != " ":
                        fiyat += b
                fiyat1 = int(fiyat)
                Piyasa["SATF"] += fiyat1
            elif i[17:24] == "Kiralik":
                Piyasa["KiralikA"] += 1
                fiyat = ""
                tut1 = i[33:43]
                for b in tut1:
                    if b != "." and b != " ":
                        fiyat += b
                fiyat1 = int(fiyat)
                Piyasa["KATF"] += fiyat1

    print("----------------------------------------------------------------------")
    print("Piyasadaki Arabalarin Toplam Sayisi: {}".format(Piyasa["SatilikA"]+Piyasa["KiralikA"]))
    print("Piyasadaki Satilik Arabalarin Toplam Sayisi: {}".format(Piyasa["SatilikA"]))
    print("Piyasadaki Kiralik Arabalarin Toplam Sayisi: {}".format(Piyasa["KiralikA"]))
    if Piyasa["SATF"] == 0:
        print("Piyasadaki Satilik Arabalarin Fiyat Ortalamasi: 0")
    else:
        print("Piyasadaki Satilik Arabalarin Fiyat Ortalamasi: {}".format(Piyasa["SATF"] / Piyasa["SatilikA"]))

    if Piyasa["KATF"] == 0:
        print("Piyasadaki Kiralik Arabalarin Fiyat Ortalamasi: 0")
    else:
        print("Piyasadaki Kiralik Arabalarin Fiyat Ortalamasi: {}".format(Piyasa["KATF"] / Piyasa["KiralikA"]))

    if (Piyasa["SATF"]+Piyasa["KATF"]) == 0:
        print("Piyasadaki Tum Arabalarin Fiyat Ortalamasi: 0")
    else:
        print("Piyasadaki Tum Arabalarin Fiyat Ortalamasi: {}".format((Piyasa["SATF"] + Piyasa["KATF"]) / (Piyasa["SatilikA"] + Piyasa["KiralikA"])))

    print("----------------------------------------------------------------------")

    print("Piyasadaki Evlerin Toplam Sayisi: {}".format(Piyasa["SatilikE"] + Piyasa["KiralikE"]))
    print("Piyasadaki Satilik Evlerin Toplam Sayisi: {}".format(Piyasa["SatilikE"]))
    print("Piyasadaki Kiralik Evlerin Toplam Sayisi: {}".format(Piyasa["KiralikE"]))
    if Piyasa["SETF"] == 0:
        print("Piyasadaki Satilik Evlerin Fiyat Ortalamasi: 0")
    else:
        print("Piyasadaki Satilik Evlerin Fiyat Ortalamasi: {}".format(Piyasa["SETF"] / Piyasa["SatilikE"]))

    if Piyasa["KETF"] == 0:
        print("Piyasadaki Kiralik Evlerin Fiyat Ortalamasi: 0")
    else:
        print("Piyasadaki Kiralik Evlerin Fiyat Ortalamasi: {}".format(Piyasa["KETF"] / Piyasa["KiralikE"]))

    if (Piyasa["SETF"] + Piyasa["KETF"]) == 0:
        print("Piyasadaki Tum Evlerin Fiyat Ortalamasi: 0")
    else:
        print("Piyasadaki Tum Evlerin Fiyat Ortalamasi: {}".format((Piyasa["SETF"] + Piyasa["KETF"]) / (Piyasa["SatilikE"] + Piyasa["KiralikE"])))

    print("----------------------------------------------------------------------")
    Dosya.close()








print("~~~~\\\*****Sahibinden.com'a Hosgeldiniz*****///~~~~\n")
print("\\\*****PROGRAMI DOGRU BIR SEKILDE KULLANABILMAK ICIN LUTFEN BUTUN ACIKLAMA METINLERINI OKUYUNUZ*****///\n")
print("Lütfen gerceklestirmek istediginiz islemi seciniz.")

while True:
    print("\n")
    secim = input("----------------------------------------------------------------------\n"
                   "1)Yeni Ilan Ekleme\n2)Ilan Guncelleme\n3)Ilan Silme\n"
                   "----------------------------------------------------------------------\n"
                   "4)Tum Ilanlari Gosterme\n5)Ilanlari Filtreleyip Gosterme\n6)Piyasa Bilgisi Ogrenme\n"
                   "----------------------------------------------------------------------\n"
                   "7)Cıkıs\n"
                   "----------------------------------------------------------------------\n"
                   "---> ")
    if secim == "1":
        Ekleme()
    elif secim == "2":
        Guncelleme()
    elif secim == "3":
        Silme()
    elif secim == "4":
        Listeleme()
    elif secim == "5":
        Filtreleme()
    elif secim == "6":
        Piyasa_Bilgilendirme()
    elif secim == "7":
        exit(0)
