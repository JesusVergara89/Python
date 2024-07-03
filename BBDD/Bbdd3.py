import sqlite3

my_conextion = sqlite3.connect("Gestion_productos")

my_cursor=my_conextion.cursor()

my_cursor.execute('''
CREATE TABLE IF NOT EXISTS PRODUCTOS (
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
                  PRECIO INTEGER,
                  SECCION VARCHAR(20)
)
'''
)

productos = [
    ( "pelota", 20, "jugueteria"),
    ( "pantalon", 15, "confeccion"),
    ( "destornillador", 25, "ferreteria"),
    ( "jarron", 45, "ceramica")
]

my_cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)

my_conextion.commit()
my_conextion.close()