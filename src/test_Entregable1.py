from Entregable1 import *

def test_Alumno_agregar_asignatura():
    programacion = Asignatura("Programación", "1º", "1º", 6)
    alumno = Estudiante("Julian", "V", "74952134F", "Calle Prueba", "1º", "1", [programacion])
    with pytest.raises(ValueError):
        alumno.agregar_asignatura("programacion")

def test_Profesor_cambiarDepartamento():
    programacion = Asignatura("Programación", "1º", "1º", 6)
    profesor = Profesor("Julian", "V", "74952134F", "Calle Prueba", Departamento.DIIC, [programacion], False)
    profesor.cambiarDepartamento(Departamento.DITEC)
    assert profesor.departamento == Departamento.DITEC

def test_Profesor_agregar_asignatura():
    programacion = Asignatura("Programación", "1º", "1º", 6)
    profesor = Profesor("Julian", "V", "74952134F", "Calle Prueba", Departamento.DIIC, [], False)
    with pytest.raises(ValueError):
        profesor.agregar_asignatura("programacion")

def test_Profesor_cambiarDepartamento_excepcion():
    programacion = Asignatura("Programación", "1º", "1º", 6)
    profesor = Profesor("Julian", "V", "74952134F", "Calle Prueba", Departamento.DIIC, [programacion], False)
    with pytest.raises(ValueError):
        profesor.cambiarDepartamento("DITEC")

def test_ProfesorTitular_cambiar_investigacion():
    programacion = Asignatura("Programación", "1º", "1º", 6)
    profesor = ProfesorTitular("Julian", "V", "74952134F", "Calle Prueba", Departamento.DIIC, [programacion], True, "Git")
    profesor._cambiar_investigacion("ML")
    assert profesor.area_investigacion == "ML"

def test_ProfesorTitular_cambiar_investigacion_excepcion():
    programacion = Asignatura("Programación", "1º", "1º", 6)
    profesor = ProfesorTitular("Julian", "V", "74952134F", "Calle Prueba", Departamento.DIIC, [programacion], True, "Git")
    with pytest.raises(TypeError):
        profesor._cambiar_investigacion(1)

def test_ProfesorAdjunto_cambiar_trabajo():
    programacion = Asignatura("Programación", "1º", "1º", 6)
    profesor = ProfesorAdjunto("Julian", "V", "74952134F", "Calle Prueba", Departamento.DIIC, [programacion], False, "Programador")
    profesor.cambiar_trabajo("Profesor")
    assert profesor.trabajo_externo == "Profesor"

def test_ProfesorAdjunto_cambiar_trabajo_excepcion():
    programacion = Asignatura("Programación", "1º", "1º", 6)
    profesor = ProfesorAdjunto("Julian", "V", "74952134F", "Calle Prueba", Departamento.DIIC, [programacion], False, "Programador")
    with pytest.raises(TypeError):
        profesor.cambiar_trabajo(1)
        
def test_Universidad_nuevoEstudiante():
    universidad = Universidad()
    programacion = Asignatura("Programación", "1º", "1º", 6)
    with pytest.raises(TypeError):
        universidad.nuevoEstudiante(2,3, "74952134F", "Calle Prueba", "1º", "1", [programacion])
    assert len(universidad.estudiantes) == 0

def test_Universidad_nuevoProfesor():
    universidad = Universidad()
    programacion = Asignatura("Programación", "1º", "1º", 6)
    with pytest.raises(TypeError):
        universidad.nuevoProfesor(2,3, "74952134F", programacion, "DIIC", [programacion], False, None, "Programador")
    assert len(universidad.profesores) == 0

def test_Universidad_nuevaAsignatura():
    universidad = Universidad()
    universidad.nuevaAsignatura("Programación", "1º", "1º", 6)
    assert len(universidad.asignaturas) == 1