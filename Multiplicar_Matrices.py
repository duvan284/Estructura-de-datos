#definimos las matrices
a = [[1,2],
     [2,3]
     ]
b = [[2,1],
     [1,1]]
# guardamos el tamaño de las matrices
L = len(a)
M = len(a[0])
N = len(b[0])
# creamos la matriz ncm , vacia
c = []
for i in range(L):
    c.append([])
    for q in range(N):
        c[i].append(0)

#multiplicacion
I = 0
while I < L :
    j = 0
    while j < N :
        k = 0
        while k < M :
            c[I][j] = c[I][j] + a[I][k]* b[k][j]
            k += 1
        j += 1
    I += 1
print("matriz a".center(50,"="))
for i in range (L):
    print(a[i])
print ("matriz b".center(50,"="))
for i in range (M):
    print(b[i])
print (" matriz producto ".center(50,"="))
for i in range (I):
    print(c[i])



