## EightQueensPuzzle


### Requerimientos

- Python v3 o superior.
- Docker
- Postgress
- sqlalchemy
- pytest

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
