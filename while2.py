# načítavaj čísla dovtedy, pokiaľ ich súčet nepresiahne hodnotu 100.
# Program vypíše hodnotu tohto súčtu a aj počet čísel

cislo=int(input("zadaj mi ciselko: "))
pocet=0
x=cislo
while cislo<=100:
      cislo=int(input("zadaj cislo: "))
      x+=cislo
      pocet+=1
print(cislo)
print(pocet)

cislo=int(input("zadaj cislo: "))
pocet=0
x=cislo
while cislo!=0:
    cislo=int(input("zadaj cislo: "))
    x+=cislo
    pocet+=1
print(x/pocet)
