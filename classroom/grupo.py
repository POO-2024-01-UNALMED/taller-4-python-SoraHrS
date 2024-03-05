from classroom.asignatura import Asignatura
class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo= grupo
        self._asignaturas= asignaturas or []
        self.listadoAlumnos=estudiantes or []

    def listadoAsignaturas(self, **args):
        for x in args.values():
            asign=Asignatura(x)
            self._asignaturas.append(asign)

    def agregarAlumno(self, alumno, lista=None):
        if type(lista) !=list:
            self.listadoAlumnos.append(alumno)
        else:
            lista.append(alumno)
            self.listadoAlumnos+=lista

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 10"):
    #     cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 4"):
    #     cls.grado = nombre