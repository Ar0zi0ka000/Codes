import sys
import operator
import math

rut = input("Rut(primeros 8 digitos sin puntos): ")
rut_list = []
num_cal = [3,2,7,6,5,4,3,2]
for i in rut:
    rut_list.append(i)
rut_list_int = [int(x)for x in rut_list]
calculo = list(map(operator.mul, rut_list_int, num_cal))
calculo1 = sum(list(calculo))
calculo2 = math.floor(calculo1 / 11)
calculo3 = calculo1 - (11 * calculo2)
calculo4 = 11 - calculo3
digito_verificador = calculo4

if (calculo4 == 11):
    digito_verificador = "0"
elif (calculo4 == 10):
    digito_verificador = "k"
print( "El digito verificador es: " + str(digito_verificador) + "\n", str(rut) + "-" + str(digito_verificador))