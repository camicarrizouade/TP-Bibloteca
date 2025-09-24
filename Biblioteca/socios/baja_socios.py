from Biblioteca import constantes as C
import Biblioteca.storage as ST

def bajar_socio(socio_id: int):
    """
    Baja lógica del socio: marca ACTIVO=False.
    Devuelve (True, "Baja OK") o (False, "motivo").
    """
    for i, f in enumerate(ST.M_SOCIOS):
        if f[C.SOCIO_ID] == socio_id:
            if not f[C.SOCIO_ACTIVO]:
                return (False, "El socio ya estaba dado de baja.")
            ST.M_SOCIOS[i][C.SOCIO_ACTIVO] = False
            return (True, "Baja OK")
    return (False, "Socio no encontrado.")
