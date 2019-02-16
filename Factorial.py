#! /user/bin/env/ python3

n = int(input()) #input permite meter le variable que quiero, pero en este caso debe ser una de tipo enetero.
i = 0 #i va a a ser un contador que ir[a aumentado de uno en
by = 1 #by es otro contador, en este caso el primer n[umero que va a ser multiplicado para emepzar a desarrollar el factorial, por eso no puede emezar en cero

if n == 0: #Si el n[umero fue cero, quiero que despliegue el valor del cero factorial,0!=1
 by = 1
 print(by)
else: #Si no fue cero, quiero que entre en este ciclo while
 while i<n: #Limita a que el ciclo se repita hasta que llegue i sea igual al n[umero ingresado, i sirve como control de repeticiones.
  i = i + 1
  by = by * i #Esto hace que el valor de i que incrmento en uno se multiplicado por el valor de by del ciclo anterior. 
  if i == n:
   print(by) #Va a desplegar el valor del factorial del n[umero ingresado
 #Empiezo en cero, despies le sumo uno, a ses uno lo multimplico por otro uno, que es el primerer valor 1!, cuendo el ciclo se repita, le pido a i que ahora vle uno que incremnte otra vez, y le pido a by, que ahora vale 1, que sea multiplicado por i, dando 1*2, si el ciclo se repita dar[a (1*2)*3










