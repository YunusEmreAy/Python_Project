# Yunus Emre Ay / 21100011016 / Tel: 05516524768 / E-posta: TR.yunus.emre.ay@gmail.com / <3

print("*****YILDIZLARLA ISIM YAZMA PROGRAMINA HOSGELDINIZ*****\n\n")
print("Yildizlarla isim yazma islemini gerceklestirmeden once 'Boyut'u belirlemeniz gerekmektedir.\n")
print("Lutfen 'Boyut'u belirlerken tek sayilari kullaniniz ve en az '5' sayisini kullaniniz. ( Onerilen boyut degeri : 15 )\n")
print("Cift sayi kullandiginiz taktirde girdiginiz sayiya 1 eklenerek isleme devam edilecektir.")
print("5'ten daha kucuk bir sayi kullandiginiz taktirde Boyut=5 alinarak isleme devam edilecektir.\n\n")

Boyut = int(input("Lutfen Boyut'u belirleyiniz --> :"))

if Boyut % 2 == 0:
    Boyut +=1
if  Boyut < 5:
    Boyut = 5

print("\n\nBoyut: {}".format(Boyut))
print("--------------------------------------------------------------------------------\n")
i=0

# Y harfi
while i != Boyut:
    if i < (Boyut-1)/2:
        for a in range(i):
            print(" ",end="")
        print("*",end="")

        for a in range((Boyut-2-(2*i))):
            print(" ",end="")
        print("*")
        i += 1
    else:
        for a in range((Boyut-1)//2):
            print(" ",end="")
        print("*")
        i += 1

i = 0

print("\n\n\n\n")

# U harfi
while i != Boyut:
    if i != Boyut-1:
        print("*",end="")

        for a in range(Boyut-2):
            print(" ",end="")
        print("*")
        i += 1

    else:
        for a in range(Boyut):
            print("*",end="")
        i += 1

i = 0

print("\n\n\n\n")

# N harfi
while i != Boyut:
    if i==0 or i==Boyut-1:
        print("*",end="")

        for a in range(Boyut-2):
            print(" ",end="")
        print("*")
        i += 1

    else:
        print("*",end="")

        for a in range(i-1):
            print(" ",end="")
        print("*",end="")

        for a in range(Boyut-2-i):
            print(" ",end="")
        print("*")
        i += 1

i = 0

print("\n\n\n\n")

# U harfi
while i != Boyut:
    if i != Boyut-1:
        print("*",end="")

        for a in range(Boyut-2):
            print(" ",end="")
        print("*")
        i += 1

    else:
        for a in range(Boyut):
            print("*",end="")
        i += 1

i = 0

print("\n\n\n\n")

# S harfi
while i != Boyut:
    if i==0 or i==(Boyut-1)/2 or i==Boyut-1:
        for a in range(Boyut):
            print("*",end="")
        print("")
        i += 1
    elif 0<i and i<(Boyut-1)/2:
        print("*")
        i += 1
    else:
        for a in range(Boyut-1):
            print(" ",end="")
        print("*")
        i += 1

