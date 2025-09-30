# --- PRUEBA SOCIOS (main.py) -----------------------------------------------
from Biblioteca.socios import (
    crear_socio, listar_socios, buscar_socio_por_id,
    actualizar_socio, bajar_socio
)
from Biblioteca.consultas import mostrar_tabla
from Biblioteca import constantes as C
from Biblioteca import storage as ST

def probar_socios():
    # Seed mínimo si la matriz está vacía (no duplica)
    if not ST.M_SOCIOS:
        print("Seedeando socios...")
        print("alta1:", crear_socio("Ana Pérez",  "30123456"))
        print("alta2:", crear_socio("Luis Gómez", "28999888"))
        print("alta3:", crear_socio("Carla Ruiz", "41222333"))

    HEAD = C.ENCABEZADOS_SOCIOS
    NUMS = {C.SOCIO_ID, C.SOCIO_DNI}   # columnas numéricas a la derecha
    BOOL = {C.SOCIO_ACTIVO}            # mostrar True/False como Sí/No

    print("\n== Socios activos ==")
    mostrar_tabla(HEAD, listar_socios(), bool_cols=BOOL, num_cols=NUMS)

    # Lectura/búsqueda
    print("buscar id=1:", buscar_socio_por_id(1))

    # Actualizaciones
    print("actualizar 1 (dni nuevo):", actualizar_socio(1, dni="30123457"))
    print("actualizar 3 (dni duplicado):", actualizar_socio(3, dni="30123457"))  # debe fallar

    # Baja lógica
    print("baja 2:", bajar_socio(2))
    print("baja 2 otra vez:", bajar_socio(2))  # debe avisar que ya estaba de baja

    print("\n== Socios (incluye bajas) ==")
    mostrar_tabla(HEAD, listar_socios(incluir_bajas=True), bool_cols=BOOL, num_cols=NUMS)

if __name__ == "__main__":
    probar_socios()
