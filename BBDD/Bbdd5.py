import sqlite3

my_conextion = sqlite3.connect("Gestion_productos")
my_cursor=my_conextion.cursor()

my_cursor.execute("UPDATE PRODUCTOS SET PRECIO=55 WHERE NOMBRE_ARTICULO='pelota'")

my_conextion.commit()
my_conextion.close()

#actualizar un campo, el precio donde el nombre dle articulo llamado pelota