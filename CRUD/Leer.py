from tkinter import *
from tkinter import messagebox
import sqlite3

def readUser(id,screenID,screenName, screenPassword, screenApellido,screenDireccion, cuadroTexto):
    my_conection = sqlite3.connect("users")
    my_cursor = my_conection.cursor()
    #print(NOMBRE_USER,PASSWORD, APELLIDO, DIRECCION, COMENTARIOS)
    try:
        my_cursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID=" + id)
        user_in=my_cursor.fetchall()
        user = user_in[0]
        screenID.set(user[0])
        screenName.set(user[1])
        screenPassword.set(user[2])
        screenApellido.set(user[3])
        screenDireccion.set(user[4])
        cuadroTexto.delete('1.0', END)
        cuadroTexto.insert('1.0', user[5])
        my_conection.commit()
        messagebox.showinfo("CRUD", "Usuario leido con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"Error al leer el usuario: {e}")
    finally:
        my_conection.close()
        