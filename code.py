import tkinter as tk

def agregar_tarea():
  tarea = entrada_tarea.get()
  if tarea:
    lista_tareas.insert(tk.END, tarea)
    entrada_tarea.delete(0, tk.END)

def eliminar_tarea():
  seleccion = lista_tareas.curselection()
  if seleccion:
    lista_tareas.delete(seleccion)

#Crear la ventana proncipal

ventana = tk.Tk()
ventana.title("Lista de tareas")

#Etiqueta y entrada de texto para la tarea
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)

#Boton para agregar tarea
boton_agregar = tk.Button(ventana,
        text="Agregar tarea",
        command=agregar_tarea)
boton_agregar.pack()

#Crear una lista para mostrar las tareas
lista_tareas = tk.Listbox(ventana)
lista_tareas.pack()

#Boton para eliminar tarea
boton_eliminar = tk.Button(ventana,
        text="Eliminar Tarea",
        command=eliminar_tarea)
boton_eliminar.pack()
#Bucle
ventana.mainloop()
