usuario = input("Introduce el nombre de usuario: ")
clave = input("Introduce la contraseña: ")
if usuario == "admin" and clave == "1234":
    print("Inicio de sesión correcto")
else:
    print("Nombre de usuario incorrecto")