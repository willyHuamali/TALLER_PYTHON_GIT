"""Notas de clases"""
# TIPO DE DATOS
"""Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType  
-------------------------------- """
""" Example	Data                                Type	"""
x = "Hello World"	                            str	
x = 20                                      	int	
x = 20.5	                                    float	
x = 1j	                                        complex	
x = ["apple", "banana", "cherry"]               list	
x = ("apple", "banana", "cherry")	            tuple	
x = range(6)	                                range	
x = {"name" : "John", "age" : 36}	            dict	
x = {"apple", "banana", "cherry"}	            set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	                                    bool	
x = b"Hello"	                                bytes	
x = bytearray(5)	                            bytearray	
x = memoryview(bytes(5))                       	memoryview	
x = None	                                    NoneType

"""numeros aleatorios"""
import random
print(random.randrange(1, 10))

"""Get the character at position 1 (remember that the first character has the position 0):"""
a = "Hello, World!"
print(a[1]) #devuelve la posisicion de la variable 

"""The len() function returns the length of a string:"""

a = "Hello, World!"
print(len(a)) # devuevle la longitud de un string

"METODOS DE LETRAS"

a = "Hello, World!"
print(a.upper())  # MAYUSCULA
print(a.lower()) #miniuscula
print(a.title()) # convierte las primeras letras en mayuscula
print(a.capitalize()) #convierte solo la primera letra en mayuscula
print(a.swapcase())  # Cambiar mayúsculas por minúsculas y viceversa
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"  elimina los espacios de principio y final
a = "Hello, World!"
print(a.replace("H", "J")) #metodo para reemplazar letras J por H --- Jello, world
"DEVUELVE SI TODO LAS LETRAS ESTAN EN MAYUSCULAS, LO MISMO SE PUEDE HACER CON MINUSCULA islower()"
>>> 'Hola'.isupper()
False
>>> 'HOLA'.isupper()
True

a = "Hello, World!" 
print(a.split(",")) # returns ['Hello', ' World!'] El método divide la cadena en subcadenas si encuentr un separador

"""Code	Result	       original text                         return
\'	Single Quote	   'It\'s alright.'                      It's alright.
\\	Backslash	    "This will insert one \\ (backslash)."   This will insert one \ (backslash).
\n	New Line	       salto de linea
\r	Carriage Return	  
\t	Tab	               salta 2 espacios
\b	Backspace	       quita espacio
\f	Form Feed	       
\ooo	Octal value	
\xhh	Hex value	
"""