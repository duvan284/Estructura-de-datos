a = 1
b = 1

print(f"{a} , {b}" , end =", ")
for i in range (10):
    c = a + b
    b = a
    a = c
    print (  a,end=", ")