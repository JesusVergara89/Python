from tkinter import *
from tkinter import messagebox
import sqlite3

def createUser(NOMBRE_USER,PASSWORD, APELLIDO, DIRECCION, COMENTARIOS):
    my_conection = sqlite3.connect("users")
    my_cursor = my_conection.cursor()
    try:
        my_cursor.execute("INSERT INTO DATOS_USUARIOS VALUES (NULL,?, ?, ?, ?, ?)", 
                          (NOMBRE_USER, PASSWORD, APELLIDO, DIRECCION, COMENTARIOS))
        my_conection.commit()
        messagebox.showinfo("CRUD", "Usuario creado con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"Error al crear el usuario: {e}")
    finally:
        my_conection.close()