from tkinter import messagebox
import sqlite3

def conexionBD():
    my_conection = sqlite3.connect("users")
    my_cursor = my_conection.cursor()

    try:
        my_cursor.execute('''
                CREATE TABLE DATOS_USUARIOS (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE_USER VARCHAR(50),
                    PASSWORD VARCHAR(50),
                    APELLIDO VARCHAR(10),
                    DIRECCION VARCHAR(50),
                    COMENTARIOS VARCHAR(100)
                )
            ''')
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")

