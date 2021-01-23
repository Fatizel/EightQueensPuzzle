### Eight Queens Puzzle

El Juego de las ocho reinas es un modelo de destresa que no permiten que dos reinas compartan la misma fila, columna o diagonal, el objetivo es resolver tableros de n x n que permitan respetar estas reglas. 

### Objetivo

Desarrollar un programa en Python3 que permita encontrar todas las posibles soluciones a este problema con un tablero de n x n

### Modelo de Ejecución. 

Se utilizaron modelos recursivos para la resolución del problema de las 8 reinas, se generan 3 funciones principales que permiten verificar la posición de las reinas para encontrat las posibles soluciones al problema. Una vez que se listan las soluciones, las mismas se almacenan en la base de datos de postgres y se monitoriza el tiempo de ejecución de cada partida. 

Para la resolución del problema se diseñaron 5 funciones. 

  # verification
          En esta funcion se verifica la condición de respetar las filas las columnas y los laterasles
  # research
  # inspection
  # dbconect
           Esta funcion esta diseñada para establecer la conexion con la base de datos de postgres los parametros que se requieren son:
              * User Name
              * Password
              * host
              * Port
           Para esta prueba se utilizaron los parametros default que vienen con la instalación base del postgres.
  # dbinsert
            Permite insertar los valores dentro de la base de datos de postgress, la cual se reinicia con cada una de las iteraciónes de los datos. 
  

### Requerimientos

- Docker
- Postgress
- Python v3 o superior
- Sqlalchemy
- Pytest

### Instalación

Para la compilacion de la imagen: 

```console

docker build -t eqpuzzle -f Dockerfile  .

``` 


## Levantar servidor postgres

```console
docker run -ti --rm -e POSTGRES_PASSWORD=mysecretpassword --name=fatima-eqpuzzle eqpuzzle

```


## ejecutamos el script de python

```console

docker exec fatima-eqpuzzle python3 /opt/queen/equeenInput.py


```
