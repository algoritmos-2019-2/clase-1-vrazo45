#! /user/bin/env/ python3

P = [True, False] #Estoy haciendo variables p y q que contiene los valores verdad o mentira, por eso se ponene en forma de una lista que contenga True y False.
Q = [True, False]

print("Sean P y Q proposiciones l[ogicas") 
print("Ingrese la funci[on de la cual quiera la tabla de verdad")
print("1: And / 2: Or / 3: Not")
OpLog = int(input()) #Estoy asignando a cada uno de los operadores un valor que pueden meter para que se pueda elegir que tabla quiero

if OpLog == 1: #Condiciono, que se ejecute algo si se tecle[o esta opci[on
 for x in range(2): #En la condici[on pido que una variable este en un rando de dos, que este entre los valores 1 y 2, dos son los valores en la lista 
  for y in range(2): #Lo mismpo para y
   print(P[x] and Q[y]) #Pido que opere usando el operador l[ogico and los valoes de las listas p y q, y despu[es mueste ene la pantalla el resultado. Si x estuviera en rango de 1, solo operaria el primer valor.

elif OpLog == 2: #Pido que ejecute esta funci[on en lugar de as otras si se eliguio la opci[on dos.
 for x in range(2):
  for y in range(2):
   print(P[x] or Q[y])#Pido que muestre el resuldo de opoerar los valores de ambas listas, pero esta vez con or.

elif OpLog == 3: 
 for x in range(2):
  print(not P[x]) #En este caso, solo pido que opere con not los dos valores de las lista P si se eligio la opci[on tres

else:
 print("Yo no entiendos :,v") #Para evitar fallos, si no se marca alguna de las opciones de los operadores, que el programa despliegue una cadena de texto. 


