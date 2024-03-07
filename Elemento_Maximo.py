def elemento_maximo(arreglo):
    maximo = arreglo[0]
    for num in arreglo:
        if num > maximo:
           maximo = num

    return maximo
arreglo = [8,9,5,3,2,1,89]
print ("el elemento maximo del arreglo es el numero :" , elemento_maximo(arreglo))
