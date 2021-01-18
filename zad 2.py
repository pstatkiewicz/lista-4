import matplotlib.pyplot as plt
from math import factorial as fac,exp
def relative_error(x):
    result1=exp(x)
    list_relatives=[]
    for N in range(1,61):
        result2=0
        for i in range(N):
            result2+=(x**i)/fac(i)
        relative_error1=(abs(result1-result2))/result1
        list_relatives.append(relative_error1)
    return list_relatives
list_x=[10,2,-2,-10]
for i in range(len(list_x)):
    plt.plot(list(range(1,61)),relative_error(list_x[i]),"*")
    plt.title("Błąd w zależności od N dla e^"+str(list_x[i]))
    plt.xlabel("N")
    plt.ylabel("Błąd względny")
    plt.show()
##zmienienie tabelki kolumnowej na punktową
#Wniosek: Przy ujemnych x pracujemy na małych liczbach, więc ich dokładność może być zaburzona przez konwersje systemu dziesiętnego na binarny i z powrotem.
#Później, im większy jest stopień przybliżenia tym mniejszy jest błąd.
#+ Im mniejszy jest x, tym mniejszy jest wynik, tym mniejsza jest dokładność.
