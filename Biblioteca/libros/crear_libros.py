from Biblioteca.constantes import *
import Biblioteca.storage as ST
import Biblioteca.libros.libros as _idx_por_id



def crear_libro(titulo, autor, genero, anio, totales):
    """
    Crea un libro en M_LIBROS (matriz).
    Valida mínimos (no vacíos, enteros > 0) y arma la fila:
      [ID, TITULO, AUTOR, GENERO, ANIO, TOTALES, DISPONIBLE, PRESTADOS, ACTIVO]
    Invariantes iniciales:
      DISPONIBLE = TOTALES, PRESTADOS = 0, ACTIVO = True.
    Devuelve:
      (True, id_nuevo) si ok, o (False, "mensaje de error") si falla validación.
    """
    t = (titulo or "").strip()
    a = (autor or "").strip()
    g = (genero or "").strip()
    s_anio = str(anio).strip()
    s_tot  = str(totales).strip()

    if not t: return (False, "Título vacío.")
    if not a: return (False, "Autor vacío.")
    if not g: return (False, "Género vacío.")
    if not (s_anio.isdigit() and int(s_anio) > 0): return (False, "Año debe ser entero > 0.")
    if not (s_tot.isdigit()  and int(s_tot)  > 0): return (False, "Totales debe ser entero > 0.")

    anio_v = int(s_anio)
    tot_v  = int(s_tot)

    nuevo_id = ST.SIGUIENTE_LIBRO_ID
    ST.SIGUIENTE_LIBRO_ID += 1

    fila = [None] * (LIBRO_ACTIVO + 1)
    fila[LIBRO_ID]          = nuevo_id
    fila[LIBRO_TITULO]      = t
    fila[LIBRO_AUTOR]       = a
    fila[LIBRO_GENERO]      = g
    fila[LIBRO_ANIO]        = anio_v
    fila[LIBRO_TOTALES]     = tot_v
    fila[LIBRO_DISPONIBLE]  = tot_v      # arranca todo disponible
    fila[LIBRO_PRESTADOS]   = 0          # nadie prestado
    fila[LIBRO_ACTIVO]      = True       # baja lógica

    ST.M_LIBROS.append(fila)
    return (True, nuevo_id)
