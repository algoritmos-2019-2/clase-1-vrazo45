#! /user/bin/env/ python3

n = int(input()) #input permite meter le variable que quiero, pero en este caso debe ser una de tipo enetero.
i = 0 #Dos contadores iniciando en cero
s = 0

while i<n: #Pido que mientras se cumpla la condicion de que el n[umero ingresado sea mayor que el contador, se est[e efecutando la acci[on.
 i = i + 1 #Pido que mientres se cumpla la condici[on, primero al contador i incremente en uno y despu[es despliegue el n[umero en el que va en la pantalla
 print(i)
 s = s + i #Despu[es pido que el contador s incremente su valor sumado el valor en el que va i
 if i==n: #Pido que la siguiente parte del ciclo se comparen el valor ingresado n y el valor del contador, si ambos son iguales...
  print("La suma es")#... pido que se despliegue en la pantallla el valor del contado s
  print(s)
