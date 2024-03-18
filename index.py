import tkinter as tk
from tkinter import messagebox

def registrar_usuario():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    contraseña = entry_contraseña.get()

    # Aquí iría la lógica para validar los datos del usuario y guardarlos en la base de datos
    
    # Ejemplo de validación simple (no se almacena en la base de datos)
    if nombre.strip() == '' or correo.strip() == '' or contraseña.strip() == '':
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
    else:
        messagebox.showinfo("Éxito", "¡Usuario registrado correctamente!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Registro")

# Crear etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_correo = tk.Label(ventana, text="Correo:")
label_correo.grid(row=1, column=0, padx=10, pady=5)
entry_correo = tk.Entry(ventana)
entry_correo.grid(row=1, column=1, padx=10, pady=5)

label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.grid(row=2, column=0, padx=10, pady=5)
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.grid(row=2, column=1, padx=10, pady=5)

# Botón de registro
btn_registrar = tk.Button(ventana, text="Registrar", command=registrar_usuario)
btn_registrar.grid(row=3, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
