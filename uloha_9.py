import numpy as np
import sympy
from scipy import integrate

pocatek = 0
konec = 5
krok = 0.2

def f(x): 
    return 2*x**5 + 13*x**3 - 12*x**2 + 7*x - 11

def g(x):
    return np.sin(x + 1 + 2*np.pi)

def h(x):
    return np.log10((8*x + 13) / 27)

def analyticke_reseni(funkce):
    integral = 0
    x = pocatek
    i = 0
    while x < konec:
        integral += krok * (funkce(x) + funkce(x+krok)) / 2
        x += krok
    return integral

def vysledky():

    x = np.arange(pocatek, konec+krok, krok)
    y = f(x)
    print("analyticky ", analyticke_reseni(lambda x : f(x)))
    print("trapezoid: ", integrate.trapezoid(y, x=x))
    print("simpson: ", integrate.simpson(y=y, x=x))
    print("romberg: ", integrate.romberg(f, pocatek, konec))
    print("quadrature: ", integrate.quadrature(f, pocatek, konec)[0])

    x = np.arange(pocatek, konec+krok, krok)
    y = g(x)
    print("analyticky ", analyticke_reseni(lambda x : g(x)))
    print("trapezoid: ", integrate.trapezoid(y, x=x))
    print("simpson: ", integrate.simpson(y=y, x=x))
    print("romberg: ", integrate.romberg(g, pocatek, konec))
    print("quadrature: ", integrate.quadrature(g, pocatek, konec)[0])

    x = np.arange(pocatek, konec+krok, krok)
    y = h(x)
    print("analyticky ", analyticke_reseni(lambda x : h(x)))
    print("trapezoid: ", integrate.trapezoid(y, x=x))
    print("simpson: ", integrate.simpson(y=y, x=x))
    print("romberg: ", integrate.romberg(h, pocatek, konec))
    print("quadrature: ", integrate.quadrature(h, pocatek, konec)[0])

def benchmark():

    x = np.arange(pocatek, konec+krok, krok)
    y = f(x)
    print("trapezoid: ", abs(integrate.trapezoid(y, x=x) -  analyticke_reseni(lambda x : f(x))))
    print("simpson: ", abs(integrate.simpson(y=y, x=x) -  analyticke_reseni(lambda x : f(x))))
    print("romberg: ", abs(integrate.romberg(f, pocatek, konec) -  analyticke_reseni(lambda x : f(x))))
    print("quadrature: ", abs(integrate.quadrature(f, pocatek, konec)[0] -  analyticke_reseni(lambda x : f(x))))

    x = np.arange(pocatek, konec+krok, krok)
    y = g(x)
    print("trapezoid: ", abs(integrate.trapezoid(y, x=x) -  analyticke_reseni(lambda x : g(x))))
    print("simpson: ", abs(integrate.simpson(y=y, x=x) -  analyticke_reseni(lambda x : g(x))))
    print("romberg: ", abs(integrate.romberg(g, pocatek, konec) -  analyticke_reseni(lambda x : g(x))))
    print("quadrature: ", abs(integrate.quadrature(g, pocatek, konec)[0] -  analyticke_reseni(lambda x : g(x))))

    x = np.arange(pocatek, konec+krok, krok)
    y = h(x)
    print("trapezoid: ", abs(integrate.trapezoid(y, x=x) -  analyticke_reseni(lambda x : h(x))))
    print("simpson: ", abs(integrate.simpson(y=y, x=x) -  analyticke_reseni(lambda x : h(x))))
    print("romberg: ", abs(integrate.romberg(h, pocatek, konec) -  analyticke_reseni(lambda x : h(x))))
    print("quadrature: ", abs(integrate.quadrature(h, pocatek, konec)[0] -  analyticke_reseni(lambda x : h(x))))


if __name__ == '__main__':
    benchmark()