# ============================================================
#  ADIVINA EL NÚMERO
#  Juego interactivo donde el computador adivina el número
#  que el usuario ha pensado, usando búsqueda binaria.
#
#  Autor  : Victor Ariel Umatambo Llumiquinga
#  Materia: Lógica de Programación – UIDE
#  Fecha  : Junio 2026
# ============================================================

import time


# ── Constantes del juego ─────────────────────────────────────
LIMITE_INFERIOR = 1
LIMITE_SUPERIOR = 100


# ── Funciones auxiliares ─────────────────────────────────────

def mostrar_bienvenida():
    """Muestra el encabezado y las instrucciones del juego."""
    print("=" * 55)
    print("        🎮  ADIVINA EL NÚMERO  🎮")
    print("=" * 55)
    print(f"  Piensa un número entre {LIMITE_INFERIOR} y {LIMITE_SUPERIOR}.")
    print("  El sistema intentará adivinarlo.")
    print("  Responde con las siguientes opciones:")
    print("    [M] → Mi número es MAYOR que tu suposición")
    print("    [m] → Mi número es MENOR que tu suposición")
    print("    [C] → ¡CORRECTO! Ese es mi número")
    print("=" * 55)
    print()


def obtener_respuesta():
    """
    Solicita la respuesta del usuario y la valida.
    Retorna 'M' (mayor), 'm' (menor) o 'C' (correcto).
    No se usa .upper() para distinguir M mayúscula de m minúscula.
    """
    # Bucle de validación: se repite hasta recibir una respuesta válida
    while True:
        respuesta = input("  Tu respuesta [M / m / C]: ").strip()

        # Condicional para verificar que la entrada sea válida
        if respuesta in ("M", "m", "C", "c"):
            return respuesta
        else:
            print("  ⚠  Opción inválida. Escribe M (mayor), m (menor) o C (correcto).")


def busqueda_binaria(limite_inf, limite_sup):
    """
    Implementa la búsqueda binaria para adivinar el número.

    Parámetros:
        limite_inf (int): límite inferior del rango actual
        limite_sup (int): límite superior del rango actual

    Retorna:
        intentos (int): número de intentos realizados
    """
    intentos = 0  # Contador de intentos

    print("\n  🤔 Ya tengo tu número en mente... ¡Empecemos!\n")
    time.sleep(1)

    # Bucle principal: se repite mientras el rango sea válido
    while limite_inf <= limite_sup:

        # Calcular el punto medio del rango (suposición del sistema)
        suposicion = (limite_inf + limite_sup) // 2
        intentos += 1

        print(f"  [Intento {intentos}] ¿Tu número es {suposicion}?")

        respuesta = obtener_respuesta()

        # Condicional principal: ajusta el rango según la respuesta
        if respuesta in ("C", "c"):
            # El sistema adivinó correctamente
            return intentos

        elif respuesta == "M":
            # El número del usuario es mayor → descartar mitad inferior
            limite_inf = suposicion + 1

        else:  # respuesta == "m"
            # El número del usuario es menor → descartar mitad superior
            limite_sup = suposicion - 1

        # Verificar si el rango se volvió inválido (respuestas contradictorias)
        if limite_inf > limite_sup:
            print("\n  ⚠  Las respuestas parecen contradictorias.")
            print("     Reinicia el juego e intenta de nuevo.\n")
            return -1  # Código de error

    return intentos


def mostrar_resultado(intentos):
    """Muestra el mensaje final según el resultado del juego."""
    print()
    print("=" * 55)

    if intentos == -1:
        # Error por respuestas inconsistentes
        print("  ❌  No se pudo adivinar el número.")
    else:
        print(f"  ✅  ¡Lo logré! Adiviné tu número en {intentos} intento(s).")
        print()

        # Condicional para mensaje según la cantidad de intentos
        if intentos <= 3:
            print("  🏆  ¡Rendimiento EXCELENTE! (≤ 3 intentos)")
        elif intentos <= 5:
            print("  👍  ¡Buen resultado! (4–5 intentos)")
        else:
            print("  🎯  ¡Conseguido! La búsqueda binaria nunca falla.")

    print("=" * 55)


def preguntar_reinicio():
    """Pregunta al usuario si desea jugar otra vez. Retorna True o False."""
    while True:
        opcion = input("\n  ¿Deseas jugar otra vez? [S / N]: ").strip().upper()
        if opcion == "S":
            return True
        elif opcion == "N":
            return False
        else:
            print("  ⚠  Escribe S (sí) o N (no).")


# ── Programa principal ───────────────────────────────────────

def main():
    """Función principal que controla el flujo completo del juego."""

    mostrar_bienvenida()

    # Bucle externo: permite jugar múltiples partidas
    while True:

        print("  Piensa bien tu número y presiona ENTER cuando estés listo...")
        input()

        # Llamada al algoritmo de búsqueda binaria
        intentos = busqueda_binaria(LIMITE_INFERIOR, LIMITE_SUPERIOR)

        # Mostrar resultado de esta partida
        mostrar_resultado(intentos)

        # Condicional: preguntar si el usuario desea reiniciar
        if not preguntar_reinicio():
            print("\n  👋  ¡Hasta la próxima! Gracias por jugar.\n")
            break  # Salir del bucle principal

        # Separador visual antes de la siguiente partida
        print("\n" + "─" * 55 + "\n")
        print("  🔄  Nueva partida — ¡Piensa otro número!\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()