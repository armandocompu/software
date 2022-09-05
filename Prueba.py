
from pathlib import Path
import collections

def calificador(respuestas_correctas, respuestas_alumno):
    rc=respuestas_correctas[2:]
    ra=respuestas_alumno[3:]
    ra= ajustar(rc, ra)
    cont=0

    for la, lb in zip(rc, ra):
        if la == lb:
            cont += 1
    return    cont * 100 /len(rc)    

def ajustar(lista_completa, lista_alumno):
    '''
	Si la lista de respuestas del alumno esta incompleta, esta función rellena con -
	Si tiene más respuestas de las pedidas, elimina las últimas
	: param lista_completa : lista de respuestas completa
	: param lista_alumno : lista de respuestas del alumno
	'''
    long_correcta = len(lista_completa)
    alum_long = len(lista_alumno)

    respuestas_faltantes = long_correcta - alum_long

    for _ in range(respuestas_faltantes):
        lista_alumno.append('-')

    if respuestas_faltantes < 0:
        for _ in range(abs(respuestas_faltantes)):
            lista_alumno= lista_alumno[:-1]

    return   lista_alumno    

info = collections.namedtuple(
    'alumnoInfo',
    'nombre, nombreTrabajo, calificacion'
)

directorioAlumno = {}
listaAlumnos = []

with open("tareas/respuestas.txt", "r") as r:
    r = r.read().split('\n')

for tarea in Path("tareas/").iterdir():
    if tarea.is_file() and tarea.name.startswith('tarea'):
        with open(tarea, "r", encoding="utf-8", errors="ignore") as t:
            t = t.read()
            t = t.split('\n')

            calificacion = calificador(r, t)

            listaAlumnos.append(t[1])
            directorioAlumno[t[1]] = info(nombre=t[0], nombreTrabajo=t[2], calificacion=calificacion)


with open("calificacionesGrupales.csv", "w") as f:
    header = "Nombre, email, Tarea, Calificacion"
    f.write(header)
    f.write("\n")
    for aL in listaAlumnos:
        line = directorioAlumno[aL].nombre + " , " +aL + " , " + str(directorioAlumno[aL].nombreTrabajo) + " , " + str(directorioAlumno[aL].calificacion)
        f.write(line)
        f.write("\n")
