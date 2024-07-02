import sqlite3

my_conextion = sqlite3.connect("primera_base")

my_cursor=my_conextion.cursor()

#my_cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

my_cursor.execute("INSERT INTO PRODUCTOS VALUES('CARRO', 25, 'JUEGUETES')")

my_conextion.commit()

my_conextion.close()