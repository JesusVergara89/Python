from tkinter import *
from tkinter import messagebox
import sqlite3

def deleteUser(ID):
     my_conextion = sqlite3.connect("users")
     my_cursor=my_conextion.cursor()
     try:
        my_cursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID=" + ID)

        my_conextion.commit()
        messagebox.showinfo("CRUD", "Usuario borrado con éxito")
     except Exception as e:
        messagebox.showerror("Error", f"Error el id no existe: {e}")
     finally:
        my_conextion.close()