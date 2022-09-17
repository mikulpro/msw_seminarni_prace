from matplotlib import pyplot as plt
import numpy as np
import random

def vrh():
    return random.randint(1, 100)

def monte_carlo(pocet_opakovani=10000000):
    hody = []
    for _ in range(pocet_opakovani):
        a = vrh()
        b = vrh()
        hody.append(a + b)

    pocty_hodu = {}
    for hod in hody:
        if hod not in pocty_hodu.keys():
            pocty_hodu[hod] = 0
        else:
            pocty_hodu[hod] += 1

    x = []
    y = []
    for klic in pocty_hodu.keys():
        x.append(klic)
        y.append(pocty_hodu[klic])

    plt.bar(x, y)
    plt.xlabel("Součet dvou hodů")
    plt.ylabel("Kolikrát byl hozen")
    plt.show()

if __name__ == '__main__':
    monte_carlo()


    