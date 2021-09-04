#CALCULATER THE TIP

costo = float(input("¿Cuánto fue el gasto?"))
cant = int(input("¿Entre cuantas personas pagaran?"))

tip1= round(costo *0.18)
tip2= round(costo*0.20)
tip3= round(costo*0.25)

total1=round(costo*1.18)
total2=round(costo*1.20)
total3=round(costo*1.25)

t1=round(total1/cant) 
t2=round(total2/cant)
t3=round(total3/cant)

Final1=round(t1)
Final2=round(t2)
Final3=round(t3)

print('\nLISTA DE PROPINAS:\n\n--Gasto--:$',costo,"\n\n1-Propina con el 18%:\n-El 18% equivale a:",tip1,"\nTOTAL: $",total1,"\n-Dividido entre los comensales toca de: $",Final1)
print("\n2-Propina con el 20%:\n-El 20% equivale a:",tip2,"\n-TOTAL: $",total2,"\n-Dividido entre los comensales toca de: $",Final2)
print("\n3-Propina con el 25%:\n-El 25% equivale a:",tip3,"\n-TOTAL: $",total3,"\n-Dividido entre los comensales toca de: $",Final3)

