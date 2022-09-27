# načítavaj čísla dovtedy, pokiaľ ich súčet nepresiahne hodnotu 100.
# Program vypíše hodnotu tohto súčtu a aj počet čísel

cislo=int(input("zadaj mi ciselko: "))
pocet=0
while cislo<=100:
    cislo+=cislo+1
    pocet+=1
print(cislo)
print(pocet)

