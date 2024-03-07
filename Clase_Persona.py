class Persona :
    def __init__(self,nombre,edad,genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def saludar (self):
        print("hola soy persona ")
        pass


#instancia de la clase
persona1 = Persona("martin","23","masculino " )
persona2 = Persona("mariana","26","femenino")

#llamdao al metodo
print(Persona.saludar(persona1))

print(f"nombre:",persona1.nombre + " edad: ",persona1.edad + " genero: " ,persona1.genero)
print(f"nombre:",persona2.nombre + " edad: ",persona2.edad + " genero: " ,persona2.genero)

#clase empleado
class Empleado(Persona):
    pass
    def __init__(self,salario , puesto_de_trabajo,):
        self.salario = salario
        self.puesto_de_trabajo = puesto_de_trabajo
    def saludar(self):
        return "hola soy empleado"







emple1 = Empleado("1300000","gerente")

print(emple1.saludar())
print(f"nombre:",persona1.nombre + " edad: ",persona1.edad + " genero: " ,persona1.genero +
      "salario :",emple1.salario + " puesto de trabajo ",emple1.puesto_de_trabajo )

# clase estudiante

class Estudiante (Persona):
    pass
    def __init__(self,grado , escuela):
        self.grado = grado
        self.escuela = escuela
    def saludar(self):
        return " hola soy estudiante "
estudiante1 = Estudiante("7","u caldas")
print(estudiante1.saludar())

print(f"nombre : ", persona2.nombre + " edad : " ,persona2.edad + " genero : ",  persona2.genero
      + " grado : " , estudiante1.grado +  " escuela : " , estudiante1.escuela )
