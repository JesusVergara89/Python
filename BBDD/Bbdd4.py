import sqlite3

my_conextion = sqlite3.connect("Gestion_productos")
my_cursor=my_conextion.cursor()

my_cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confeccion' ")

productos=my_cursor.fetchall()

print(productos)

my_conextion.commit()
my_conextion.close()

#seleccionar un producto, en este caso de la seccion confesion
