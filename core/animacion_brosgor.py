import time
import os
from art import text2art

def animacion_brosgor():
    # Generar el logo "BROSGOR" en arte ASCII
    logo = text2art("BROSGOR", font='block')

    # Icono pequeño de un candado
    icono = """
      ____
     |    |
     | [] |
     |____|
      _||_
     |____|
    """

    # Limpiar consola antes de iniciar la animación
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Mostrar el icono con un pequeño retraso
    for linea in icono.splitlines():
        print(linea)
        time.sleep(0.1)  # Ajusta el tiempo para hacer la animación más lenta o rápida

    time.sleep(1)  # Pausa antes de mostrar el logo de BROSGOR
    
    # Mostrar el título "BROSGOR" con efecto de escritura
    for linea in logo.splitlines():
        print(linea)
        time.sleep(0.05)  # Ajusta el tiempo para el efecto de animación de letras

    time.sleep(1)  # Pausa antes de limpiar la pantalla para continuar con el programa

# Ejecutar la animación
animacion_brosgor()
