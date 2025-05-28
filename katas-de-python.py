#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.


def frecuencia(texto):
    texto = texto.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

texto = 'A veces la vida te da sorpresas, sorpresas que la vida misma no esperaba, porque la vida es así, llena de sorpresas'


#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado_map_lamda=(list(map(lambda x: x*2,numeros)))
print(resultado_map_lamda)

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.


def buscar_palabras_con_objetivo(lista_palabras, palabra_objetivo):
    resultado = [palabra for palabra in lista_palabras if palabra_objetivo in palabra]
    return resultado


palabras = ['computadora', 'ratón', 'teclado', 'monitor', 'portátil', 'componente']
objetivo = 'com'

print(buscar_palabras_con_objetivo(palabras, objetivo))


#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()


lista1 = [5,10,15,20,35]
lista2 = [3,8,12,15,20]
diferencia = (list(map(lambda x, y : x - y, lista1, lista2)))
print(diferencia)


#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.


def evaluar_notas(notas, notas_aprobado):
    media = sum(notas)  / len(notas) 
    if media >= 5:
        estado= 'Aprobado'
    else:
        estado= 'Suspenso'
    return media, estado
notas = [5,7,4,2,8,7]
resultado = evaluar_notas(notas, 5)

print(resultado)


#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
        if n == 0 or n == 1:
            return 1
        else: 
            return n* factorial(n-1)
n = factorial(5)
print(n)


#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: ', '.join(map(str, t)), lista_tuplas))

tuplas = [(1, 2), (3, 4), ('a', 'b')]
resultado = tuplas_a_strings(tuplas)
print(resultado)

#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.


try:
    numero1 = float(input('Ingresa un primer numéro: '))
    numero2 = float(input('Ingresa un segundo numéro: '))

    resultado = numero1/numero2

except ValueError:
    print('Ingrese un número válido')
except ZeroDivisionError:
    print('No se puede dividi entre cero')

else:
    print(f'El resultado es: {resultado}')


#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()


lista_mascotas = ["Gato", "Serpiente Pitón", "Perro", "Pez", "Cocodrilo", "Hamster", "Pajaro", "Huron", "Oso"]
lista_mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

def filtrar_mascotas(mascotas):
    return list(filter(lambda m:m not in lista_mascotas_prohibidas, mascotas))
mascotas_filtradas = filtrar_mascotas(lista_mascotas)

print("lista_mascotas", mascotas_filtradas)


#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.


lista = [2,4,6,8,10]
avg =sum(lista)/len(lista)
print(f'El promedio es {round(avg)}')
'

#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.


print("¿Cuál es tu edad?")
edad=0
def obtener_edad():
    while True:
        try:
            edad=int(input("Introduce tu edad: "))
            if  edad <=0 or edad >=120:
                raise ValueError  ("La edad tiene que estar comprendida entre 0 y 120 años")
            else:
                return edad
            
        except ValueError:
            print("edad erronea, introduce un número.")

edado=obtener_edad()

print(f"Tu edad es {edad}.")


#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()


def longitudes_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

frase = 'Hola mi nombre es Aida'
resultado = longitudes_palabras(frase)
print(resultado)


#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def letras_mayus_minus(conjunto):
    unicas = set(filter(str.isalpha, conjunto))
    resultado = list(map(lambda c: (c.upper(), c.lower()), unicas))
    return resultado

conjunto = "aAbBcC123!a"
print(letras_mayus_minus(conjunto))


#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()


def palabras_con_b(palabra, letra):
    return list(filter(lambda palabra_b: palabra_b.startswith(letra), palabra))

lista_palabras = ['taza', 'vaso', 'abrigo', 'bolsa', 'ordenador' 'mochila', 'bolso', 'blusa'] 
resultado = palabras_con_b(lista_palabras, 'b')      

print(resultado)


#15. Crea una función lambda que sume 3 a cada número de una lista dada.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado_map_lamda=(list(map(lambda x: x+3,numeros)))
print(resultado_map_lamda)


#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def cadena_de_texto(numero, n):
    cadena = texto.split()
    return list(filter(lambda cadena: len(cadena) > n, cadena))

texto = 'Hola mi nombre es Aida y estoy aprendiendo Python'
resultado = cadena_de_texto(texto, 5)
print(resultado)

#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()


from functools import reduce

def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

resultado = lista_a_numero([4,8,2,7])
print("Número:", resultado)

#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()


estudiantes = [
    {'nombre': 'Juan', 'edad': 18, 'calificación' : 25},
    {'nombre': 'Maria', 'edad': 19, 'calificación' : 95},
    {'nombre': 'Pedro', 'edad': 35, 'calificación' : 90},
    {'nombre': 'Ana', 'edad': 22, 'calificación' : 85}
]

def filtrar_calificacion(usuario):
  return usuario['calificación'] >= 90

estudiantes_aprobados = list(filter(filtrar_calificacion, estudiantes))

print(estudiantes_aprobados)


#19. Crea una función lambda que filtre los números impares de una lista dada.


filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtrado = list(filter(lambda x: x % 2 != 0, numeros))
print(filtrado)


#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()


mi_lista = [1, 'hola', 3, 'me', 5, 'llamo', 8, 'Aida', 16]
solo_enteros = list(filter(lambda x: isinstance(x, int), mi_lista))
print(solo_enteros)


#21. Crea una función que calcule el cubo de un número dado mediante una función lambda


numero = 5
cubo = lambda x: x ** 3
resultado = cubo(numero)
print(resultado)


#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .


from functools import reduce
lista_numeros = [2,4,8,6,10]
producto_total =  reduce(lambda x , y : x * y, lista_numeros)
print(f'El producto total es : {producto_total}')


#23. Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce
lista_palabras= ['Hola',' ', 'mi',' ',  'nombre', ' ', 'es',' ', 'Aida']
frase_total =  reduce(lambda x , y : x + y, lista_palabras)
print(frase_total)


#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce
lista_numeros = [63,45,32,15]
producto_total =  reduce(lambda x , y : x - y, lista_numeros)
print(f'La diferencia total es : {producto_total}')


#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.


def contar_caractertes(texto):
    return len(texto)

frase = "Hola, mi nombre es Aida"
cantidad = contar_caractertes(frase)
print(f'El número de caracteres es: {cantidad}')


#26. Crea una función lambda que calcule el resto de la división entre dos números dados.


resto = lambda x, y: x % y
print(resto(7, 3)) 
print(resto(25, 7))

#27. Crea una función que calcule el promedio de una lista de números.


def calcular_promedio(lista):
        if not lista:
            return 0
        return sum(lista)/len(lista)
    
numeros=[4,7,25,47]
promedio = calcular_promedio(numeros)
print(f'El promedio es: {promedio}')


#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.


def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None 
print(primer_duplicado([3, 5, 1, 4, 5, 6]))


#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.


def enmascarar(variable):
    texto = str(variable)
    if len(texto) <= 4:
        return texto
    return '#' * (len(texto) - 4) + texto[-4:]

print(enmascarar("contraseña"))


#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.


def esAnagrama(cadena1, cadena2):
    return sorted(cadena1) == sorted(cadena2)

print(esAnagrama('roma','mora'))


#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

nombre1 = input('Dame un nombre 1: ')
nombre2 = input('Dame un nombre 2: ')
nombre3 = input('Dame un nombre 3: ')
nombre4 = input('Dame un nombre 4: ')
nombre5 = input('Dame un nombre 5: ')

lista_nombres = [nombre1, nombre2, nombre3, nombre4, nombre5]
print (f'La lista de nombres es: {lista_nombres}')

while True:
    nombre_buscar = input('Dame un nombre: ')
    if nombre_buscar in lista_nombres:
        print('¡Enhorabuena! El nombre está en la lista.')
        break  # Sale del bucle
    else:
        print('Lo siento, ese nombre no está en la lista. Intenta de nuevo.')

#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.


def obtener_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre_completo.lower():
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí."

empleados = [
    {"nombre": "Aida Herrero", "puesto": "Research Executive"},
    {"nombre": "Paula Clemente", "puesto": "Strategy Manager"},
    {"nombre": "Rocio Martinez", "puesto": "Campaing Manager"}
]

print(obtener_puesto("Aida Herrero", empleados))  
print(obtener_puesto("Cristina Gomez", empleados)) 


#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.


lista_1 = [1,2,3,4,5,6]
lista_2 = [6,5,4,3,4,1]

resultado = list(map(lambda x,y: x + y, lista_1,lista_2))
print(f'La suma de los elementos correspondiente a las listas es: {resultado}')



#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
#Código a seguir:
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.


class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print(f"No hay rama en la posición {posicion}")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# 1. Crear un árbol
mi_arbol = Arbol()

# 2. Hacer crecer el tronco del árbol una unidad
mi_arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol
mi_arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad
mi_arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2
mi_arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol
info = mi_arbol.info_arbol()
print(info)



#36.Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
#Código a seguir:
#1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
#2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
#3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
#4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.


class UsuarioBanco:
    #consrtuctor
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar €{cantidad}.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado €{cantidad}. Saldo restante: €{self.saldo}.")

    def transferir_dinero(self, otro_usuario, cantidad):
        if not isinstance(otro_usuario, UsuarioBanco):
            raise TypeError(f"{otro_usuario} no está registado en el banco.")
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser mayor que cero.")
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir €{cantidad}.")
        
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"{otro_usuario.nombre} transfirió €{cantidad} a {self.nombre}.")
        print(f"{self.nombre} ahora tiene €{self.saldo}. {otro_usuario.nombre} ahora tiene €{otro_usuario.saldo}.")

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor que cero.")
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado €{cantidad}. Saldo actual: €{self.saldo}.")

usuario1 = UsuarioBanco("Carlos", 500, True)
usuario2 = UsuarioBanco("Aida", 300, False)

usuario1.retirar_dinero(100)
usuario1.agregar_dinero(200)
usuario1.transferir_dinero(usuario2, 150)




#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
#Código a seguir:
#1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
#2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
#3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
#4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
#Caso de uso:
#Comprueba el funcionamiento completo de la función procesar_texto

#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.


hora = float(input('¿Que hora es? '))

if 6 <= hora < 12:
    print(f'Es de día.') 
elif 12 <= hora < 18:
    print(f'Es por la tarde.') 
elif 18 <= hora <= 23 or 0 <= hora < 6:
    print(f'Es de noche.')


#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
#Las reglas de calificación son:
#- 0 - 69 insuficiente
#- 70 - 79 bien
#- 80 - 89 muy bien
#- 90 - 100 excelente


calificacion_en_texto = int(input('Escribe tu calificación: '))
nota = calificacion_en_texto

def calificacion_en_texto(nota):
    valoracion = ""
    if 0 >= nota < 69:
        valoracion = 'Insuficiente'
    elif 70 >= nota < 79:
        valoracion = 'Bien'
    elif 80 >= nota < 89:
        valoracion ='Muy bien'
    elif 90 >= nota < 100:
        valoracion = 'Excelente'
    else:
        valoracion = 'Nota no valida'
    return valoracion
print(f'Tu calificacion es: {calificacion_en_texto(nota)}')


#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).


import math

def calcular_area(figura, datos):
    figura = figura.lower()  # Asegura que la entrada no sea sensible a mayúsculas

    if figura == "rectangulo":
        if len(datos) != 2:
            raise ValueError("Para un rectángulo se requieren dos valores: base y altura.")
        base, altura = datos
        return base * altura
    
print(calcular_area("rectangulo", (5, 10)))

#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:


#Solicitar precio original
try:
    precio_original = float(input("Ingresa el precio original del artículo (€): "))
    if precio_original <= 0:
        print("El precio debe ser mayor que cero.")
    else:
        #Preguntar si tiene cupón
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí o no): ").strip().lower()

        #Si tiene cupón, pedir valor y aplicar si es válido
        if tiene_cupon == "sí" or tiene_cupon == "si":
            try:
                descuento = float(input("Ingresa el valor del cupón de descuento (€): "))
                if descuento > 0:
                    precio_final = max(precio_original - descuento, 0)  # Evita precios negativos
                    print(f"Se ha aplicado un descuento de {descuento}€. El precio final es: {precio_final:.2f}€")
                else:
                    print("El valor del cupón debe ser mayor que cero. No se aplicó descuento.")
                    print(f"El precio final es: {precio_original:.2f}€")
            except ValueError:
                print("Entrada no válida para el valor del cupón.")
                print(f"El precio final es: {precio_original:.2f}€")
        elif tiene_cupon == "no":
            print(f"No se aplicó ningún descuento. El precio final es: {precio_original:.2f}€")
        else:
            print("Respuesta no válida. Se asumirá que no tienes cupón.")
            print(f"El precio final es: {precio_original:.2f}€")
except ValueError:
    print("Entrada no válida para el precio original.")
