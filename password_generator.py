import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_caracters = "!@#$%&*_+-=?~"

def password_generator(
        long_password=12, 
        lowercase_op=True, 
        uppercase_op=True, 
        numbers_op=True, 
        special_caracters_op=True):
    
    """
    Metodo encarfado de generar una contraseña aleatoria.

    :param long_passwrod: Logitud de la contraseña a generar por defecto de 12 caracteres.
    :param lowercase_op: Valida uso de minisculas.
    :param uppercase_op: Valida uso de mayusculas.
    :param numbers_op: Valida uso de numeros.
    :param special_caracters_op: Valida uso de caracteres especiales.
    :return: Restorna un str con una constraseñas segun los parametros definidos.
    """
    
    if long_password < 8:
        raise ValueError("La longitud de la contraseña debe ser mayor a 8 caracteres.")
    if long_password > 20:
        raise ValueError("La longitud de la contraseña debe ser menor a 20 caracteres.")

    caracters = []
    if lowercase_op:
        caracters.append(lowercase)
    if uppercase_op:
        caracters.append(uppercase)
    if numbers_op:
        caracters.append(numbers)
    if special_caracters_op:
        caracters.append(special_caracters)
    if not caracters:
        raise ValueError("No se ha definido ningun tipo de caracter para la contraseña.")
    
    # Genera una contraseña aleatoria
    password = ""
    for i in range(long_password):
        random_list = random.choices(caracters)[0]
        random_caracter = random_list[random.randint(0, len(random_list)-1)]
        password += random_caracter
    return password

# TODO: Construir menu de opciones para el usuario.
if __name__ == "__main__":
    # Saludo
    print("""Bienvenido al generador de contraseñas.\n""")
    
    menu = {
        "Enter": "Generar contraseña",
        "l": "Configurar longitud de la contraseña",
        "m": "Configurar uso de minisculas",
        "M": "Configurar uso de mayusculas",
        "n": "Configurar uso de numeros",
        "s": "Configurar uso de caracteres especiales",
        "q": "Salir"
    }

    # Variables de configuracion
    long_password = 12
    lowercase_op = True
    uppercase_op = True
    numbers_op = True
    special_caracters_op = True

    while True:
        # Imprime el menu
        print("Menu de opciones:")
        for key, value in menu.items():
            print(f"{key}: {value}")
        
        # Solicita al usuario una opcion
        user_input = input("\nSeleccione una opcion: ")
        if user_input == "Enter" or user_input == "":
            # Genera la contraseña
            password = password_generator(long_password, lowercase_op, uppercase_op, numbers_op, special_caracters_op)
            print(f"""
-----------------------------------
Contraseña generada: {password}
-----------------------------------""")
        elif user_input == "l":
            # Configura la longitud de la contraseña
            try:
                long_password = int(input("Ingrese la longitud de la contraseña: (minimo 8, maximo 20) "))
            except ValueError:
                print("Error: La longitud de la contraseña debe ser un numero.")
                continue
            if long_password < 8 or long_password > 20:
                print("Error: La longitud de la contraseña debe ser mayor a 8 y menor a 20.")
                continue
            print(f"Longitud de la contraseña configurada a: {long_password}")
        elif user_input == "m":
            # Configura el uso de minisculas
            lowercase_op = input("¿Usar minisculas? (s/n): ").lower()
            if lowercase_op == "s":
                lowercase_op = True
            elif lowercase_op == "n":
                lowercase_op = False
            else:
                print("Opcion no valida.")
                continue
            print(f"Uso de minisculas configurado a: {lowercase_op}")
        elif user_input == "M":
            # Configura el uso de mayusculas
            uppercase_op = input("¿Usar mayusculas? (s/n): ").lower()
            if uppercase_op == "s":
                uppercase_op = True
            elif uppercase_op == "n":
                uppercase_op = False
            else:
                print("Opcion no valida.")
                continue
            print(f"Uso de mayusculas configurado a: {uppercase_op}")
        elif user_input == "n":
            # Configura el uso de numeros
            numbers_op = input("¿Usar numeros? (s/n): ").lower()
            if numbers_op == "s":
                numbers_op = True
            elif numbers_op == "n":
                numbers_op = False
            else:
                print("Opcion no valida.")
                continue
            print(f"Uso de numeros configurado a: {numbers_op}")
        elif user_input == "s":
            # Configura el uso de caracteres especiales
            special_caracters_op = input("¿Usar caracteres especiales? (s/n): ").lower()
            if special_caracters_op == "s":
                special_caracters_op = True
            elif special_caracters_op == "n":
                special_caracters_op = False
            else:
                print("Opcion no valida.")
                continue
            print(f"Uso de caracteres especiales configurado a: {special_caracters_op}")
        elif user_input == "q":
            # Sale del programa
            break
        else:
            print("Opcion no valida.")

        # Configuraciones definidas por el usuario
        print(f"""
    - Longitud de contraseña: {long_password} 
    - Uso de minisculas (a-z): {lowercase_op}
    - Uso de mayusculas (A-Z): {uppercase_op}
    - Uso de numeros (0-9): {numbers_op}
    - Uso de caracteres especiales (!@#$%&*_+-=?~): {special_caracters_op}\n""")