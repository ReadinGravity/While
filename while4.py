# napíš program, ktorý bude načítavať čísla dovtedy pokiiaľ nezadáte nulu.
# Na záver program vypíše aritmetický priemer týchto čísel. Nulu do priemeru nezahrňte

cislo=int(input("zadaj mi ciselko: "))
pocet=0
x=cislo
while cislo!=0:
      cislo=int(input("zadaj ciselko: "))
      x+=cislo
      pocet+=1
print(x/pocet)
