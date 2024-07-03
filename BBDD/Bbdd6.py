import sqlite3

my_conextion = sqlite3.connect("Gestion_productos")
my_cursor=my_conextion.cursor()

my_cursor.execute("DELETE FROM PRODUCTOS WHERE ID=2")

my_conextion.commit()
my_conextion.close()

#Eliminar un registro, se recomienda hacerlo por el id, que es la clave unica