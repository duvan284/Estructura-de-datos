def buscar_numero(arreglo, objetivo):
    for num in arreglo:
        if num == objetivo:
            return True
    return False

arreglo =[1,6,9,5,9,7]
numero_objetivo = 5
print("¿ el numero objetivo esta presente en el arreglo ? : ",buscar_numero(arreglo,numero_objetivo))
print ("El numero objetivo se encuentra  en el arreglo " , 5 in arreglo)