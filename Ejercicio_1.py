# solicitar al usuario elemntos

mi_lista=[]

num = int(input("ingrese numero de datos q quiere ingresar "))

for i in range(num):
    mi_lista.append(int(input("ingrese numero : ")))


    print("tu lista de los  datos ingresados es :" ,mi_lista)

# eliminar duplicados
def Eliminar_duplicados (lista):

    for num in lista:           # recoremos la lista
        if num == num:
            lista.remove(num)
            return lista



lista =[1,1,2,3,3,3]
print ("la nueva lista es :",lista)


# Suma
def suma(lista1):
    suma = 0
    for num in lista1:
        suma += num
    return suma
lista1= [1,2,3,4,5]
print("la suma de los elementos de la suma  es : ",suma(lista1))

# comparacion de 2 listas
def comparacion_listas(lista_A,lista_B):
    for num in lista_A:  #recorremos lista_A
        if num in lista_B:
            return True
        return False
# creamos las listas
lista_A = [8,2,3]
lista_B = [1,4,5]
print("estas listas tienen algun elemento en comun : ",comparacion_listas(lista_A,lista_B))

#resta de matrices














