#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
num = 10;
print(10);

# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
CONSTANTE = 8.5;
print(type(CONSTANTE));

# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(num));

# 4) Crear una variable que contenga tu nombre

# In[2]:
nombre = 'Gerardo';

# 5) Crear una variable que contenga un número complejo

# In[3]:
complejo = 5 + 3j;

# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(complejo));

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
pi = 3.1416;

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
variable = True;
variable2 = variable;

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(variable2));

# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
suma = (4 + 3.6);

# 11) Realizar una operación de suma de números complejos

# In[2]:
sumaComplejo = (3+5j) + (2+4j);
print(sumaComplejo);

# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
sumaReal = (4) + (4 + 3j);
print(sumaReal);

# 13) Realizar una operación de multiplicación

# In[5]:
mul = 4 * 4;

# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
potencia = 2 ** 8;
print(potencia);

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
cociente = 27 / 4;
print(cociente);

# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
enteroDivision = 27 // 4;
print(enteroDivision);

# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
restoDivision = 27 % 4;
print(restoDivision);

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
resultado = (enteroDivision * 4) + restoDivision;
print(resultado);

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
alfanumerico = '10' + "4";
print(alfanumerico);

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
evaluar = ("2" == 2);
print(evaluar);

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
print(int("2") == 2);

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
a = float("3.5"); # da el error por la coma 
print(a);

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
variable3 = 3;
variable3 -= 1;
print(variable3);

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
operacion = 1 << 2; #suma de binarios
print(operacion);

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
print(2 + int("2"))

# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
suma = 3 + int("23");
print(suma);



# %%
