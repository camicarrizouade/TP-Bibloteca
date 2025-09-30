from Biblioteca import constantes as C
import Biblioteca.storage as ST
import Biblioteca.validaciones as V

def _idx_por_id(socio_id: int):
    """Devuelve el índice de la fila con ese SOCIO_ID, o -1 si no existe."""
    for i, f in enumerate(ST.M_SOCIOS):
        if f[C.SOCIO_ID] == socio_id:
            return i
    return -1

def _dni_ya_existe(dni: str, excluir_id: int = 0):
    """True si el DNI ya lo usa otro socio ACTIVO (excluye opcionalmente un ID)."""
    s = V.normalizar_texto(dni)
    for f in ST.M_SOCIOS:
        if f[C.SOCIO_DNI] == s and f[C.SOCIO_ID] != excluir_id and f[C.SOCIO_ACTIVO]:
            return True
    return False

def listar_socios(incluir_bajas: bool = False):
    """Devuelve todos si incluir_bajas=True; si no, solo los activos."""
    return ST.M_SOCIOS if incluir_bajas else [f for f in ST.M_SOCIOS if f[C.SOCIO_ACTIVO]]

def buscar_socio_por_id(socio_id: int, incluir_bajas: bool = False):
    """Retorna (índice, fila) si existe (respeta incluir_bajas); si no, (-1, None)."""
    i = _idx_por_id(socio_id)
    if i == -1:
        return -1, None
    f = ST.M_SOCIOS[i]
    return (i, f) if (incluir_bajas or f[C.SOCIO_ACTIVO]) else (-1, None)
