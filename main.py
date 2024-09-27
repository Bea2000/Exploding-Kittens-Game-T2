import random

def leer_juego():
    juego = []
    with open("juego.txt", "r") as file:
        for line in file:
            juego.append(line.strip())
    return juego

def escribir_juego(juego):
    with open("output.txt", "w") as file:
        file.write(juego)

data = leer_juego()
respuesta_final = ""
linea = 0
Mazo=data[linea]
linea += 1
Mazo=Mazo.split(",")
totalmazo=0
for x in Mazo:
    totalmazo=totalmazo+1
Jugadores=data[linea]
linea += 1
Jugadores=Jugadores.split(",")
i=0
j=0
total=totalmazo
Cartas1=data[linea]
linea += 1
Cartas1=Cartas1.split(",")
Cartas2=data[linea]
linea += 1
Cartas2=Cartas2.split(",")
Cartas3=data[linea]
linea += 1
Cartas3=Cartas3.split(",")
respuesta=data[linea]
linea += 1
Juego=True
Jugador1=True
Jugador2=True
Jugador3=True
J1=Jugadores[0]
J2=Jugadores[1]
J3=Jugadores[2]
explotados=0
CantidadJ1=6
CantidadJ2=6
CantidadJ3=6
while(i<totalmazo and Juego==True):
    while((respuesta=="Robar" or respuesta=="Jugar") and total!=0 and Juego==True):
        j=j+1
        if(j==1):
            if(Jugador1==True):
                if(respuesta=="Robar"):
                    i=i+1
                    Tirar=True
                    a=Mazo.pop()
                    respuesta_final += f"{Jugadores[0]} ha robado {a}" + "\n"
                    CantidadJ1=CantidadJ1+1
                    if(a=="Exploding Kitten"):
                        respuesta_final += f"{Jugadores[0]} ha explotado" + "\n"
                        Jugador1=False
                        explotados=explotados+1
                        if(explotados==2):
                            Juego=False
                    Cartas1.append(a)
                    total=total-1
                elif(respuesta=="Jugar"):
                    Tirar=True
                    carta_a_jugar=data[linea]
                    linea += 1
                    if(carta_a_jugar=="Skip"):
                        Cartas1.remove("Skip")
                        respuesta_final += f"{Jugadores[0]} ha jugado Skip" + "\n"
                        CantidadJ1=CantidadJ1-1
                    elif(carta_a_jugar=="Favor"):
                        respuesta_final += f"{Jugadores[0]} ha jugado Favor" + "\n"
                        CantidadJ1=CantidadJ1-1
                        Cartas1.remove("Favor")
                        robar=data[linea]
                        linea += 1
                        if(robar==J2):
                            carta_a_robar=data[linea]
                            linea += 1
                            Cartas2.remove(carta_a_robar)
                            Cartas1.append(carta_a_robar)
                            respuesta_final += f"{J1} ha recibido {carta_a_robar} de {J2}" + "\n"
                            j=j-1
                            CantidadJ1=CantidadJ1+1
                            CantidadJ2=CantidadJ2-1
                        elif(robar==J3):
                            carta_a_robar=data[linea]
                            linea += 1
                            Cartas3.remove(carta_a_robar)
                            Cartas1.append(carta_a_robar)
                            respuesta_final += f"{J1} ha recibido {carta_a_robar} de {J3}" + "\n"
                            j=j-1
                            CantidadJ1=CantidadJ1+1
                            CantidadJ3=CantidadJ3-1
                    elif(carta_a_jugar.lower()=="monicat" or carta_a_jugar.lower()=="danicat" or carta_a_jugar.lower()=="tomicat" or carta_a_jugar.lower()=="nicocat"):
                        if(Cartas1.count(carta_a_jugar)>=2):
                            respuesta_final += f"{Jugadores[0]} ha jugado dos {carta_a_jugar}" + "\n"
                            CantidadJ1=CantidadJ1-2
                            Cartas1.remove(carta_a_jugar)
                            Cartas1.remove(carta_a_jugar)
                            robar=data[linea]
                            linea += 1
                            if(robar==J2):
                                carta_a_robar=random.randint(1,CantidadJ2)-1
                                carta_a_robar2=Cartas2[carta_a_robar]
                                Cartas2.pop(carta_a_robar)
                                Cartas1.append(carta_a_robar2)
                                CantidadJ2=CantidadJ2-1
                                CantidadJ1=CantidadJ1+1
                                respuesta_final += f"{J1} ha recibido {carta_a_robar2} de {J2}" + "\n"
                                j=j-1
                            elif(robar==J3):
                                carta_a_robar=random.randint(1,CantidadJ3)-1
                                carta_a_robar2=Cartas3[carta_a_robar]
                                Cartas3.pop(carta_a_robar)
                                Cartas1.append(carta_a_robar2)
                                CantidadJ3=CantidadJ3-1
                                CantidadJ1=CantidadJ1+1
                                respuesta_final += f"{J1} ha recibido {carta_a_robar2} de {J3}" + "\n"
                                j=j-1
                        else:
                            respuesta_final += f"{J1} no tiene suficientes {carta_a_jugar}" + "\n"
                            j=j-1
            else:
                Tirar=False
        elif(j==2):
            if(Jugador2==True):
                if(respuesta=="Robar"):
                    Tirar=True
                    a=Mazo.pop()
                    respuesta_final += f"{Jugadores[1]} ha robado {a}" + "\n"
                    CantidadJ2=CantidadJ2+1
                    if(a=="Exploding Kitten"):
                        respuesta_final += f"{Jugadores[1]} ha explotado" + "\n"
                        Jugador2=False
                        explotados=explotados+1
                        if(explotados==2):
                            Juego=False
                    Cartas2.append(a)
                    total=total-1
                elif(respuesta=="Jugar"):
                    Tirar=True
                    carta_a_jugar=data[linea]
                    linea += 1
                    if(carta_a_jugar=="Skip"):
                        Cartas2.remove("Skip")
                        respuesta_final += f"{Jugadores[1]} ha jugado Skip" + "\n"
                        CantidadJ2=CantidadJ2-1
                    elif(carta_a_jugar=="Favor"):
                        respuesta_final += f"{Jugadores[1]} ha jugado Favor" + "\n"
                        Cartas2.remove("Favor")
                        CantidadJ2=CantidadJ2-1
                        robar=data[linea]
                        linea += 1
                        if(robar==J1):
                            carta_a_robar=data[linea]
                            linea += 1
                            Cartas1.remove(carta_a_robar)
                            Cartas2.append(carta_a_robar)
                            respuesta_final += f"{J2} ha recibido {carta_a_robar} de {J1}" + "\n"
                            j=j-1
                            CantidadJ2=CantidadJ2+1
                            CantidadJ1=CantidadJ1-1
                        elif(robar==J3):
                            carta_a_robar=data[linea]
                            linea += 1
                            Cartas3.remove(carta_a_robar)
                            Cartas2.append(carta_a_robar)
                            respuesta_final += f"{J2} ha recibido {carta_a_robar} de {J3}" + "\n"
                            j=j-1
                            CantidadJ2=CantidadJ2+1
                            CantidadJ3=CantidadJ3-1
                    elif(carta_a_jugar.lower()=="monicat" or carta_a_jugar.lower()=="danicat" or carta_a_jugar.lower()=="tomicat" or carta_a_jugar.lower()=="nicocat"):
                        if(Cartas2.count(carta_a_jugar)>=2):
                            respuesta_final += f"{Jugadores[1]} ha jugado dos {carta_a_jugar}" + "\n"
                            CantidadJ2=CantidadJ2-2
                            Cartas2.remove(carta_a_jugar)
                            Cartas2.remove(carta_a_jugar)
                            robar=data[linea]
                            linea += 1
                            if(robar==J1):
                                carta_a_robar=random.randint(1,CantidadJ1)-1
                                carta_a_robar2=Cartas1[carta_a_robar]
                                Cartas1.pop(carta_a_robar)
                                Cartas2.append(carta_a_robar2)
                                CantidadJ1=CantidadJ1-1
                                CantidadJ2=CantidadJ2+1
                                respuesta_final += f"{J2} ha recibido {carta_a_robar2} de {J1}" + "\n"
                                j=j-1
                            elif(robar==J3):
                                carta_a_robar=random.randint(1,CantidadJ3)-1
                                carta_a_robar2=Cartas3[carta_a_robar]
                                Cartas3.pop(carta_a_robar)
                                Cartas2.append(carta_a_robar2)
                                CantidadJ3=CantidadJ3-1
                                CantidadJ2=CantidadJ2+1
                                respuesta_final += f"{J2} ha recibido {carta_a_robar2} de {J3}" + "\n"
                                j=j-1
                        else:
                            respuesta_final += f"{J2} no tiene suficientes {carta_a_jugar}" + "\n"
                            j=j-1
            else:
                Tirar=False
        elif(j==3):
            if(Jugador3==True):
                if(respuesta=="Robar"):
                    Tirar=True
                    a=Mazo.pop()
                    respuesta_final += f"{Jugadores[2]} ha robado {a}" + "\n"
                    CantidadJ3=CantidadJ3+1
                    if(a=="Exploding Kitten"):
                        respuesta_final += f"{Jugadores[2]} ha explotado" + "\n"
                        Jugador3=False
                        explotados=explotados+1
                        if(explotados==2):
                            Juego=False
                    Cartas3.append(a)
                    total=total-1
                elif(respuesta=="Jugar"):
                    Tirar=True
                    carta_a_jugar=data[linea]
                    linea += 1
                    if(carta_a_jugar=="Skip"):
                        Cartas3.remove("Skip")
                        CantidadJ3=CantidadJ3-1
                        respuesta_final += f"{Jugadores[2]} ha jugado Skip" + "\n"
                    elif(carta_a_jugar=="Favor"):
                        respuesta_final += f"{Jugadores[2]} ha jugado Favor" + "\n"
                        CantidadJ3=CantidadJ3-1
                        Cartas3.remove("Favor")
                        robar=data[linea]
                        linea += 1
                        if(robar==J2):
                            carta_a_robar=data[linea]
                            linea += 1
                            Cartas2.remove(carta_a_robar)
                            Cartas3.append(carta_a_robar)
                            respuesta_final += f"{J3} ha recibido {carta_a_robar} de {J2}" + "\n"
                            j=j-1
                            CantidadJ2=CantidadJ2-1
                            CantidadJ3=CantidadJ3+1
                        elif(robar==J1):
                            carta_a_robar=data[linea]
                            linea += 1
                            Cartas1.remove(carta_a_robar)
                            Cartas3.append(carta_a_robar)
                            respuesta_final += f"{J1} ha recibido {carta_a_robar} de {J1}" + "\n"
                            j=j-1
                            CantidadJ1=CantidadJ1-1
                            CantidadJ3=CantidadJ3+1
                    elif(carta_a_jugar.lower()=="monicat" or carta_a_jugar.lower()=="danicat" or carta_a_jugar.lower()=="tomicat" or carta_a_jugar.lower()=="nicocat"):
                        if(Cartas3.count(carta_a_jugar)>=2):
                            respuesta_final += f"{Jugadores[2]} ha jugado dos {carta_a_jugar}" + "\n"
                            CantidadJ3=CantidadJ3-2
                            Cartas3.remove(carta_a_jugar)
                            Cartas3.remove(carta_a_jugar)
                            robar=data[linea]
                            linea += 1
                            if(robar==J2):
                                carta_a_robar=random.randint(1,CantidadJ2)-1
                                carta_a_robar2=Cartas2[carta_a_robar]
                                Cartas2.pop(carta_a_robar)
                                Cartas3.append(carta_a_robar2)
                                CantidadJ2=CantidadJ2-1
                                CantidadJ3=CantidadJ3+1
                                respuesta_final += f"{J3} ha recibido {carta_a_robar2} de {J2}" + "\n"
                                j=j-1
                            elif(robar==J1):
                                carta_a_robar=random.randint(1,CantidadJ1)-1
                                carta_a_robar2=Cartas1[carta_a_robar]
                                Cartas1.pop(carta_a_robar)
                                Cartas3.append(carta_a_robar2)
                                CantidadJ1=CantidadJ1-1
                                CantidadJ3=CantidadJ3+1
                                respuesta_final += f"{J3} ha recibido {carta_a_robar2} de {J1}" + "\n"
                                j=j-1
                        else:
                            respuesta_final += f"{J3} no tiene suficientes {carta_a_jugar}" + "\n"
                            j=j-1
            else:
                Tirar=False
        else:
            if(Jugador1==True):
                j=1
                if(respuesta=="Robar"):
                    Tirar=True
                    a=Mazo.pop()
                    respuesta_final += f"{Jugadores[0]} ha robado {a}" + "\n"
                    CantidadJ1=CantidadJ1+1
                    if(a=="Exploding Kitten"):
                        respuesta_final += f"{Jugadores[0]} ha explotado" + "\n"
                        Jugador1=False
                        explotados=explotados+1
                        if(explotados==2):
                            Juego=False
                    Cartas1.append(a)
                    total=total-1
                elif(respuesta=="Jugar"):
                    Tirar=True
                    carta_a_jugar=data[linea]
                    linea += 1
                    if(carta_a_jugar=="Skip"):
                        Cartas1.remove("Skip")
                        CantidadJ1=CantidadJ1-1
                        respuesta_final += f"{Jugadores[0]} ha jugado Skip" + "\n"
                    elif(carta_a_jugar=="Favor"):
                        respuesta_final += f"{Jugadores[0]} ha jugado Favor" + "\n"
                        Cartas1.remove("Favor")
                        CantidadJ1=CantidadJ1-1
                        robar=data[linea]
                        linea += 1
                        if(robar==J2):
                            carta_a_robar=data[linea]
                            linea += 1
                            Cartas2.remove(carta_a_robar)
                            Cartas1.append(carta_a_robar)
                            respuesta_final += f"{J1} ha recibido {carta_a_robar} de {J2}" + "\n"
                            j=j-1
                            CantidadJ1=CantidadJ1+1
                            CantidadJ2=CantidadJ2-1
                        elif(robar==J3):
                            carta_a_robar=data[linea]
                            linea += 1
                            Cartas3.remove(carta_a_robar)
                            Cartas1.append(carta_a_robar)
                            respuesta_final += f"{J1} ha recibido {carta_a_robar} de {J3}" + "\n"
                            j=j-1
                            CantidadJ3=CantidadJ3-1
                            CantidadJ1=CantidadJ1+1
                    elif(carta_a_jugar.lower()=="monicat" or carta_a_jugar.lower()=="danicat" or carta_a_jugar.lower()=="tomicat" or carta_a_jugar.lower()=="nicocat"):
                        if(Cartas1.count(carta_a_jugar)>=2):
                            respuesta_final += f"{Jugadores[0]} ha jugado dos {carta_a_jugar}" + "\n"
                            CantidadJ1=CantidadJ1-2
                            Cartas1.remove(carta_a_jugar)
                            Cartas1.remove(carta_a_jugar)
                            robar=data[linea]
                            linea += 1
                            if(robar==J2):
                                carta_a_robar=random.randint(1,CantidadJ2)-1
                                carta_a_robar2=Cartas2[carta_a_robar]
                                Cartas2.pop(carta_a_robar)
                                Cartas1.append(carta_a_robar2)
                                CantidadJ2=CantidadJ2-1
                                CantidadJ1=CantidadJ1+1
                                respuesta_final += f"{J1} ha recibido {carta_a_robar2} de {J2}" + "\n"
                                j=j-1
                            elif(robar==J3):
                                carta_a_robar=random.randint(1,CantidadJ3)-1
                                carta_a_robar2=Cartas3[carta_a_robar]
                                Cartas3.pop(carta_a_robar)
                                Cartas1.append(carta_a_robar2)
                                CantidadJ3=CantidadJ3-1
                                CantidadJ1=CantidadJ1+1
                                respuesta_final += f"{J1} ha recibido {carta_a_robar2} de {J3}" + "\n"
                                j=j-1
                        else:
                            respuesta_final += f"{J1} no tiene suficientes {carta_a_jugar}" + "\n"
                            j=j-1
            else:
                j=1
                Tirar=False
        if(total!=0 and Juego==True and Tirar==True):
            respuesta=data[linea]
            linea += 1
    while(respuesta=="Imprimir Estado" and total!=0 and Juego==True):
        respuesta_final += f"Cartas restantes: {total}" + "\n"
        if(Jugador1==True):
            respuesta_final += f"Mano {J1}: {Cartas1}" + "\n"
        if(Jugador1==False):
            respuesta_final += f"Mano {J1}: KABOOM!" + "\n"
        if(Jugador2==True):
            respuesta_final += f"Mano {J2}: {Cartas2}" + "\n"
        if(Jugador2==False):
            respuesta_final += f"Mano {J2}: KABOOM!" + "\n"
        if(Jugador3==True):
            respuesta_final += f"Mano {J3}: {Cartas3}" + "\n"
        if(Jugador3==False):
            respuesta_final += f"Mano {J3}: KABOOM!" + "\n"
        if(total!=0):
            respuesta=data[linea]
            linea += 1            
respuesta_final += "El juego ha terminado" + "\n"
if(Jugador1==True):
    respuesta_final += f"{J1} ha ganado" + "\n"
elif(Jugador2==True):
    respuesta_final += f"{J2} ha ganado" + "\n"
elif(Jugador3==True):
    respuesta_final += f"{J3} ha ganado" + "\n"
respuesta_final += f"Cartas restantes: {total}" + "\n"
if(Jugador1==True):
    respuesta_final += f"Mano {J1}: {Cartas1}" + "\n"
if(Jugador1==False):
    respuesta_final += f"Mano {J1} : KABOOM!" + "\n"
if(Jugador2==True):
    respuesta_final += f"Mano {J2}: {Cartas2}" + "\n"
if(Jugador2==False):
    respuesta_final += f"Mano {J2}: KABOOM!" + "\n"
if(Jugador3==True):
    respuesta_final += f"Mano {J3}: {Cartas3}" + "\n"
if(Jugador3==False):
    respuesta_final += f"Mano {J3}: KABOOM!" + "\n"
    
escribir_juego(respuesta_final)