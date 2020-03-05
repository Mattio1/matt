import time

def zmierz(f, n=100):
    """Funkcja mierzy czas wykonania funkcji podanej jako argument dla podanego argumentu"""
    t0=time.time()
    f(n)
    t1=time.time()
    return t1 - t0

def silnia_rek(n):
    if n>1:
        return silnia_rek(n-1)*n
    else:
        return 1
    
def silnia_it(n):
    a=1
    for n in range(1,n-1):
        a = a*n
    return a

print("Silnia rekurencyjnie: ", zmierz(silnia_rek))
print("Silnia iteracyjnie: ", zmierz(silnia_it))