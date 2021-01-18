def result_error(n):
  for i in range(1,n):
    result=i/100*100-i
    if result!=0:
      print(i,result)
n=int(input("Podaj liczbę całkowitą:"))
result_error(n)
##zapisanie programu w funkcji
#Wniosek: Komputer wykonuje działania na systemie binarnym.
#Nie da się z idealną dokładnością zapisać niektórych liczb systemu dziesiętnego za pomocą sumy liczb systemu binarnego, w szczgólności dla małych liczb.
#+ Błąd się powtarza od zmiennej równej 7 co kolejną potęgę dwójki, 7*2^1, 7*2^2, 7*2^3. 
