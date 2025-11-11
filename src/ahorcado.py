"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: [Jesús Rodríguez Rodríguez]
Fecha: [7/11/2025]
"""


def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para 'limpiar' la consola
    y que el jugador 2 no vea la palabra introducida
    """
    print("\n" * 50)


def solicitar_palabra():
    """
    Solicita una palabra al jugador 1
    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    Returns:
        str: La palabra a adivinar en mayúsculas
    """
    # TODO: Implementar la función

    palabra = input("¿Cual sera la palabra a adivinar?")

    while len(palabra) <= 5 or not palabra.isalpha():
        palabra = input("¿Cual sera la palabra a adivinar?, tiene que tener al menos 5 caracteres y que todos sean letras.")
    return palabra.upper()


def solicitar_letra(letras_usadas):
    """
    Solicita una letra al jugador 2
    La letra debe ser válida (solo una letra) y no estar ya usada
    
    Args:
        letras_usadas (list): Lista de letras ya introducidas
        
    Returns:
        str: La letra introducida en mayúsculas
    """
    # TODO: Implementar la función

    letra = input("Dime una letra")
    while len(letra) != 1 or not letra.isalpha() or letra in letras_usadas:
        letra = input("Dime una letra")
    return letra.upper()

def mostrar_estado(palabra_oculta, intentos, letras_usadas):
    """
    Muestra el estado actual del juego
    
    Args:
        palabra_oculta (str): La palabra con _ y letras adivinadas
        intentos (int): Número de intentos restantes
        letras_usadas (list): Lista de letras ya usadas
    """
    # TODO: Implementar la función
    print(f"Intentos restantes:{intentos}")
    print(palabra_oculta)
    print(f"Letras usadas:{letras_usadas}")


def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    """
    Actualiza la palabra oculta revelando las apariciones de la letra
    
    Args:
        palabra (str): La palabra completa a adivinar
        palabra_oculta (str): La palabra actual con _ y letras adivinadas
        letra (str): La letra que se ha adivinado
        
    Returns:
        str: La palabra oculta actualizada
    """
    # TODO: Implementar la función
    palabra_oculta_lista = list(palabra_oculta)

    for indice, caracter in enumerate(palabra):
        if caracter == letra:
            palabra_oculta_lista[indice] = letra

    palabra_oculta = ""
    for c in palabra_oculta_lista:
        palabra_oculta += c

    return palabra_oculta

def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    print("=== JUEGO DEL AHORCADO ===\n")
    
    # Configuración inicial
    INTENTOS_MAXIMOS = 5
    
    # TODO: Solicitar la palabra al jugador 1
    palabra = solicitar_palabra()

    
    # TODO: Limpiar la pantalla para que el jugador 2 no vea la palabra
    limpiar_pantalla()
    
    # TODO: Inicializar variables del juego
    palabra_oculta = "_" * len(palabra)
    intentos = INTENTOS_MAXIMOS
    letras_usadas = []
    juego_terminado = False
    
    print("Jugador 2: ¡Adivina la palabra!\n")
    
    # TODO: Bucle principal del juego
    # - Mientras haya intentos y el juego no haya terminado:
    while intentos > 0 and not juego_terminado:
    #   1. Mostrar el estado actual
        mostrar_estado(palabra_oculta, intentos, letras_usadas)
    #   2. Solicitar una letra
        letra = solicitar_letra(letras_usadas)
    #   3. Añadir la letra a letras_usadas
        letras_usadas.append(letra)
    #   4. Si la letra está en la palabra:
        if letra in palabra:
    #      - Actualizar palabra_oculta
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
    #      - Mostrar mensaje de acierto
            print(f"La letra '{letra}' está en la palabra.")
    #      - Si ya no hay '_' en palabra_oculta, el jugador ha ganado
            if "_" not in palabra_oculta:
                juego_terminado = True
    #   5. Si la letra NO está en la palabra:
        else:
    #      - Restar un intento
            intentos -= 1
    #      - Mostrar mensaje de fallo
            print(f"La letra '{letra}' no está en la palabra.")
    
    # TODO: Mostrar mensaje final
    # - Si ganó: mostrar felicitación y la palabra
    # - Si perdió: mostrar mensaje de derrota y la palabra correcta
    print("FIN DE LA PARTIDA")

    if juego_terminado:
        print(f"Has ganado. La palabra era: {palabra}")
    else:
        print(f"Has perdido. La palabra correcta era: {palabra}")
    

def main():
    """
    Punto de entrada del programa
    """
    jugar()
    
    # TODO (Opcional): Preguntar si quiere jugar otra vez
    # jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    # if jugar_otra_vez.lower() == 's':
    #     main()
    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    if jugar_otra_vez.lower() == "s":
        main()


if __name__ == "__main__":
    main()
