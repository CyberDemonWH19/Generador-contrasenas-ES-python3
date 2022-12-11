#!/usr/bin/env python3
#coding: utf-8

import os, subprocess, time, getpass
from colorama import Fore, init, Style

#Esto permite poner colores
init()

#Imprimir funcionalidad
print (Fore.CYAN, Style.BRIGHT, "\nEsto le ayudará a buscar la contraseña creada con el generador mediante el nombre y pondrá su contenido en pantalla\n", Fore.RESET)
print (Fore.CYAN, Style.BRIGHT, "\nIngrese el nombre de archivo de la contraseña:\n", Fore.RESET)
a=input("")
print (Fore.CYAN, Style.BRIGHT, "\nIngrese la contraseña que utilizó para encriptar:\n", Fore.RESET)
contrasena_enc = getpass.getpass("")

#Funciones
def desencriptar():    
    # Crear una variable con el comando que se desea ejecutar
    comando = f"openssl enc -aes-256-cbc -pbkdf2 -d -in archivos/{a}.enc -out archivos/{a} -k {contrasena_enc}"    
    # Ejecutar el comando
    subprocess.run(comando, shell=True)
    
    # Borrar el archivo encriptado
    os.remove(f"archivos/{a}.enc")
    
    buscar_archivo()

#Función que busca el archivo y muestra su contenido
def buscar_archivo():
    #Aqui debes poner la ruta donde guardas las contraseñas
    with open('archivos/%s' % a, 'r') as archivo:
        for linea in archivo:
            print (Fore.GREEN, Style.BRIGHT, "\nEsta es la contraseña: " + linea, Fore.RESET)
    time.sleep(3)
    comando = f"openssl enc -aes-256-cbc -pbkdf2 -in archivos/{a} -out archivos/{a}.enc -k {contrasena_enc}"
    
    # Ejecutar el comando
    subprocess.run(comando, shell=True)
    
    # Borrar el archivo original
    os.remove(f"archivos/{a}")    

#Si tienes permisos root invocar la función
if os.geteuid()==0:
    desencriptar()
else:
    print (Fore.RED, Style.BRIGHT, "\n[!] Aviso debes ser root para leer las contraseñas y saber la clave", Fore.RESET)
