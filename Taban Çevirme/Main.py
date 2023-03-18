# Yunus Emre Ay / 21100011016 / TR.yunus.emre.ay@gmail.com / 05516524768 / <3

sayilar = "01"
while True:
      print("Lutfen yapmak istediginiz islemi seciniz:\n\n 1) ikilik tabandan onluk tabana cevirme\n "
      "2) Onluk tabandan ikilik tabana cevirme\n 3) Cikis ")
      x = int(input("--> "))
      if x<1 | x>3:
            continue
      if x==1:
            print("***ikilik tabandan onluk tabana cevirme islemi etkinlestirildi***")
            sayi = input("**Yalnızca 0 ve 1 rakamlarından olusan bir sayi giriniz --> ")
            sayac = 0
            for i in sayi:
                  sayac += 1
            a=0
            while a < sayac :
                  for karakterler in sayi:
                        if karakterler in sayilar:
                              a += 1
                        else:
                              sayi = input("**Yalnızca 0 ve 1 rakamlarından olusan bir sayi giriniz ->")
                              a=0
                              sayac = 0
                              for i in sayi:
                                    sayac += 1
                              break
            sonuc = 0
            sayac -= 1
            for i in sayi:
                  if i == '1':
                        sonuc = sonuc + 2**sayac
                  sayac -= 1

            print("*ikilik tabanda girdiginiz sayinin onluk tabanda karsiligi : {}\n\n".format(sonuc))
      elif x==2:
            print("***Onluk tabandan ikilik tabana cevirme islemi etkinlestirildi***")
            sayi = int(input("**ikilik tabana cevirmek istediginiz sayiyi giriniz --> "))

            toplama = ''
            while sayi != 0:
                  tut = sayi % 2
                  tut = str(tut)
                  toplama = tut + toplama
                  sayi = sayi // 2

            print("*Onluk tabanda girdiginiz sayinin ikilik tabanda karsiligi : {}\n\n".format(toplama))

      elif x==3:
            break
