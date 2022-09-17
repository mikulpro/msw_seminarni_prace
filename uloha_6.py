import psutil
import pyautogui
from numpy import round
from datetime import datetime
from time import perf_counter

def generuj_semeno():
    a = psutil.cpu_freq().current*10                        # momentalni frekvence CPU
    b = perf_counter()*(10**7)                              # momentalni cas desetinnym cislem
    c = datetime.fromtimestamp(psutil.boot_time()).second   # sekundova cast casu spusteni
    d = psutil.net_io_counters().bytes_recv                 # pocet prijatych Bytu od spusteni
    e = psutil.virtual_memory().available                   # volna pamet v Bytech

    nova_cisla = []
    for cislo in [a, b, c, d, e]:
        pozice_mysi = pyautogui.position()
        temp = None
        if cislo % 2 == 0:
            temp = cislo * pozice_mysi[0]
        else:
            temp = cislo * pozice_mysi[1]
        nova_cisla.append(int(round(temp, decimals=0)))
    
    semeno = 0
    for nove_cislo in nova_cisla:
        semeno += nove_cislo
        semeno = semeno * nove_cislo
        semeno = semeno - int(round(perf_counter()*(10**8), decimals=0))
        semeno = semeno * int(round(perf_counter(), decimals=0))
    
    return semeno

if __name__ == '__main__':
    for i in range(100):
        print(generuj_semeno())