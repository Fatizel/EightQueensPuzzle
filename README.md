### Eight Queens Puzzle

El Juego de las ocho reinas es un modelo de destresa que no permiten que dos reinas compartan la misma fila, columna o diagonal, el objetivo es resolver tableros de n x n que permitan respetar estas reglas. 

### Objetivo

Desarrollar un programa en Python3 que permita encontrar todas las posibles soluciones a este problema con un tablero de n x n

### Modelo de Ejecución. 

Se utilizaron modelos recursivos para la resolución del problema de las 8 reinas, se generan 3 funciones principales para verificar la posición de las reinas y encontrar las posibles soluciones al problema. Una vez que se listan las soluciones, estas se almacenan en la base de datos de postgres y se monitoriza el tiempo de ejecución de cada partida. 

Para la resolución del problema se diseñaron 5 funciones. 

  #### verification
          En esta funcion se verifica la condición de respetar las filas las columnas y los laterales
  #### research
          Recorre la matriz por columnas para evaluar las condiciones llamando a la función de ispection, que se encarga de regresar los resultados validos. 
  #### inspection
          Es la funcion principal de la verificación de la matriz, recibe la información de la función research, verifica si la información es valida y almacena los resultados en una matriz que contiene las posibles soluciones. 
  #### dbconect
           Esta funcion esta diseñada para establecer la conexion con la base de datos de postgres los parametros que se requieren son:
              * User Name
              * Password
              * host
              * Port
           Para esta prueba se utilizaron los parametros default que vienen con la instalación base del postgres.
  #### dbinsert
            Permite insertar los valores dentro de la base de datos de postgress, la cual se reinicia con cada una de las iteraciónes de los datos. 
  
  La ejecución principal se encarga del paso de parametros a la función principal el numero n para el problema de las ocho reinas y permite almacenar la información resultante en la base de datos de postgres. 

 El valor n se podra modificar en la variable "queen", variable principal para la ejecución. 
```console
            queen = int(8)
```

### Requerimientos

- Docker
- Postgress
- Python v3 o superior
- Sqlalchemy
- Pytest

Para la ejecución de la prueba se requiere seguir los siguientes pasos los cuales permiten la instalación y configuración del docker así como todos sus componentes. 

### Instalación

El primer paso es la compilación de la imagen en el cual se tiene el archivo Dockerfile, en este archivo se encuentran toda la paqueteria necesaria, una vez descargados los recursos en nuestro equipo, solo es necesario utilizar un gestor de contenedores para ejecutar la imagen de Docker incluida en el proyecto.

Para la contrucción del contenedor con todos los elementos necesarios se ejecuta la siguiente linea de codigo. 

```console

docker build -t eqpuzzle -f Dockerfile  .

``` 
Una vez que el contenedor fue creado exitosamente se requiere levantar la instancia de postgres la cual se muestra con el siguiente codigo, si las credencailes de acceso al postgres fueron modificadas se debera realizar los cambios donde corresponda, se no ser así se ejecuta . 

## Levantar servidor postgres

```console
docker run -ti --rm -e POSTGRES_PASSWORD=mysecretpassword --name=fatima-eqpuzzle eqpuzzle

```
Por ultimo para la ejecución del script realizado para resolver el problema de las Ocho reinas tenemos la siguiente linea de codigo. 

## ejecutamos el script de python

```console

docker exec fatima-eqpuzzle python3 /opt/queen/equeenInput.py


```
Si se requiere modificar el numero N en el archivo equeenInput.py en la variable queen, como se menciono en el paso anterior. 


