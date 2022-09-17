from matplotlib import pyplot as plt
import sympy

def f(x): 
    return x**3

def numericka_derivace(v_bode, krok=0.05):
    return (f(v_bode + krok) - f(v_bode - krok) / (2*krok))
    
def benchmark(v_bode):
    x = [ (1.0 - 0.01*i) for i in range(100) ]
    y = []
    for k in x:
        y.append(numericka_derivace(v_bode, k))
    plt.plot(x, y)
    plt.title("Derivace funkce x^3")
    plt.ylabel("Výsledek numerické derivace")
    plt.xlabel("Velikost kroku")
    plt.show()

if __name__ == '__main__':
    #benchmark(0)
    x = sympy.Symbol("x")
    fce = x**3
    derivace = sympy.diff(fce, x)
    derivace