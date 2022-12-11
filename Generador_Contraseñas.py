#!/usr/bin/env python3

#Creado por Martin aka CyberDemon19

import string, signal, sys, random, time, subprocess, os, getpass
from colorama import Fore, Style, init

init()

#Salir
def Salir(sig, frame):
        print(Fore.RED, Style.BRIGHT, "\n\n[!] Saliendo...\n", Fore.RESET)
        sys.exit(0)

signal.signal(signal.SIGINT, Salir)

print (Fore.LIGHTCYAN_EX, Style.BRIGHT, "Este es un generador de contraseñas aleatorias. (Si gustas puedes personalizar la herramienta a tu gusto :D) ", Fore.RESET)
print (Fore.CYAN, Style.BRIGHT, "USO---> !!!Ingrese solo números!!!", Fore.RESET)
time.sleep(2)

#Variables
# Caracteres para generar la contraseña a partir de:
letras = list(string.ascii_letters)
digitos = list(string.digits)
caracteres_especiales = list("!@#$%^&*()?¡¿")
caracteres = list(string.ascii_letters + string.digits + "!@#$%^&*()?¡¿")

#Variable del archivo
print (Fore.CYAN, Style.BRIGHT, "\nIngrese el nombre del archivo para guardar la contraseña: Ejemplo:Facebook\n", Fore.RESET)
archivo = input("")

def generar_contrasena_aleatoria():
	# Longitud deseada de la contraseña
	print (Fore.CYAN, Style.BRIGHT, "\nIngrese la longitud de la contraseña:\n", Fore.RESET)
	longitud = int(input(""))
	# Numero de tipos de caracteres
	print (Fore.CYAN, Style.BRIGHT, "\nIngrese la cantidad de letras para la contraseña:\n", Fore.RESET)
	cantidad_letras = int(input(""))
	print (Fore.CYAN, Style.BRIGHT, "\nIngrese la cantidad de digitos para la contraseña:\n", Fore.RESET)
	cantidad_digitos = int(input(""))
	print (Fore.CYAN, Style.BRIGHT, "\nIngrese la cantidad de caracteres especiales para la contraseña:\n", Fore.RESET)
	cantidad_caracteres_especiales = int(input(""))
	cantidad_caracteres = cantidad_letras + cantidad_digitos + cantidad_caracteres_especiales
	# Verificar la longitud con la suma de caracteres Imprimir Error la cantidad total de caracteres es mayor que la longitud
	if cantidad_caracteres > longitud:
		print(Fore.MAGENTA, Style.BRIGHT, "\nError la cantidad total de caracteres es mayor que la longitud\n", Fore.RESET)
		return
	# Generando la contraseña
	contrasena = []
	# Eligiendo letras al azar 
	for i in range(cantidad_letras):
		contrasena.append(random.choice(letras))
	# Eligiendo digitos al azar
	for i in range(cantidad_digitos):
		contrasena.append(random.choice(digitos))
	# Eligiendo caracteres especiales al azar
	for i in range(cantidad_caracteres_especiales):
		contrasena.append(random.choice(caracteres_especiales))
	# Si el total de caracteres es menor a la longitud de la contraseña agregar al azar hasta completar la longitud
	if cantidad_caracteres < longitud:
		random.shuffle(caracteres)
		for i in range(longitud - cantidad_caracteres):
			contrasena.append(random.choice(caracteres))
	# Mezclando los caracteres de la contraseña
	random.shuffle(contrasena)
	# Convirtiendo la lista a cadenas
	print (Fore.GREEN, Style.BRIGHT, "La contraseña es: ", "".join(contrasena), Fore.RESET)
	with open ('archivos/%s' % archivo, 'w+') as f:
		f.write("".join(contrasena) + '\n')
		f.close()
	encriptar()

def encriptar():
    # Crear variables y comando a ejecutar
    print (Fore.CYAN, Style.BRIGHT, "\nIngrese la contraseña para encriptar:\n", Fore.RESET)
    contrasena_enc = getpass.getpass("")
    comando = f"openssl enc -aes-256-cbc -pbkdf2 -in archivos/{archivo} -out archivos/{archivo}.enc -k {contrasena_enc}"
    
    # Ejecutar el comando
    subprocess.run(comando, shell=True)
    
    # Borrar el archivo original
    os.remove(f"archivos/{archivo}")    

# Invocar la funcion
if __name__ == "__main__":
    generar_contrasena_aleatoria()
