import os
import time
from core.animacion_brosgor import animacion_brosgor
from core.cipherbox import CipherBox
import platform

# Función para limpiar la consola
def clear_console():
    operating_system = platform.system()
    if operating_system == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Función para listar archivos en un directorio y seleccionarlos por número
def list_files(directory):
    files = os.listdir(directory)
    if files:
        print("\nArchivos disponibles:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
        selection = int(input("\nSelecciona el número del archivo que deseas: ")) - 1
        if 0 <= selection < len(files):
            return os.path.join(directory, files[selection])
        else:
            print("Selección inválida.")
            return None
    else:
        print("No hay archivos en este directorio.")
        return None

def main_cli():
    data_dir = "data"
    originals_dir = "central"  # Carpeta para archivos sin cifrar
    cipher_box = CipherBox(data_dir)

    # Llama a la animación al inicio del programa
    animacion_brosgor()
    
    # Muestra la descripción del programa
    print("Bienvenido al sistema de cifrado híbrido Brosgor (AES-256 + RSA).")
    print("\nEste programa te permite cifrar y descifrar archivos utilizando un sistema híbrido que combina")
    print("cifrado simétrico AES-256 y cifrado asimétrico RSA. Los archivos cifrados se almacenarán")
    print("con la extensión '.lock' y la clave AES cifrada con la extensión '.key'.")
    print("\nPresiona cualquier tecla para continuar...")

    input()  # Espera a que el usuario presione cualquier tecla

    clear_console()

    while True:
        print("Sistema de cifrado híbrido Brosgor.")

        print("\nSelecciona una opción:")
        print("1. Cifrar un archivo")
        print("2. Descifrar un archivo")
        print("3. Salir")
        
        option = input("Ingresa el número de tu opción: ")

        if option == '1':
            clear_console()
            print("Listando archivos en la carpeta 'central'...")
            source_file = list_files(originals_dir)
            if source_file:
                encrypted_file_name = input("Ingresa el nombre del archivo cifrado (sin extensión): ")
                cipher_box.lock_file(source_file, encrypted_file_name)
                print("\n✅ Archivo cifrado exitosamente.")
            else:
                print("No se pudo seleccionar un archivo para cifrar.")
            input("\nPresiona cualquier tecla para continuar...")  # Pausa antes de continuar

        elif option == '2':
            clear_console()
            print("Listando archivos en la carpeta 'data' (archivos cifrados)...")
            encrypted_file = list_files(data_dir)
            if encrypted_file and encrypted_file.endswith('.lock'):
                decrypted_file_name = input("Ingresa el nombre del archivo descifrado (incluyendo la extensión): ")
                cipher_box.unlock_file(encrypted_file, decrypted_file_name)
                print("\n✅ Archivo descifrado exitosamente.")
            else:
                print("No se pudo seleccionar un archivo para descifrar o el archivo no es válido.")
            input("\nPresiona cualquier tecla para continuar...")  # Pausa antes de continuar

        elif option == '3':
            clear_console()
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción inválida. Por favor, intenta nuevamente.")
            input("\nPresiona cualquier tecla para continuar...")  # Pausa antes de continuar

if __name__ == "__main__":
    main_cli()
