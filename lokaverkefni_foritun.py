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



    if val == 1:
        if notandi_stokur > tolva_stokur:
            print("þú vanst  þingd",notandi_stokur[0][1],tolva_stokur[0][1])
        elif tolva_stokur > notandi_stokur:
            print("talvan vann  þingd",notandi_stokur[0][1],tolva_stokur[0][1])
        elif notandi_stokur == tolva_stokur:
            print("það var jafntefli  þingd",notandi_stokur[0][1],tolva_stokur[0][1])
    if val ==2:
        if notandi_stokur > tolva_stokur:
            print("þú vanst  mjólkurlangi",notandi_stokur[0][2],tolva_stokur[0][2])
        elif tolva_stokur > notandi_stokur:
            print("talvan vann  mjólkurlangi",notandi_stokur[0][2],tolva_stokur[0][2])
        elif notandi_stokur == tolva_stokur:
            print("það var jafntefli  mjólkurlangi",notandi_stokur[0][2],tolva_stokur[0][2])
    if val ==3:
        if notandi_stokur > tolva_stokur:
            print("þú vanst  einkun ullar",notandi_stokur[0][3],tolva_stokur[0][3])
        elif tolva_stokur > notandi_stokur:
            print("talvan vann  einkun ullar",notandi_stokur[0][3],tolva_stokur[0][3])
        elif notandi_stokur == tolva_stokur:
            print("það var jafntefli  einkun ullar",notandi_stokur[0][3],tolva_stokur[0][3])
    if val ==4:
        if notandi_stokur > tolva_stokur:
            print("þú vanst  einkun",notandi_stokur[0][4],tolva_stokur[0][4])
        elif tolva_stokur > notandi_stokur:
            print("talvan vann  einkun",notandi_stokur[0][4],tolva_stokur[0][4])
        elif notandi_stokur == tolva_stokur:
            print("það var jafntefli  einkun",notandi_stokur[0][4],tolva_stokur[0][4])
    if val ==5:
        if notandi_stokur > tolva_stokur:
            print("þú vanst  einkun læris",notandi_stokur[0][5],tolva_stokur[0][5])
        elif tolva_stokur > notandi_stokur:
            print("talvan vann",notandi_stokur[0][5],tolva_stokur[0][5])
        elif notandi_stokur == tolva_stokur:
            print("það var jafntefli",notandi_stokur[0][5],tolva_stokur[0][5])
    if val ==6:
        if notandi_stokur > tolva_stokur:
            print("þú vanst",notandi_stokur[0][6],tolva_stokur[0][6])
        elif tolva_stokur > notandi_stokur:
            print("talvan vann",notandi_stokur[0][6],tolva_stokur[0][6])
        elif notandi_stokur == tolva_stokur:
            print("það var jafntefli",notandi_stokur[0][6],tolva_stokur[0][6])
    if val ==7:
        if notandi_stokur > tolva_stokur:
            print("þú vanst",notandi_stokur[0][7],tolva_stokur[0][7])
        elif tolva_stokur > notandi_stokur:
            print("talvan vann",notandi_stokur[0][7],tolva_stokur[0][7])
        elif notandi_stokur == tolva_stokur:
            print("það var jafntefli",notandi_stokur[0][7],tolva_stokur[0][7])
    if val ==8:
        if notandi_stokur > tolva_stokur:
            print("þú vanst",notandi_stokur[0][8],tolva_stokur[0][8])
        elif tolva_stokur > notandi_stokur:
            print("talvan vann",notandi_stokur[0][8],tolva_stokur[0][8])
        elif notandi_stokur == tolva_stokur:
            print("það var jafntefli",notandi_stokur[0][8],tolva_stokur[0][8])







