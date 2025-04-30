import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_caracters = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"

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

print(password_generator())

# TODO: Construir menu de opciones para el usuario.