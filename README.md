# EvaluacionFinal


# Documentación Python

Este código cumple la función de convertir una letra o palabra en su código ASCII correspondiente y seguidamente en su forma binaria. 

### Para esto se hace el uso de la función "ord()" la cual está contenida en la función convert_ascii:
```py
def  convert_ascii(letter):

result  =  ord(letter)

return  result

```
Esta función recibe como parámetro un string el cual va a ser contenido en la variable "letter", la función convierte el parámetro en a su código ASCII y lo almacena en la variable "result" para luego retornarla.

### Para la conversión a forma binaria se utiliza la función "bin()" contenida en la función convert_binary:
```py
def  convert_binary(num):

result  =  bin(num)

return  result
```
La función recibe como parámetro un número entero que el cual va a ser contenido en la variable "num", la función convierte el parámetro en a su forma binaria y lo almacena en la variable "result" para luego retornarla.

## Menú del programa
El menú será la manera en la que el usuario interactúa con el programa, desde ahí podrá elegir si desea convertir una letra o una palabra a su código ASCII y su  forma binaria. Por lo que estarán solamente 2 opciones disponibles, cualquier elección ajena a estas dos opciones el programa lo asumirá como orden para salir del programa.

### Para convertir una letra en ASCII y en binario
```py
if  option  ==  1:
chosenLetter  =  input("Write the letter: ")
ascii_num  =  convert_ascii(chosenLetter)
print("=============\nResults\n=============\n")
print(
"ASCII character value of", chosenLetter, "is", ascii_num ,
"and representation of", chosenLetter, "in a byte is", convert_binary(ascii_num)
)
```
Para esta opción, el programa le pedirá al usuario que escriba la letra de su interés, luego el programa hará uso de las funciones convert_ascii para obtener el valor del código ASCII y utilizarlo para obtener la forma binaria de la letra escogida por el usuario.

### Para convertir una palabra en ASCII y en binario
```py
elif  option  ==  2:
chosenWord  =  input("Write the word: ")
binaryWord  = []
print("=============\nResults\n=============\n")
for  i  in  chosenWord:
ascii_num  =  convert_ascii(i)
convertion  =  convert_binary(ascii_num)
print(
"ASCII character value of", i, "is", ascii_num ,
"and representation of", i, "in a byte is", convertion
)
binaryWord.append(convertion)
print(" ".join(binaryWord))
```
Para la conversión de una palabra a su código ASCII y su forma binaria utilizamos el mismo procedimiento de la conversión de letras, pero adicionando un ciclo finito para la conversión de cada letra de la palabra que será almacenada en la lista "binaryWord" que finalmente se mostrará en pantalla dando como resultado la palabra completa en su forma binaria.


# Documentación GitHub
### Integrante: Juan José Arcila (usuario: juanjo2354)

Primero, se creó el repositorio donde se sube la información de este archivo, cabe resaltar que este repositorio es de acceso público. Para clonar el repositorio en el ordenador donde se realizó el desarrollo del programa se utilizó la llave SSH del usuario utilizando el siguiente comando en Git Bash:

```
$ git clone "llave SSH del usuario"
```
Una vez creado el clon del repositorio nos ubicamos en la rama principal del repositorio con el siguiente comando:
```
$ cd "nombre de la carpeta del repositorio"/
```
Esto nos lleva a la rama principal ("main") del repositorio, sin embargo los archivos se van a subir a una rama distinta que diverge desde esta rama principal, por lo que usamos los siguientes comandos para crear y acceder a dicha rama:
```
$ git branch "nombre de la rama"

$ giy checkout "nombre de la rama"
```
Una vez ubicados en la rama de interés y desarrollado el código, utilizamos los siguientes comandos para añadir los archivos a la lista de pendientes, confirmamos y seguidamente subirlos:
```
$ git add . (añadir todos los archivos con cambios al repositorio)

$ git commit -m "añade un comentario que va a ir con los archivos"

$ git push origin "nombre de la rama donde van a ir los archivos"
```
Ahora si los archivos se han subido a la rama que creamos en el repositorio. Finalmente realiza un Pull Request a la rama main para copiar los archivos de la rama que creamos a la rama principal.
