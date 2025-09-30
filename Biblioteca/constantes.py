# ======= Columnas de la Matriz LIBROS ========

LIBRO_ID=0
LIBRO_TITULO=1
LIBRO_AUTOR=2
LIBRO_GENERO=3
LIBRO_ANIO=4
LIBRO_TOTALES=5
LIBRO_DISPONIBLE=6
LIBRO_PRESTADOS=7
LIBRO_ACTIVO=8

ENCABEZADOS_LIBROS = ["ID","Título","Autor","Género","Año","Totales","Disp.","Prest.","Activo"]

# ======= Columnas de la Matriz SOCIOS ========

SOCIO_ID     = 0
SOCIO_NOMBRE = 1
SOCIO_DNI    = 2
SOCIO_ACTIVO = 3

ENCABEZADOS_SOCIOS = ["ID","Nombre","DNI","Activo"]

# ======= Columnas de la Matriz PRESTAMOS ========
PRESTAMO_ID              = 0
PRESTAMO_SOCIO_ID        = 1
PRESTAMO_LIBRO_ID        = 2
PRESTAMO_FECHA_SALIDA    = 3
PRESTAMO_FECHA_DEVOL     = 4
PRESTAMO_ACTIVO          = 5

HEADERS_PRESTAMOS = ["ID","SocioID","LibroID","Salida","Devolución","Activo"]
