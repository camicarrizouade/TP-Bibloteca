from Biblioteca.constantes import *
import Biblioteca.storage as ST
from .libros import buscar_libro_por_id
import Biblioteca.validaciones as V

def actualizar_libro(libro_id, titulo=None, autor=None, genero=None, anio=None, totales=None):
    """
    Edita campos opcionales. Valida con Biblioteca/validaciones.py
    Mantiene: TOTALES = DISPONIBLE + PRESTADOS y TOTALES >= PRESTADOS.
    """
    i, f = buscar_libro_por_id(libro_id, incluir_bajas=True)
    if i == -1:
        return (False, "Libro no encontrado.")

    if titulo is not None:
        t = V.normalizar_texto(titulo)
        if not V.validar_titulo(t): return (False, "Título vacío.")
        f[LIBRO_TITULO] = t

    if autor is not None:
        a = V.normalizar_texto(autor)
        if not V.validar_autor(a): return (False, "Autor vacío.")
        f[LIBRO_AUTOR] = a

    if genero is not None:
        g = V.normalizar_texto(genero)
        if not V.validar_genero(g): return (False, "Género vacío.")
        f[LIBRO_GENERO] = g

    if anio is not None:
        s = V.normalizar_texto(anio)
        if not V.validar_anio(s): return (False, "Año inválido.")
        f[LIBRO_ANIO] = int(s)

    if totales is not None:
        s = V.normalizar_texto(totales)
        if not V.validar_totales(s): return (False, "Totales inválido.")
        nuevo_tot = int(s)
        prestados = f[LIBRO_PRESTADOS]
        if nuevo_tot < prestados:
            return (False, "Totales no puede ser menor que los prestados.")
        f[LIBRO_TOTALES]    = nuevo_tot
        f[LIBRO_DISPONIBLE] = nuevo_tot - prestados

    return (True, "OK")