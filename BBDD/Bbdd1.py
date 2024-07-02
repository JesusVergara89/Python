import sqlite3

my_conextion = sqlite3.connect("primera_base")

my_cursor=my_conextion.cursor()

#my_cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#variosProductos = [("pantalon", 24, "ropa"),("vaso",5,"cocina"),("nevera", 230, "cocina")]

#my_cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)

my_cursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=my_cursor.fetchall()

for product in variosProductos:
    print(product)

##my_conextion.commit()

my_conextion.close()