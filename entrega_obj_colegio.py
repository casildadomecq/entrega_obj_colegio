"""
Queremos crear un programa para un colegio. Todas las personas del colegio tienen nombre y edad, y todas saben presentarse y decir qué hacen en el día a día, pero cada una lo hace de forma diferente.

"""

from abc import ABC, abstractmethod 

class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod  #dice qué tiene que hacer la clase hija pero no como hacerlo, por eso solo pongo pass
    def presentarse(self):
        pass
    @abstractmethod 
    def actividad_diaria(self):
        pass    
    def cumplir_anios(self): #devuelve un mensaje con la nueva edad, da igual si es Alumno o Profesor.
        self.edad+=1 #Se escribe self.edad (y no solo edad) porque edad está guardado como un atributo dentro del propio objeto (self), no como una variable suelta dentro del método cumplir_anios.
        return f"Felicidades {self.nombre}, ya tienes {self.edad} años"

class Alumno(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def presentarse(self):
        print (f"Hola, soy {self.nombre}, tengo {self.edad} años y estoy en {self.curso}.")
    def actividad_diaria(self):
        print (f"{self.nombre} estudia en la UFV.")

class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def presentarse(self):
        print (f"Hola, soy {self.nombre}, tengo {self.edad} años")

    def actividad_diaria(self):
        print (f"{self.nombre} enseña/trabaja en la UFV.")

alumno = Alumno("Casilda", 21, "Primero de BA")
profesor = Profesor("Rufino", 30, "Programación")

print(alumno.presentarse())
print(alumno.actividad_diaria())
print(alumno.cumplir_anios())
print(profesor.presentarse())
print(profesor.actividad_diaria())
print(profesor.cumplir_anios())