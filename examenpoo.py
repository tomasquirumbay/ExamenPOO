#Clase principal
def __init__(self, nombreDocente, apellidoDocente, edadDocente):
    self.nombre=nombreDocente
    '''Variable nombre'''
    self.apellido=apellidoDocente
    '''Variable apellido'''
    self.edad=edadDocente
    '''Variable edad'''
#clase estado
def estado(self, rol, departamento, salario):
    self.rol=rol
    '''variable rol'''
    self.departamento=departamento
    '''Variable departamento'''
    self.salario=salario
    '''variable salario'''
#Clase del personal academico
def personalAcademico():
    print("***Area del personal***")
    '''Mensaje de muestra'''
    docentesRegistrados=int(input("Escriba los docentes existentes en su institución/universidad: "))
    '''Escribir la cantidad de docentes que existan'''
    nombre=str(input("Escriba el nombre: "))
    '''Escribir el nombre del docente'''
    apellido=str(input("Escriba el apellido: "))
    '''Escribir el apellido del docente'''
    edad=str(input("Escriba la edad: "))
    '''Escribir la edad del docente'''
    departamento=str(input("Escriba el departamento: "))
    '''Escribir el area en el que se encuentra dicho docente'''
personalAcademico()
'''Imprimimos los datos'''