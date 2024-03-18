class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento, estado, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.prioridad = prioridad

# Ejemplo de uso
tarea_1 = Tarea("Completar proyecto", "Terminar el proyecto de gestión de tareas", "2024-03-25", "Por hacer", "Alta")
tarea_2 = Tarea("Revisar informe", "Revisar y corregir el informe final", "2024-03-28", "Por hacer", "Media")
tarea_3 = Tarea("Preparar presentación", "Preparar la presentación para la reunión de equipo", "2024-03-30", "Por hacer", "Alta")

# Impresión de los detalles de la tarea
print("Detalles de la tarea 1:")
print("Título:", tarea_1.titulo)
print("Descripción:", tarea_1.descripcion)
print("Fecha de vencimiento:", tarea_1.fecha_vencimiento)
print("Estado:", tarea_1.estado)
print("Prioridad:", tarea_1.prioridad)
