# -*- coding: utf-8 -*-
iterations = 200
cont = 2
result = ""
 
if iterations > 1:
    fibonacci1 = 1
    fibonacci2 = 1
 
    result = result + "" + format(fibonacci1)
    result = result + ", " + format(fibonacci2)
 
    while cont < iterations:
        temp = fibonacci2
        fibonacci2 = fibonacci1 + fibonacci2
        fibonacci1 = temp
        result = result + ", " + format(fibonacci2)
        cont = cont + 1
 
print("Fibonacci: " + result)

