from cProfile import label
from unicodedata import decimal
from matplotlib import pyplot as plt
from numpy import round_ as rd


# pocatecni nacteni souboru do listu
tabulka = []
try:
    soubor = open("mcdonalds_dataset.csv")
    for line in soubor:
        radek = line.split(',')
        tabulka.append(radek)
    soubor.close()

except FileNotFoundError:
    print("Soubor nenalezen.")
    exit()

# graf procentualniho zastoupeni rozbitych automatu dane zemepisne sirky
@staticmethod
def funkcnost_podle_sirky():
    ruzne_sirky = {} # seznam zemepisnych sirek na 1 platne desetinne misto
    for i in range(1, len(tabulka)):
        if rd(float(tabulka[i][0]), decimals=1) not in ruzne_sirky.keys():
            ruzne_sirky[ rd(float(tabulka[i][0]), decimals=1) ] = [tabulka[i][3]]
        else:
            ruzne_sirky[ rd(float(tabulka[i][0]), decimals=1) ].append(tabulka[i][3])

    # priradi kazdemu rozsahu (spolecne 1. desetinne misto) zemepisnych sirek pomer fungujicich automatu
    for delka in ruzne_sirky:
        T = 0
        F = 0
        zastoupeni = None
        for hodnota in ruzne_sirky[delka]:
            if hodnota == 'True':
                T += 1
            else:
                F += 1
        zastoupeni = (T / (F + T))
        ruzne_sirky[delka] = zastoupeni

    x = []
    y = []
    for klic in ruzne_sirky.keys():
        x.append(float(klic))
        y.append(ruzne_sirky[klic])

    plt.bar(x, y)
    plt.show()

@staticmethod
def celkova_funkcnost():

    # spocita pocet fungujicich a pocet rozbitych automatu
    T = 0
    F = 0
    for i in range(1, len(tabulka)):
        if tabulka[i][3] == 'True':
            T += 1
        else:
            F += 1

    plt.title(f"Poměr skutečně rozbitých automatů")
    plt.pie([F, T], labels=[f"Funkční", f"Rozbité"], autopct="%1.1f%%")
    plt.show()

@staticmethod
def aktivni_automaty_v_jednotlivych_statech():
    '''
    Vypise top 10 mest s nejvice neplatnymi stiznostmi
    '''

    # vyziska vsechny staty a jejich pocty automatu
    mesta = {}
    for i in range(1, len(tabulka)):
        if tabulka[i][3] == 'False':
            index = 7
            if tabulka[i][index] not in mesta.keys():
                mesta[tabulka[i][index]] = 1
            else:
                mesta[tabulka[i][index]] += 1
    
    # vytridi top 10 poctu automatu
    x = []
    y = []
    for klic in mesta.keys():
        y.append(mesta[klic])
    y.sort(reverse=True)
    y = y[:10]
    new_y = []
    for hodnota in y:
        new_y.append(hodnota)
        treshold = 0
        for klic in mesta.keys():
            if mesta[klic] == hodnota:
                x.append(klic)
                treshold += 1
                if treshold > 1:
                    new_y.append(hodnota)
    y = new_y

    plt.figure(figsize=(10, 8))
    plt.barh(x, y)
    plt.title(f"TOP 10 měst s neplatnými stížnostmi")
    #plt.xticks(rotation=45, ha="right")
    plt.show()

@staticmethod
def nejvice_stiznosti_v_casech():
    casy = []
    for i in range(1, len(tabulka)):
        temp_text = tabulka[i][-1]
        temp_text = temp_text.split(' ')
        if temp_text[0] == "Checked":
            casy.append(int(temp_text[1]))
        else:
            casy.append(int(temp_text[0]))
    casy.sort()
    
    x = []
    y = []
    prev = None
    for cas in casy:
        if prev != cas:
            x.append(cas)
            y.append(0)
        else:
            y[-1] += 1
        prev = cas

    plt.xlabel("Počet minut od poslední kontroly funkce")
    plt.ylabel("Počet stížností")
    plt.plot(x, y)
    plt.show()

@staticmethod
def mesto_s_nejvice_nefungujicimi_kontrolkami():
    staty = []
    cetnost_nefunkcnich_kontrolek = []
    index_statu = -2
    for i in range(1, len(tabulka)):
        if tabulka[i][index_statu] not in staty:
            staty.append(tabulka[i][index_statu])
    for stat in staty:
        cetnost_nefunkcnich_kontrolek.append(0)
        for i in range(1, len(tabulka)):
            if tabulka[i][index_statu] == stat and tabulka[i][5] == 'broken':
                cetnost_nefunkcnich_kontrolek[-1] += 1
    plt.bar(staty, cetnost_nefunkcnich_kontrolek)
    plt.show()


    

if __name__ == '__main__':
    # funkcnost_podle_sirky()
    # celkova_funkcnost()
    # aktivni_automaty_v_jednotlivych_statech()
    # nejvice_stiznosti_v_casech()
    # mesto_s_nejvice_nefungujicimi_kontrolkami()
    ...