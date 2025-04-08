class Persona:
    def __init__(self, nombre, apellido, fn):
        self.nombre = nombre
        self.apellido = apellido
        self.fn = fn

    def caminar(self):
        print(f"la persona {self.nombre} esta caminando")

class Estudiante(Persona):

    def __init__(self, nombre, apellido, fn, materia, notas):
        super().__init__(nombre, apellido, fn)
        self.materia = materia
        self.notas = notas

    def estudiar(self):
        print(f"el estudiante {self.nombre} esta estudiando {self.materia}")

estudiante1 = Estudiante("Karen", "Sachica", "20/02/2020", "Programacion", [4.2, 3.8, 3,9])
estudiante1.caminar()
estudiante1.estudiar()