#! /user/bin/env/ python3

n = int(input())#input permite meter le variable que quiero, pero en este caso debe ser una de tipo enetero.
i = 0 #Dos contadores iniciando en cero
s = 0

for i in range(1, n):#Esta condici[on limita al ciclo a que se repita mientras que el contador  i est[e dentro de los valores del rango que va de 1 hasta el valor ingresado n
 i = i + 1 #Le dice al contado if que incremente una unidad cad vueta del ciclo.
 print(i)
 s = s + i #Le pido a s que cambi su valor al qe enia mas el valor de contdor i espues del incremento
 if i == n:#Pido que la siguiente parte del ciclo se comparen el valor ingresado n y el valor del contador, si ambos son iguales...
  print(s)#... pido que se despliegue en la pantallla el valor del contado s
