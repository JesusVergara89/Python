from tkinter import *
from tkinter import messagebox
import sqlite3

def updateUser(id, nombre, password, apellido, direccion, comentarios):
    my_conection = sqlite3.connect("users")
    my_cursor = my_conection.cursor()
    try:
        my_cursor.execute(
            "UPDATE DATOS_USUARIOS SET NOMBRE_USER=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID=?",
            (nombre, password, apellido, direccion, comentarios, id)
        )
        my_conection.commit()
        messagebox.showinfo("CRUD", "Usuario actualizado con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizado el usuario: {e}")
    finally:
        my_conection.close()