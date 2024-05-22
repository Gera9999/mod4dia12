import json
from usuario import Usuario

def main():
    usuarios = []
    error_log = "error.log"

    # Intentar abrir el archivo usuarios.txt
    try:
        with open("usuarios.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError as e:
        print(f"El archivo usuarios.txt no se encontró: {str(e)}")
        return

    # Limpiar o crear el archivo error.log
    with open(error_log, "w") as error_file:
        pass

    # Leer cada línea y crear instancias de Usuario
    with open(error_log, "a") as error_file:
        for line in lines:
            try:
                # Intentar cargar la línea como JSON
                user_data = json.loads(line.strip())
                
                # Crear una instancia de Usuario
                usuario = Usuario(
                    nombre=user_data["nombre"],
                    apellido=user_data["apellido"],
                    email=user_data["email"],
                    genero=user_data["genero"]
                )
                usuarios.append(usuario)
            except (KeyError, json.JSONDecodeError) as e:
                error_file.write(f"Error en la línea: {line.strip()} - {str(e)}\n")
            except Exception as e:
                error_file.write(f"Error inesperado en la línea: {line.strip()} - {str(e)}\n")

    # Imprimir las instancias de Usuario creadas
    for usuario in usuarios:
        print(usuario)

if __name__ == "__main__":
    main()
