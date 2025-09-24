from Biblioteca import constantes as C
import Biblioteca.storage as ST
import Biblioteca.validaciones as V

def crear_socio(nombre, dni):
    n = V.normalizar_texto(nombre)
    d = V.normalizar_texto(dni)

    if not V.texto_no_vacio(n):  return (False, "Nombre vacío.")
    if not V.validar_dni(d):     return (False, "DNI inválido (7–8 dígitos).")
    if V.existe_valor(ST.M_SOCIOS, C.SOCIO_DNI, d, col_id=C.SOCIO_ID, col_activo=C.SOCIO_ACTIVO):
        return (False, "DNI ya registrado.")

    nuevo_id = ST.SIGUIENTE_SOCIO_ID; ST.SIGUIENTE_SOCIO_ID += 1
    fila = [None]*(C.SOCIO_ACTIVO+1)
    fila[C.SOCIO_ID]=nuevo_id; fila[C.SOCIO_NOMBRE]=n; fila[C.SOCIO_DNI]=d; fila[C.SOCIO_ACTIVO]=True
    ST.M_SOCIOS.append(fila)
    return (True, nuevo_id)
