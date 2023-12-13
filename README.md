# Registro Básico de Contactos

## Instalación

Preferiblemente utilizar un bash de linux para la ejecución de comandos

- git bash

### Paso 1

En una línea de comandos, instalaremos virtualenv

```bash
pip install virtualenv
```
### paso 2

luego, nos movemos al directorio de este proyecto y abrimos una línea de comandos donde ejecutaremos lo siguiente

```bash
virtualenv env
```
se va a crear una carpeta `env` en la carpeta principal del proyecto

### paso 3

Ahora activaremos nuestro entorno virtual, en la línea de comandos ejecutaremos lo siguiente

```bash
source env/Script/activate
```
arriba de nuestro usuario, aparecerá `(env)`

### paso 4 

Instalaremos las dependencias necesarias para el proyecto

```bash
pip install -r requeriments.txt
```
## Ejecución del programa

Al ser un programa CLI, todo será ejecutado por la consola.

para arrancar el programa, debebos asegurarnos que estamos ubicados en el entorno virtual. 

```bash
python main.py
```

Aparecerán las opciones del programa.

A disfrutar


