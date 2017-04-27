import random
#nemendurSigurður Aron Bl. Eggertsson og Þórður Jónatansson
stokkur = []
with open("spil.txt","r") as skra:
    lina = skra.read()
    #print(lina)
    tempstokkur = (lina.split('\n'))
    #stokkur = list(map(int, stokkur))
print(tempstokkur)
for l in tempstokkur:
    spil = l.split(',')
    stokkur.append(spil)
print (stokkur)