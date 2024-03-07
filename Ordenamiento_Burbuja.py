def burbuja(arreglo):
    for i in range(1,len(arreglo)):
        for j in range(len (arreglo)-1):
            if (arreglo[j+1]<arreglo[j]):
                aux = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo [j+1] = aux
    return arreglo
arreglo = [7,4,0,1,2,3]
print("arreglo original :" , (arreglo))
print("arreglo ordenado :" , burbuja(arreglo))