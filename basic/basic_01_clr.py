__Author__ = 'Diego Galviz'
__License__ = 'Free use'
__version__ = '1.0'
__status__ = 'Development'


"""
En el siguiente archivo se muestra como importar un modulo de clr. 
El modulo clr es un modulo que permite importar librerias de .net a python.
En este caso se importa la libreria ProtoGeometry.dll que es una libreria de .net
que contiene las clases de geometria de Dynamo.
"""

# _________________________________
# importando modulo clr
import clr

# Importando archivo dll
clr.AddReference("ProtoGeometry")

# importando namespace
from Autodesk.DesignScript.Geometry import *


# _________________________________
# output o salida
OUT = Point.ByCoordinates.__doc__








