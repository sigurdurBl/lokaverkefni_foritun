import random
#nemendurSigurður Aron Bl. Eggertsson og Þórður Jónatansson
spila_stokkur = []
with open("hrutaspil.txt","r", encoding="iso-8859-1") as stokkur:

    for line in stokkur:
        spila_stokkur.append(eval(line))
notandi_stokur = []
tolva_stokur = []
random.shuffle(spila_stokkur)
print(spila_stokkur)
for i in range(len(spila_stokkur)):
    if i %2 == 0:
        notandi_stokur.append(spila_stokkur[i])
    else:
        tolva_stokur.append(spila_stokkur[i])

while len(notandi_stokur) != 0 and len(tolva_stokur) != 0:

    print('Spilið þitt er:')
    print("-----------------------------------------")
    print('Nafn:', notandi_stokur[0][0])
    print("-----------------------------------------")
    print("þyngd-1:",notandi_stokur[0][1])
    print("-----------------------------------------")
    print("mjólkurlangi-2:",notandi_stokur[0][2])
    print("-----------------------------------------")
    print("einkun ullar-3:",notandi_stokur[0][3])
    print("-----------------------------------------")
    print("fjöldi afkvæma-4:",notandi_stokur[0][4])
    print("-----------------------------------------")
    print("einkun læris-5:",notandi_stokur[0][5])
    print("-----------------------------------------")
    print("frjósemi-6:",notandi_stokur[0][6])
    print("-----------------------------------------")
    print("gerd/þykkt bakvövar-7:",notandi_stokur[0][7])
    print("-----------------------------------------")
    print("einkun fyrir maltir-8:",notandi_stokur[0][8])
    val = int(input("hvað vilt þu velja"))

    print('Spilið tölvunar er:')
    print("-----------------------------------------")
    print('Nafn:', tolva_stokur[0][0])
    print("-----------------------------------------")
    print("þyngd-1:", tolva_stokur[0][1])
    print("-----------------------------------------")
    print("mjólkurlangi-2:", tolva_stokur[0][2])
    print("-----------------------------------------")
    print("einkun ullar-3:", tolva_stokur[0][3])
    print("-----------------------------------------")
    print("fjöldi afkvæma-4:", tolva_stokur[0][4])
    print("-----------------------------------------")
    print("einkun læris-5:", tolva_stokur[0][5])
    print("-----------------------------------------")
    print("frjósemi-6:", tolva_stokur[0][6])
    print("-----------------------------------------")
    print("gerd/þykkt bakvövar-7:", tolva_stokur[0][7])
    print("-----------------------------------------")
    print("einkun fyrir maltir-8:", tolva_stokur[0][8])

    if notandi_stokur > tolva_stokur:
        print("þú vanst  þingd",notandi_stokur[0][val],tolva_stokur[0][val])
        notandi_stokur.append(tolva_stokur[0])
        notandi_stokur.append(notandi_stokur[0])
    elif tolva_stokur > notandi_stokur:
        print("talvan vann  þingd",notandi_stokur[0][val],tolva_stokur[0][val])
        tolva_stokur.append(tolva_stokur[0])
        tolva_stokur.append(notandi_stokur[0])
    elif notandi_stokur == tolva_stokur:
        print("það var jafntefli  þingd",notandi_stokur[0][val],tolva_stokur[0][val])
    tolva_stokur.remove(tolva_stokur[0])
    notandi_stokur.remove([0])








