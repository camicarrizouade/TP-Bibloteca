# MATRICES + contador
# Fila LIBRO: [id, titulo, autor, genero, anio, totales, disponible, prestados, activo]

M_LIBROS = [
    [1,  "El Aleph",                         "Jorge Luis Borges",        "Cuento",          1949, 3, 2, 1, True],
    [2,  "Rayuela",                           "Julio Cortázar",           "Novela",          1963, 5, 5, 0, True],
    [3,  "Cien años de soledad",              "Gabriel García Márquez",   "Novela",          1967, 4, 2, 2, True],
    [4,  "Ficciones",                         "Jorge Luis Borges",        "Cuento",          1944, 2, 2, 0, True],
    [5,  "El túnel",                          "Ernesto Sábato",           "Novela",          1948, 3, 2, 1, True],
    [6,  "La invención de Morel",             "Adolfo Bioy Casares",      "Novela",          1940, 2, 2, 0, True],
    [7,  "Pedro Páramo",                      "Juan Rulfo",               "Novela",          1955, 2, 1, 1, True],
    [8,  "1984",                              "George Orwell",            "Distopía",        1949, 4, 1, 3, True],
    [9,  "La historia interminable",          "Michael Ende",             "Fantasía",        1979, 3, 3, 0, True],
    [10, "Fundación",                         "Isaac Asimov",             "Ciencia Ficción", 1951, 5, 3, 2, True],
    [11, "El nombre de la rosa",              "Umberto Eco",              "Misterio",        1980, 2, 1, 1, False],  # ejemplo de baja lógica
    [12, "Crónica de una muerte anunciada",   "Gabriel García Márquez",   "Novela",          1981, 3, 2, 1, True],
    [13, "La ciudad y los perros",            "Mario Vargas Llosa",       "Novela",          1963, 2, 2, 0, True],
    [14, "El hobbit",                         "J. R. R. Tolkien",         "Fantasía",        1937, 5, 1, 4, True],
    [15, "La tregua",                         "Mario Benedetti",          "Novela",          1960, 3, 3, 0, True],
]

SIGUIENTE_LIBRO_ID = 16