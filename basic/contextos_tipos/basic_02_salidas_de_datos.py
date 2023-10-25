"""
Ejercicio de tipos de datos
en este ejercicio se muestra algunos los tipos de datos que se pueden usar con python en dynamo
"""

import clr

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
from decimal import Decimal, getcontext

getcontext().prec = 2

#  data types
int_exe = 1
float_exe = 1.0
decimal_exe = Decimal("1.0")
string_exe = "esto es un string"
string_exe_2 = 'esto tambien es un string'
complex_num = 4j
boolean_exe = True
boolean_exe_2 = False

# itereable data types
list_exe = ['esto es un elemento de la lista', 6, 1.0]
tuple_exe = ('esto es un elemento de la tupla', 7, 10)
set_exe = {'esto es un elemento del set', 8, 10, 8, 10}
dict_exe = {'key': 'value', 'key_2': 'value_2'}

# objects or instances of class
instances_of_clase_or_object = Point.ByCoordinates(1, 2, 3)
instances_of_clase_or_object_2 = Point.ByCoordinates(2, 3, 5)

# float and decimal
num_decimal_1 = Decimal("0.1")
num_decimal_2 = Decimal("0.2")
num_decimal_3 = Decimal("0.3")

# error de redondeo float
num_1 = 0.2
num_2 = 0.1
num_3 = 0.3

result_1 = (num_1 + num_2) - num_3
type_result_1 = type(result_1)
result = num_decimal_1 + num_decimal_2 - num_decimal_3
type_result = type(result)
suma = num_1 + num_2

OUT = instances_of_clase_or_object
