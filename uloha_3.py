import numpy as np
import matplotlib.pyplot as plt
import time

def nahodna_ostre_diagonalne_dominantni_matice(n):
    """
    Vygeneruje ctvercovou celociselnou matici o rozmerech n x n, ktera je ostre diagonalne dominantni.
    """

    nasobic = 10
    horni_limit_scitance_diagonaly = 2*n*nasobic
    temp_matice = np.random.rand(n, n)                      # vrati nahodnou matici n x n, kazdy prvek v intervalu [0, 1]
    nasobici_matice = np.full((n, n), nasobic)
    pricitaci_matice = np.diag([np.random.randint(n*nasobic, horni_limit_scitance_diagonaly) for _ in range(n)])
    temp_matice = np.multiply(temp_matice, nasobici_matice) # vynasobi kazdy prvek
    temp_matice = np.round(temp_matice, decimals=0)         # zaokrouhli kazdy prvek na cele cislo
    temp_matice = temp_matice + pricitaci_matice            # pricte dostatecne velke cislo k hlavni diagonale, zajisteni dominance
    return temp_matice

def nahodny_vektor(n):
    return nahodna_ostre_diagonalne_dominantni_matice(n)[:,[0]]

def prima_metoda_benchmark(A, B):
    """
    Hleda X takove, ze A.X=B
    A je ctvercova matice a B je vektor pravych stran
    Pouziva ruzne metody na bazi GEM, voli vhodny postup podle velikosti matice a povahy hodnot uvnitr.
    Funkce vrati pouze cas, jak dlouho trval vypocet.
    """

    cas_na_zacatku = time.perf_counter()
    np.linalg.solve(A, B)
    cas_na_konci = time.perf_counter()
    return cas_na_konci - cas_na_zacatku

def iteracni_metoda_benchmark(A, B, pocet_iteraci=25):
    """
    Hleda X takove, ze A.X=B
    A a B jsou 2 ctvercove matice stejnych rozmeru.
    Pouziva moji implementaci Jacobiho metody.
    Funkce vrati pouze cas, jak dlouho trval vypocet.
    Funkce vrati None, pokud matice A nebyla ostre diagonalne dominantni.
    """    

    cas_na_zacatku = time.perf_counter()

    # 1) Rozlozeni matice A na A = D + N
    n = A.shape[0]
    diagonala_jednicek = np.diag([1 for _ in range(n)])
    diagonala_nul = np.ones(n) - diagonala_jednicek
    D = np.multiply(A, diagonala_jednicek)
    N = np.multiply(A, diagonala_nul)

    # 2) stanoveni hloupeho pocatecniho odhadu reseni
    X = np.ones(n)

    # 3) iterovani vztahem x[n+1] = D_inverzni . (B - N . x[n]) az po dosazeni pozadovane presnosti reseni
    for _ in range(pocet_iteraci):
        X = (B - np.dot(N, X)) / D
        X = X.diagonal().transpose()

    cas_na_konci = time.perf_counter()
    return cas_na_konci - cas_na_zacatku

def graficky_benchmark(pocatecni_velikost_matice=2, konecna_velikost_matice=1000, krok_velikosti_matice=1, pocet_rund=20):
    
    casy_Jacobi = []
    casy_GEM = []
    velikosti = range(pocatecni_velikost_matice, konecna_velikost_matice + 1, krok_velikosti_matice)
    pocitadlo_postupu_benchmarku = 0
    pocet_kroku_k_dokonceni_benchmarku = len(velikosti)*pocet_rund

    for velikost_matice in velikosti:

        namerene_casy_Jacobi = []
        namerene_casy_GEM = []

        for _ in range(pocet_rund):

            A = nahodna_ostre_diagonalne_dominantni_matice(velikost_matice)
            B = nahodny_vektor(velikost_matice)

            namerene_casy_Jacobi.append(iteracni_metoda_benchmark(A, B, pocet_iteraci=25))
            namerene_casy_GEM.append(prima_metoda_benchmark(A, B))

            pocitadlo_postupu_benchmarku += 1
            print(f"Hotovo {pocitadlo_postupu_benchmarku} kroku z {pocet_kroku_k_dokonceni_benchmarku}")
        
        casy_Jacobi.append(np.mean(namerene_casy_Jacobi))
        casy_GEM.append(np.mean(namerene_casy_GEM))
    
    plt.plot(velikosti, casy_Jacobi, label='Iterační')
    plt.plot(velikosti, casy_GEM, label='Přímá')     
    plt.legend()   
    plt.show()


if __name__ == '__main__':
    graficky_benchmark()