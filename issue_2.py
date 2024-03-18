import tkinter as tk
from tkinter import messagebox

def iniciar_sesion():
    correo = entry_correo.get()
    contraseña = entry_contraseña.get()

    # Aquí iría la lógica para validar las credenciales del usuario
    # Por simplicidad, supongamos que se trata de un usuario estándar "usuario" y contraseña "contraseña"

    if correo == "usuario" and contraseña == "contraseña":
        messagebox.showinfo("Inicio de Sesión", "¡Inicio de sesión exitoso!")
    else:
        messagebox.showerror("Inicio de Sesión", "Credenciales incorrectas. Inténtalo de nuevo.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")

# Crear etiquetas y campos de entrada
label_correo = tk.Label(ventana, text="Correo electrónico:")
label_correo.grid(row=0, column=0, padx=10, pady=5)
entry_correo = tk.Entry(ventana)
entry_correo.grid(row=0, column=1, padx=10, pady=5)

label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.grid(row=1, column=0, padx=10, pady=5)
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.grid(row=1, column=1, padx=10, pady=5)

# Botón de inicio de sesión
btn_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
btn_iniciar_sesion.grid(row=2, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
