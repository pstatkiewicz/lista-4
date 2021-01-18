import random
from math import sqrt
def sign(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
list_x1=[]
list_x2_1=[]
list_x2_2=[]
a=1
c=1
for i in range(100):
    b=random.uniform(pow(10,7.4),pow(10,8.5))
    x1=(1/(2*a))*(-b-(sign(b))*sqrt((b**2)-4*a*c))
    x2_1=(1/(2*a))*(-b+(sign(b))*sqrt((b**2)-4*a*c))
    x2_2=c/(a*x1)
    list_x1.append(x1)
    list_x2_1.append(x2_1)
    list_x2_2.append(x2_2)
print(list_x1)
print(list_x2_1)
print(list_x2_2)
#Wniosek: Wykonywanie działań na małych liczbach, może być niedokładne z powodu niedokładności w zmienianiu liczb z systemu dziesiętnego na liczby systemu binarnego i z powrotem
#(wynik się zeruje lub przyjmuje takie same wartości dla róznych liczb początkowych).
#W drugim sposobie obliczania x2 mamy po prostu podaną odwrotność x1, co jest o wiele bardziej mniej złożonym działaniem.
    

