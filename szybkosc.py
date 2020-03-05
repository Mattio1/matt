import time

def zmierz(f, n=100):
    """Funkcja mierzy czas wykonania funkcji podanejjako argument dla podanego argumentu"""
    t0=time.time()
    f(n)
    t1=time.time()
    return t1 - t0

def silnia(n):
    if n>1:
        return silnia(n-1)*n
    else:
        return 1
    

print("Silnia rekurencyjnie: ", zmierz(silnia))