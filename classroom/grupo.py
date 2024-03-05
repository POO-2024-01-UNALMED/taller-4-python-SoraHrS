from classroom.asignatura import Asignatura

class Grupo:
    grado = 12

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        if estudiantes in None:
            estudiantes = []
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos.append(lista)

    def __str__(self):
        return "Grupo de estudiantes: grupo predeterminado"

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre