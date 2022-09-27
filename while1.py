# načítavaj čísla dovtedy, pokiaľ nenačítaš číslo väčšie ako 100.
# Ak sa to stane, program skončí a vypíše celkový počet načítaných čísel

cislo=int(input("zadaj mi ciselko: "))
pocet=0
while cislo<=100:
      cislo+=1
      pocet+=1
print(pocet)
