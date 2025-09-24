from Biblioteca import constantes as C
import Biblioteca.validaciones as V
from .socios import buscar_socio_por_id

def actualizar_socio(socio_id, nombre=None, dni=None):
    i, f = buscar_socio_por_id(socio_id, incluir_bajas=True)
    if i == -1: return (False, "Socio no encontrado.")

    if nombre is not None:
        n = V.normalizar_texto(nombre)
        if not V.texto_no_vacio(n): return (False, "Nombre vacío.")
        f[C.SOCIO_NOMBRE] = n

    if dni is not None:
        d = V.normalizar_texto(dni)
        if not V.validar_dni(d): return (False, "DNI inválido (7–8 dígitos).")
        if V.existe_valor(
            matriz=__import__("Biblioteca.storage").storage.M_SOCIOS,
            col_valor=C.SOCIO_DNI, valor=d,
            col_id=C.SOCIO_ID, excluir_id=socio_id, col_activo=C.SOCIO_ACTIVO
        ):
            return (False, "DNI ya registrado.")
        f[C.SOCIO_DNI] = d
    return (True, "OK")
