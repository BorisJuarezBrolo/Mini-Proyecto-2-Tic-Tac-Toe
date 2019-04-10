"""
Tic-tac-toe Boris Juárez Brolo Proyecto 3 de Programación 1 
"""

import random
import time



"""
Se define una matriz en forma de lista de rango 9 
"""
matrix = list(range(9))

def linea(letra, uno, dos, tres):
    """
    Se define el criterio ganador, con el caracter o letra alineado en 3 posiciones de la matriz sin interrupción del oponente
    """
    if matrix[uno] == letra and matrix[dos] == letra and matrix[tres] == letra:
        return True

def check_winner(letra):
    """
    Se busca al ganador en todas las posibles combinaciones de victoria. 
    """
    win = False
    if linea(letra, 0, 1, 2):
        win = True
    elif linea(letra, 3, 4, 5):
        win = True
    elif linea(letra, 6, 7, 8):
        win = True
    elif linea(letra, 0, 4, 8):
        win = True
    elif linea(letra, 2, 4, 6):
        win = True
    elif linea(letra, 0, 3, 6):
        win = True
    elif linea(letra, 1, 4, 7):
        win = True
    elif linea(letra, 2, 5, 8):
        win = True
    elif linea(letra, 2, 5, 8):
        win = True

    return win

def matriz_coordenadas():
    """
    Mostrar matriz con coordenadas
    """
    
    print("\n          " + str(matrix[0]) + '     |     ' + str(matrix[1]) + "     |      " + str(matrix[2]))
    print("       -------------------------------")
    print("          " + str(matrix[3]) + '     |     ' + str(matrix[4]) + "     |      " + str(matrix[5]))
    print("       -------------------------------")
    print("          " + str(matrix[6]) + '     |     ' + str(matrix[7]) + "     |      " + str(matrix[8]))

def matriz_vacía():
    """
    Mostrar matriz vacía
    """

    print("          "'     |     '"     |      ")
    print("       -------------------------------")
    print("          " '     |     '"     |      ")
    print("       -------------------------------")
    print("          "'     |     '  "     |      " )

robots = ['ROBONAUT', 
'LEONARDO', 
'KITT', 
'HAL 9000', 
'R.O.B.',
'HAL 9000',
'ROOMBA',
'SLUGBOT',
'ELEKTRO',
'SPARKO',
'SBOT',
'TIC-TAC-BOT',
'AIBO',
'R2D2',
'OPTIMUS PY',
'TURK',
'BUMBLEPY',
'VAUCANSONS DUCK',
'ELSIE',
'PYTHON COP',
'ELMER',
'GORT',
'ALBERT HUBO',
'ROBART',
'C3PO',
'BB8',
'LUKE PYWALKER',
]



while(1):

    
    

    eleccion1=input("Seleccione su inciso a visualizar \n 1. Fase 1 (Competencia entre humanos) \n 2. Fase 2 (Competencia vs BOT) \n 3. Misere Tic Tac Toe Humano  \n Lista de Incisos a continuación 1 / 2 / 3 : '   ")
    
    if eleccion1 == '1':

        matriz_vacía()

        nombre1=str(input("Ingrese nombre para jugador 1 : "))
        nombre2=str(input("Ingrese nombre para jugador 2 : "))

        matriz_coordenadas() 
        
        if random.randint(1, 2) is 1:
            
            while True:

            
                jugador_1 = int(input("\n\nEscoja su siguiente movimiento "+nombre1+": "))
                
                #player
                if matrix[jugador_1] != "X" and matrix[jugador_1] != "O":
                    time.sleep(0.5)
                    matrix[jugador_1] = "X"
                    matriz_coordenadas()
                    if check_winner('X') is True:
                        time.sleep(3)
                        print(nombre1+", Felicidades. Haz ganado")
                        jugador_1 = input("<<<Presione enter para jugar de nuevo>>>")
                        if jugador_1 or not jugador_1:
                            matrix = list(range(9))
                            
                    #jugador_2
                while True:
                    
                    jugador_2 = int(input("\n\nEscoja su siguiente movimiento "+nombre2+": "))
                    
                    if matrix[jugador_2] != "O" and matrix[jugador_2] != "X":
                        time.sleep(0.5)
                        matrix[jugador_2] = "O"
                        matriz_coordenadas()

                        if check_winner('O') is True:
                            time.sleep(3)
                            print(nombre2+" Felicidades. Haz ganado")
                            jugador_1 = input("<<<Presione enter para jugar de nuevo>>>")
                            if jugador_1 or not jugador_1:
                                matrix = list(range(9))
                                break
                        break
                else:
                    print("Not valid")

            else:

                    while True:

                    
                        jugador_2 = int(input("\n\nEscoja su siguiente movimiento "+nombre2+": "))
                        
                        if matrix[jugador_2] != "O" and matrix[jugador_2] != "X":
                            time.sleep(0.5)
                            matrix[jugador_2] = "O"
                            matriz_coordenadas()

                            if check_winner('O') is True:
                                time.sleep(3)
                                print(nombre2+" Felicidades. Haz ganado")
                                jugador_1 = input("<<<Presione enter para jugar de nuevo>>>")
                                if jugador_1 or not jugador_1:
                                    matrix = list(range(9))
                        
                        
                            #jugador_2
                        while True:
                            
                            jugador_1 = int(input("\n\nEscoja su siguiente movimiento "+nombre1+": "))
                            if matrix[jugador_1] != "X" and matrix[jugador_1] != "O":
                                time.sleep(0.5)
                                matrix[jugador_1] = "X"
                                matriz_coordenadas()
                                if check_winner('X') is True:
                                    time.sleep(3)
                                    print(nombre1+", Felicidades. Haz ganado")
                                    jugador_1 = input("<<<Presione enter para jugar de nuevo>>>")
                                    if jugador_1 or not jugador_1:
                                        matrix = list(range(9))
                                        break
                                break
                        else:
                            print("Not valid")
            
    elif eleccion1 == '2':
        matriz_vacía()

        nombre1=str(input("Ingrese nombre para jugador 1 : "))

        robot_deturno = random.choice(robots)


        matriz_coordenadas()   


        if random.randint(1, 2) is 1:

            while True:  
                jugador_1 = int(input("\n\nEscoja su siguiente movimiento "+nombre1+": "))
        
                #player
                if matrix[jugador_1] != "X" and matrix[jugador_1] != "O":
                    time.sleep(0.5)
                    matrix[jugador_1] = "X"
                    
                    matriz_coordenadas() 

                    if check_winner('X') is True:
                        time.sleep(3)
                        print(nombre1+", Felicidades. Haz ganado")
                        jugador_1 = input("<<<Presione enter para jugar de nuevo>>>")
                        if jugador_1 or not jugador_1:
                            matrix = list(range(9))
                            
                    #maquina
                while True:
                    
                    maquina = random.randint(0, 8)
                
                    if matrix[maquina] != "O" and matrix[maquina] != "X":
                        time.sleep(0.5)
                        matrix[maquina] = "O"
                        print(robot_deturno,'ha movido de la siguiente manera')
                        matriz_coordenadas()

                        if check_winner('O') is True:
                            print(robot_deturno+ " Ha ganado. Buena suerte a la próxima")
                            turno_1 = input("<<<Presione enter para jugar de nuevo>>>")
                            if turno_1 or not turno_1:
                                matrix = list(range(9))
                                break
                        break
                else:
                    print("Not valid")

        else:
            while True:

                
                maquina = random.randint(0, 8)
                
                if matrix[maquina] != "O" and matrix[maquina] != "X":
                    time.sleep(0.5)
                    matrix[maquina] = "O"
                    print(robot_deturno,'ha movido de la siguiente manera')
                    matriz_coordenadas() 
                    

                    if check_winner('O') is True:
                        print(robot_deturno+ " Ha ganado. Buena suerte a la próxima")
                        turno_1 = input("<<<Presione enter para jugar de nuevo>>>")
                        if turno_1 or not turno_1:
                            matrix = list(range(9))

                
                
                    #player
                while True:
                    
                    jugador_1 = int(input("\n\nEscoja su siguiente movimiento "+nombre1+": "))
                    if matrix[jugador_1] != "X" and matrix[jugador_1] != "O":
                        time.sleep(0.5)
                        matrix[jugador_1] = "X"
                        matriz_coordenadas()
                        if check_winner('X') is True:
                            time.sleep(3)
                            print(nombre1+", Felicidades. Haz ganado")
                            jugador_1 = input("<<<Presione enter para jugar de nuevo>>>")
                            if jugador_1 or not jugador_1:
                                matrix = list(range(9))
                                break
                        break
                else:
                    print("Not valid")  
    
    elif eleccion1 == '3':
        matriz_vacía()

        nombre1=str(input("Ingrese nombre para jugador 1 : "))
        nombre2=str(input("Ingrese nombre para jugador 2 : "))
            
        matriz_coordenadas()

        if random.randint(1, 2) is 1:

            while True:

                
                jugador_1 = int(input("\n\nEscoja su siguiente movimiento "+nombre1+": "))
                
                #player
                if matrix[jugador_1] != "X" and matrix[jugador_1] != "O":
                    time.sleep(0.5)
                    matrix[jugador_1] = "X"
                    matriz_coordenadas()
                    if check_winner('X') is True:
                        time.sleep(3)
                        print(nombre1+", Lo lamentamos, mejor suerte a la próxima. Haz perdido")
                        jugador_1 = input("<<<Presione enter para jugar de nuevo>>>")
                        if jugador_1 or not jugador_1:
                            matrix = list(range(9))
                            
                    #jugador_2
                while True:
                    
                    jugador_2 = int(input("\n\nEscoja su siguiente movimiento "+nombre2+": "))
                    
                    if matrix[jugador_2] != "O" and matrix[jugador_2] != "X":
                        time.sleep(0.5)
                        matrix[jugador_2] = "O"
                        matriz_coordenadas()

                        if check_winner('O') is True:
                            time.sleep(3)
                            print(nombre2+" Lo lamentamos, mejor suerte a la próxima. Haz perdido")
                            jugador_1 = input("<<<Presione enter para jugar de nuevo>>>")
                            if jugador_1 or not jugador_1:
                                matrix = list(range(9))
                                break
                        break
                else:
                    print("Not valid")

        else:
            while True:

        
                jugador_2 = int(input("\n\nEscoja su siguiente movimiento "+nombre2+": "))
                
                if matrix[jugador_2] != "O" and matrix[jugador_2] != "X":
                    time.sleep(0.5)
                    matrix[jugador_2] = "O"
                    matriz_coordenadas()

                    if check_winner('O') is True:
                        time.sleep(3)
                        print(nombre2+" Lo lamentamos, mejor suerte a la próxima. Haz perdido")
                        jugador_1 = input("<<<Presione enter para jugar de nuevo>>>")
                        if jugador_1 or not jugador_1:
                            matrix = list(range(9))
                
                
                    #jugador_2
                while True:
                    
                    jugador_1 = int(input("\n\nEscoja su siguiente movimiento "+nombre1+": "))
                    if matrix[jugador_1] != "X" and matrix[jugador_1] != "O":
                        time.sleep(0.5)
                        matrix[jugador_1] = "X"
                        matriz_coordenadas()
                        if check_winner('X') is True:
                            time.sleep(3)
                            print(nombre1+", Lo lamentamos, mejor suerte a la próxima. Haz perdido")
                            jugador_1 = input("<<<Presione enter para jugar de nuevo>>>")
                            if jugador_1 or not jugador_1:
                                matrix = list(range(9))
                                break
                        break
                else:
                    print("Not valid")
            