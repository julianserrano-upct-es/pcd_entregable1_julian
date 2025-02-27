from enum import Enum
import pytest

class Asignatura():
    """
    Clase que representa una asignatura.

    Atributos:
    - nombre (str): El nombre de la asignatura.
    - curso (str): El curso donde se imparte la asignatura.
    - cuatrimestre (str): El cuatrimestre donde se imparte la asignatura.
    - creditos (int): El número de créditos de la asignatura.
    """

    def __init__(self, nombre, curso, cuatrimestre, creditos):
        self._nombre = nombre
        self._curso = curso
        self._cuatrimestre = cuatrimestre
        self._creditos = creditos

    def __str__(self):
        return f"nombre:{self._nombre}, curso:{self._curso} creditos:{self._creditos}"
    
    def getnombre(self):
        return self._nombre

class Persona():
    """
    Clase que representa a una persona. Usada principalmente como clase base para Estudiante y Profesor.

    Atributos:
    - nombre (str): El nombre de la persona.
    - sexo (str): El sexo de la persona.
    - dni (str): El DNI de la persona.
    - direccion (str): La dirección de la persona.
    """

    def __init__(self, nombre, sexo, dni, direccion):
        if not all(isinstance(i, str) for i in [nombre, sexo, dni, direccion]):
            raise TypeError("Las variables tienen que ser un string")
        self._nombre = nombre
        self._sexo = sexo
        self._dni = dni
        self._direccion = direccion
    
    def getdni(self):
        return self._dni
    
    def getnombre(self):
        return self._nombre
    
class Estudiante(Persona):
    """
    Clase que representa a un estudiante. Hereda de Persona.

    Atributos:
    - curso (str): El curso del estudiante.
    - num_expediente (str): El número de expediente del estudiante.
    - asignaturas (list): La lista de asignaturas que esta matriculado el estudiante.
    """

    def __init__(self, nombre, sexo, dni, direccion, curso, num_expediente, asignaturas):
        super().__init__(nombre, sexo, dni, direccion)
        self._curso = curso
        self._num_expediente = num_expediente
        self._asignaturas = asignaturas

    def __str__(self):
        return f"nombre:{self._nombre}, expediente:{self._num_expediente}, asignaturas:{self._asignaturas}"
    
    def agregar_asignatura(self, asignatura):
        """
        Agrega una asignatura a la lista de asignaturas del estudiante.

        Parámetros:
        - asignatura (Asignatura): La asignatura a agregar.
        """
        if not isinstance(asignatura, Asignatura):
            raise ValueError("La asignatura tiene que ser un objeto de la clase Asignatura")

        self._asignaturas.append(asignatura)


    def eliminar_asignatura(self, asignatura):
        """
        Elimina una asignatura de la lista de asignaturas del profesor.

        Parámetros:
        - asignatura (Asignatura): La asignatura a eliminar.
        """
        if not isinstance(asignatura, Asignatura):
            raise ValueError("La asignatura tiene que ser un objeto de la clase Asignatura")

        if asignatura in self._asignaturas:
            self._asignaturas.remove(asignatura)
    
class Departamento(Enum):
    """
    Enumeración que representa los departamentos de la universidad en los que puede estar un profesor.
    """

    DIIC = 1
    DITEC = 2
    DIS = 3

class Profesor(Persona):
    """
    Clase que representa a un profesor. Hereda de Persona.

    Atributos:
    - departamento (Departamento): El departamento al que pertenece el profesor. Al ser una enumeración el valor tendrá que ser uno de los valores de la enumeración Departamento.
    - asignaturas (list): La lista de asignaturas que imparte el profesor.
    - investigador (bool): Indica si el profesor es investigador(True) o no(False).
    """

    def __init__(self, nombre, sexo, dni, direccion, departamento, asignaturas, investigador:bool):
        super().__init__(nombre, sexo, dni, direccion)
        self.departamento = Departamento(departamento)
        self.asignaturas = asignaturas
        self.investigador = investigador

    def cambiarDepartamento(self, departamento):
        """
        Cambia el departamento del profesor.

        Parámetros:
        - departamento (Departamento): El nuevo departamento del profesor. Recuerda que el valor tiene que ser uno de los valores de la enumeración Departamento.
        """
        if not isinstance(departamento, Departamento):
            raise ValueError("El departamento tiene que ser un valor de la enumeración Departamento")
        self.departamento = Departamento(departamento)

    def agregar_asignatura(self, asignatura):
        """
        Agrega una asignatura a la lista de asignaturas del profesor.

        Parámetros:
        - asignatura (Asignatura): La asignatura a agregar.
        """
        if not isinstance(asignatura, Asignatura):
            raise ValueError("La asignatura tiene que ser un objeto de la clase Asignatura")

        self.asignaturas.append(asignatura)

    def eliminar_asignatura(self, asignatura):
        """
        Elimina una asignatura de la lista de asignaturas del profesor.

        Parámetros:
        - asignatura (Asignatura): La asignatura a eliminar.
        """
        if not isinstance(asignatura, Asignatura):
            raise ValueError("La asignatura tiene que ser un objeto de la clase Asignatura")

        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
    

class ProfesorTitular(Profesor):
    """
    Clase que representa a un profesor titular. Hereda de Profesor.

    Atributos:
    - area_investigacion (str): El área de investigación del profesor titular.
    """

    def __init__(self, nombre, sexo, dni, direccion, departamento, asignaturas, investigador:bool, investigacion):
        super().__init__(nombre, sexo, dni, direccion, departamento, asignaturas, investigador)
        self.area_investigacion = investigacion

    def __str__(self):
        return f"nombre:{self._nombre}, departamento:{self.departamento}, asignaturas:{self.asignaturas}, investigacion:{self.area_investigacion}"
        
    def _cambiar_investigacion(self, investigacion):
        """
        Cambia el área de investigación del profesor titular.

        Parámetros:
        - investigacion (str): El nuevo área de investigación del profesor titular.
        """
        if not isinstance(investigacion, str):
            raise TypeError("El área de investigación tiene que ser un string")
        self.area_investigacion = investigacion

class ProfesorAdjunto(Profesor):
    """
    Clase que representa a un profesor adjunto. Herea de Profesor.

    Atributos:
    - trabajo_externo (str): El trabajo externo del profesor adjunto.
    """

    def __init__(self, nombre, sexo, dni, direccion, departamento, asignaturas, investigador:bool, trabajo):
        super().__init__(nombre, sexo, dni, direccion, departamento, asignaturas, investigador)
        self.trabajo_externo = trabajo

    def __str__(self):
        return f"nombre:{self._nombre},departamento:{self.departamento}, asignaturas:{self.asignaturas}, trabajo:{self.trabajo_externo}"

    def cambiar_trabajo(self, trabajo):
        """
        Cambia el trabajo externo del profesor adjunto.

        Parámetros:
        - trabajo (str): El nuevo trabajo externo del profesor adjunto.
        """
        if not isinstance(trabajo, str):
            raise TypeError("El trabajo tiene que ser un string")
        self.trabajo_externo = trabajo
  
class Universidad():
    """
    Clase que representa una universidad. Utilizada como gestor de todo el programa.
    Dentro de esta clase se almacenan las listas de estudiantes, profesores y asignaturas.
    A su vez dentro de la clase es donde se borran o añaden estudiantes, profesores y asignaturas.

    Atributos:
    - estudiantes (list): La lista de estudiantes de la universidad.
    - profesores (list): La lista de profesores de la universidad.
    - asignaturas (list): La lista de asignaturas de la universidad.
    """

    def __init__(self):
        self.estudiantes = []
        self.profesores = []
        self.asignaturas = []
    
    def nuevoEstudiante(self, nombre, sexo, dni, direccion, curso, num_expediente, asignaturas):
        """
        Crea un nuevo estudiante y lo agrega a la lista de estudiantes.

        Parámetros:
        - nombre (str): El nombre del estudiante.
        - sexo (str): El sexo del estudiante.
        - dni (str): El DNI del estudiante.
        - direccion (str): La dirección del estudiante.
        - curso (str): El curso del estudiante.
        - num_expediente (str): El número de expediente del estudiante.
        - asignaturas (list): La lista de asignaturas que esta matriculado el estudiante.
        """
        self.estudiantes.append(Estudiante(nombre, sexo, dni, direccion, curso, num_expediente, asignaturas))

    def nuevoProfesor(self, nombre, sexo, dni, direccion, departamento, asignaturas, investigador:bool, investigacion=None, trabajo=None):
        """
        Crea un nuevo profesor y lo agrega a la lista de profesores.

        Parámetros:
        - nombre (str): El nombre del profesor.
        - sexo (str): El sexo del profesor.
        - dni (str): El DNI del profesor.
        - direccion (str): La dirección del profesor.
        - departamento (Departamento): El departamento al que pertenece el profesor.
        - asignaturas (list): La lista de asignaturas que imparte el profesor.
        - investigador (bool): Indica si el profesor es investigador(True) o no(False).
        - investigacion (str, opcional): El área de investigación del profesor titular.
        - trabajo (str, opcional): El trabajo externo del profesor adjunto.
        """
        if investigador == True:
            self.profesores.append(ProfesorTitular(nombre, sexo, dni, direccion, departamento, asignaturas, investigador, investigacion))
        else:
            self.profesores.append(ProfesorAdjunto(nombre, sexo, dni, direccion, departamento, asignaturas, investigador, trabajo))

    def nuevaAsignatura(self, nombre, curso, cuatrimestre, creditos):
        """
        Crea una nueva asignatura y la agrega a la lista de asignaturas.

        Parámetros:
        - nombre (str): El nombre de la asignatura.
        - curso (str): El curso donde se imparte la asignatura.
        - cuatrimestre (str): El cuatrimestre donde se imparte la asignatura.
        - creditos (int): El número de créditos de la asignatura.
        """
        self.asignaturas.append(Asignatura(nombre, curso, cuatrimestre, creditos))

    def buscarEstudiante(self, dni):
        """
        Busca un estudiante en la lista de estudiantes.

        Parámetros:
        - dni (str): El DNI del estudiante a buscar. Como es unico, se puede buscar por el DNI.

        Retorna:
        - Estudiante: El estudiante encontrado o None si no se encuentra.
        """
        for estudiante in self.estudiantes:
            if estudiante.getdni() == dni:
                return estudiante
        return None
    
    def buscarProfesor(self, dni):
        """
        Busca un profesor en la lista de profesores.

        Parámetros:
        - dni (str): El DNI del profesor a buscar. Como es unico, se puede buscar por el DNI.

        Retorna:
        - Profesor: El profesor encontrado o None si no se encuentra.
        """
        for profesor in self.profesores:
            if profesor.getdni() == dni:
                return profesor
        return None 
    
    def buscarAsignatura(self, nombre):
        """
        Busca una asignatura en la lista de asignaturas.

        Parámetros:
        - nombre (str): El nombre de la asignatura a buscar. No debería haber dos asignaturas con el mismo nombre.

        Retorna:
        - Asignatura: La asignatura encontrada o None si no se encuentra.
        """
        for asignatura in self.asignaturas:
            if asignatura.getnombre() == nombre:
                return asignatura
        return None
    
    def eliminarEstudiante(self, dni):
        """
        Elimina un estudiante de la lista de estudiantes.

        Parámetros:
        - dni (str): El DNI del estudiante a eliminar. Como es unico, se puede buscar por el DNI.

        Retorna:
        - bool: True si se eliminó el estudiante, False si no se encontró.
        """
        estudiante = self.buscarEstudiante(dni)
        if estudiante != None:
            self.estudiantes.remove(estudiante)
            return True
        return False

    def eliminarProfesor(self, dni):
        """
        Elimina un profesor de la lista de profesoresd.

        Parámetros:
        - dni (str): El DNI del profesor a eliminar. Como es unico, se puede buscar por el DNI.

        Retorna:
        - bool: True si se eliminó el profesor, False si no se encontró.
        """
        profesor = self.buscarProfesor(dni)
        if profesor != None:
            self.profesores.remove(profesor)
            return True
        return False
    
    def eliminarAsignatura(self, nombre):
        """
        Elimina una asignatura de la lista de asignaturas.

        Parámetros:
        - nombre (str): El nombre de la asignatura a eliminar. No debería haber dos asignaturas con el mismo nombre.

        Retorna:
        - bool: True si se eliminó la asignatura, False si no se encontró.
        """
        asignatura = self.buscarAsignatura(nombre)
        if asignatura != None:
            self.asignaturas.remove(asignatura)
            return True
        return False
    
if __name__ == "__main__":
    chequeo = True
    uni = Universidad()
    #Bucle para que el programa no se cierre y probar las funciones
    while chequeo == True:
        a = int(input("¿Qué desea hacer? (1.nuevoEstudiante, 2.nuevoProfesor, 3.nuevaAsignatura, 4.buscarEstudiante, 5.buscarProfesor, 6.buscarAsignatura, 7.eliminarEstudiante, 8.eliminarProfesor, 9.eliminarAsignatura, 10.salir): "))
        if a == 1:
            nombre = input("Nombre: ")
            sexo = input("Sexo: ")
            dni = input("DNI: ")
            direccion = input("Direccion: ")
            curso = input("Curso: ")
            num_expediente = input("Numero de expediente: ")
            asignaturas = []
            uni.nuevoEstudiante(nombre, sexo, dni, direccion, curso, num_expediente, asignaturas)

        elif a == 2:
            nombre = input("Nombre: ")
            sexo = input("Sexo: ")
            dni = input("DNI: ")
            direccion = input("Direccion: ")
            departamento = input("Departamento: ")
            asignaturas = []
            investigador = input("Investigador: (True/False)")
            if investigador == "True":
                investigacion = input("Investigacion: ")
                uni.nuevoProfesor(nombre, sexo, dni, direccion, departamento, asignaturas, True, investigacion)
            else:
                trabajo = input("Trabajo: ")
                uni.nuevoProfesor(nombre, sexo, dni, direccion, departamento, asignaturas, False, None, trabajo)
        
        elif a == 3:
            nombre = input("Nombre: ")
            curso = input("Curso: ")
            cuatrimestre = input("Cuatrimestre: ")
            creditos = input("Creditos: ")
            uni.nuevaAsignatura(nombre, curso, cuatrimestre, creditos)

        elif a == 4:
            dni = input("DNI: ")
            print(uni.buscarEstudiante(dni))
        
        elif a == 5:
            dni = input("DNI: ")
            print(uni.buscarProfesor(dni))
        
        elif a == 6:
            nombre = input("Nombre: ")
            print(uni.buscarAsignatura(nombre))
        
        elif a == 7:
            dni = input("DNI: ")
            print(uni.eliminarEstudiante(dni))
        
        elif a == 8:
            dni = input("DNI: ")
            print(uni.eliminarProfesor(dni))
        
        elif a == 9:
            nombre = input("Nombre: ")
            print(uni.eliminarAsignatura(nombre))
        
        elif a == 10:
            chequeo = False

        else:
            print("Opción no valida")

        #Para dejar un espacio entre cada pregunta
        print()