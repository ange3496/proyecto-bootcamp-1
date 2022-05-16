from ast import For
import os
from pickle import TRUE
import colorama
from colorama import Fore
from pathlib import Path

carpeta_actual = Path.cwd()

# https://appdividend.com/2022/01/29/how-to-clear-console-in-python/


def clear_console():
    os.system('cls')


def show_content_file(path_file):
    if path_file.is_file() and path_file.exists():
        return path_file.read_text()


def ver_archivo(nombre_archivo):
    if(nombre_archivo.lower().endswith(".txt")):
        path = carpeta_actual / nombre_archivo
        file_contents = show_content_file(path)
        clear_console()
        print("Contenido del archivo " + Fore.CYAN +
              nombre_archivo + Fore.RESET + ":")
        print(Fore.BLUE + file_contents + Fore.RESET)


clear_console()
# https://www.adamsmith.haus/python/answers/how-to-edit-a-file-in-python
print('')
# https://www.makeuseof.com/how-to-include-emojis-in-your-python-code
print('Bienvenido \U0001F642')
while(TRUE):  # https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/
    print('')
    print(Fore.GREEN + 'MENU: ' + Fore.RESET)
    print('')
    print('1. Listar archivos')
    print('2. Ver archivo')
    print('3. Editar archivo')
    print('Salir (Quit or Exit)')
    print('')
    opcion = input('Ingresa una opcion: ')
    clear_console()
    if(opcion == '1'):
        archivos = os.listdir()
        print(Fore.GREEN + 'No. \tNombre  \t Tamaño' + Fore.RESET)
        print('-- \t-------- \t--------')
        for i, archivo in enumerate(archivos):
            # https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
            if archivo.endswith('.txt'):
                info_archivo = os.stat(carpeta_actual / archivo).st_size
                print(str(i + 1) + '\t' + archivo + ' \t ' +
                      str(round(info_archivo / 1024, 2)) + 'Kb')
    if(opcion == '2'):
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        ver_archivo(nombre_archivo)
    if(opcion == '3'):
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        if(nombre_archivo.lower().endswith(".txt")):
            path = carpeta_actual / nombre_archivo
            contenido = show_content_file(path)
            clear_console()
            print("Ingrese el texto que desea añadir al archivo " +
                  Fore.BLUE + nombre_archivo + Fore.RESET + ": ")
            nuevo_contenido = input()
            # https://stackoverflow.com/questions/22402548/default-values-on-empty-user-input
            respuesta = input(
                "Quiere reemplazar el contenido? Si o [No] ") or "No"
            if(respuesta.lower() == 'si'):
                path.write_text(nuevo_contenido)
            else:
                path.write_text(contenido + "\n" + nuevo_contenido)
            clear_console()
            ver_archivo(nombre_archivo)
    if(opcion in ('quit', 'exit')):
        exit()
    # https://www.askpython.com/python/examples/in-and-not-in-operators-in-python
    elif(opcion not in ("1", "2", "3", "quit", "exit")):
        print(Fore.YELLOW + "Opcion no encontrada!" + Fore.RESET)
