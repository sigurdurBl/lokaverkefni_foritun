import random
#nemendurSigurður Aron Bl. Eggertsson og Þórður Jónatansson
spila_stokkur = []
temp_stokur = []
teljari = 0
with open("hrutaspil.txt","r", encoding="iso-8859-1") as stokkur:

    for line in stokkur:
        spila_stokkur.append(eval(line))
notandi_stokur = []
tolva_stokur = []
random.shuffle(spila_stokkur)
for i in range(len(spila_stokkur)):
    if i %2 == 0:
        notandi_stokur.append(spila_stokkur[i])
    else:
        tolva_stokur.append(spila_stokkur[i])

while len(notandi_stokur) != 0 and len(tolva_stokur) != 0:
    teljari = teljari +1
    if teljari %2 != 0:
        print("þetta er þín umferð")
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
        print("-----------------------------------------")
        val = int(input("hvað vilt þu velja? "))
        print("-----------------------------------------")
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
        print("-----------------------------------------")
    else:
        print("-----------------------------------------")
        print("þetta er  umferð tölvuna")
        print()
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
        print()
        val = random.randint(1, 8)
        print("Tölvan valdi", val)
        print('Spilið þitt er:')
        print("-----------------------------------------")
        print('Nafn:', notandi_stokur[0][0])
        print("-----------------------------------------")
        print("þyngd-1:", notandi_stokur[0][1])
        print("-----------------------------------------")
        print("mjólkurlangi-2:", notandi_stokur[0][2])
        print("-----------------------------------------")
        print("einkun ullar-3:", notandi_stokur[0][3])
        print("-----------------------------------------")
        print("fjöldi afkvæma-4:", notandi_stokur[0][4])
        print("-----------------------------------------")
        print("einkun læris-5:", notandi_stokur[0][5])
        print("-----------------------------------------")
        print("frjósemi-6:", notandi_stokur[0][6])
        print("-----------------------------------------")
        print("gerd/þykkt bakvövar-7:", notandi_stokur[0][7])
        print("-----------------------------------------")
        print("einkun fyrir maltir-8:", notandi_stokur[0][8])
        print()


    if notandi_stokur[0][val] > tolva_stokur[0][val]:
        print("þú vanst","þetta er þit spil :",notandi_stokur[0][val],"þetta er spil tölvunar :",tolva_stokur[0][val])
        notandi_stokur.append(tolva_stokur[0])
        notandi_stokur.append(notandi_stokur[0])
        if len(temp_stokur) > 0:
            for x in temp_stokur:
                notandi_stokur.append(x)
            temp_stokur.clear()
    elif tolva_stokur[0][val] > notandi_stokur[0][val]:
        print("talvan vann","þetta er þit spil :",notandi_stokur[0][val],"þetta er spil tölvunar :",tolva_stokur[0][val])
        tolva_stokur.append(tolva_stokur[0])
        tolva_stokur.append(notandi_stokur[0])
        for x in temp_stokur:
            tolva_stokur.append(x)
        temp_stokur.clear()

    elif notandi_stokur[0][val] == tolva_stokur[0][val]:
        print("það var jafntefli","þú vanst","þetta er þit spil :",notandi_stokur[0][val],"þetta er spil tölvunar :",tolva_stokur[0][val])
        temp_stokur.append(notandi_stokur[0])
        temp_stokur.append(tolva_stokur[0])

    tolva_stokur.remove(tolva_stokur[0])
    notandi_stokur.remove(notandi_stokur[0])
    print("þú á svona mörg spil efitr", len(notandi_stokur))
    print("talvan á svona mörg spil efitr", len(tolva_stokur))
    input("sláðu á Enter til að halda áfram")









