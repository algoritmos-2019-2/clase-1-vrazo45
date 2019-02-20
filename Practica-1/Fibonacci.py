#! /user/bin/env python3

n = int(input())#input permite meter le variable que quiero, pero en este caso debe ser una de tipo enetero.
i = 0 #i va a a ser un contador que ir[a aumentado de uno en uno 
a = 1
b = 0
suma = 0 

while i<n: #Limita que el ciclo se repita hasta que el contador i iguale al valor del n[umer ingresado, i est[a solo de control para limitar las vultas del ciclo.
 i = i + 1 # i incrementando de uno en uno.
 suma = a + b #Pido que los valores a y b cuyos valores son los de los primeros t[erminos de la suceci[on de fibonacci  se sumen.
 print(suma) #Despliga el valor de la suma en la pantalla.
 a = b #Le pido a "a" que tome el valor de b, osea que a se vuelva el siguiente t[ermino de la suceci[on
 b = suma #Una vee que "a" se convirti[o en el primer valor de "b", quiero que "b" se vuleva el siguiente t[ernido de la suceci[on despu[es de "a", que en este caso es la suma


 










