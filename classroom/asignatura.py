class Asignatura:

    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        if self._salon=="remoto":
            return self._nombre + " " + self._salon
        else:
            return self._nombre + " " + self._salon