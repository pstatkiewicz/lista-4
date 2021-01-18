from math import sqrt
x=9.8**201
y=10.2**199
z1=sqrt(x**2+y**2)
z2=y*sqrt(pow((x/y),2)+1)
print(z1)
print(z2)
#Wniosek: W pierwszym działaniu podnosimy i tak już ogromne liczby do kolejnej potęgi, co może powodować przekroczenie limitu kompilatora.
#W drugim działaniu x i y są przez siebie dzielone, a iloraz dwóch ogromnych, całkiem podobnych wartościom liczb jest już zdecydowanie mniejszy
#i można na nim normalnie przeprowadzać obliczenia bez prawdopodobieństwa przekroczenia limitu. 
