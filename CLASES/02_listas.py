semana=['lunes', 'martes','miercoles','jueves','viernes','sabado','domingo']
horas=[]
for dia in semana:
    hora=int(input("hora de ingreso el dia "+ dia+" es: "))
    horas.append(hora)

for i in range(len(semana)):
    print("el dia "+ semana[i]+" ingreso a las:"+str(horas[i]))
