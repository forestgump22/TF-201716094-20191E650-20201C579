## Complejidad Algoritmica - CC184
![](https://github.com/IbrahimImanol/TF-201716094-20191E650-20201C579/blob/henry/Imagenes/UPC.png)
## Integrantes
- Ibrahim Imanol Jordi, Arquiñigo Jacinto -  U20191E650
- Luis Roberto, Arroyo Bonifaz            -  U201716094
- Henry Josué, Diaz Huarcaya              -  U20201C579 

## Introduccion
En este trabajo se continuara el trabajo realizado del parcial del curso de Complejidad Algoritmica. En el presente trabajo se desarrollara la competencia de "Responsabilidad y Etica profesional". De esta manera debemos tener detallada la informacion de los entregables pasados, presentes y futuros.

Para el presente trabajo se agregara las funciones de visualizacion para mostrar el grafo como un mapa. Ademas de la creacion de una interfaz para que el usuario pueda interactuar con el grafo en diferentes horas del dia. Asimismo agregaremos la funcion del calculo del trafico aleatorio utilizando SimplexNoise. De esta manera desarrollaremos el trabajo para la finalizacion del curso de Complejidad Algoritmica 2022-1.
## Objetivos
El objetivo como grupo es demanera responsable y ética, poder a través del trabajo parcial, complementarlo con funcionalidades que le permitan convertirse de un generador de grafo de una ciudad, a un sistema de búsqueda de rutas. Este sistema además deberá contar con un factor de tráfico que estará regulado por la hora del día.

Con esto buscamos crear una aplicación similar a "Waze", aplicación móvil de tránsito automotor en tiempo real y navegación asistida por GPS. Para esto usaremos conceptos aprendidos en el curso como la teoría de grafos, algoritmos de búsqueda en grafos como el algoritmo de Dijkstra y agregandole funciones adicionales como la función perlin noise la cual es una función matemática que utliza interpolaciones para así lograr valores seudo-aleatorios y conseguir un mapa de tráfico condicionado por la hora del día que se encuentre.

## Video Previo TP

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/kyKOBNskkek/0.jpg)](http://www.youtube.com/watch?v=kyKOBNskkek)

## Resumen Ejecutivo

El presente trabajo tiene como finalidad crear una aplicacion de búsqueda de rutas para obtener la ruta minima entre dos intersecciones de calles. Asimismo nos apoyaremos en una visualizacion del grafo para observar cual es el camino mas corto entre puntos. Estos puntos para el presente trabajo se trabajaran como intersecciones entre calles (latitud y logitud).

Ademas de entrgarle al usuario una interaccion con el trafico en diferentes horas del dia. Para el trabajo realizado como ya se menciono antes se utilizara la ciudad de New York. 

Imagen Referencial de la ciudad de Nueva York: 

![](https://github.com/IbrahimImanol/TF-201716094-20191E650-20201C579/blob/henry/Imagenes/NEW%20YORK.png)

Para logar nuestro objetivo, debemos contar con la latitud y longitud de cada intersección en nuestro grafo, el peso de las aristas calculados, en función a la latitud y longitus, y el factor de tráfico. Además, tenemos en cuenta que el factor del tráfico varia según la hora del día y la ubicación. Para esto crearemos una función seudoaleatoria la cual en función a la hora ingresada por el usuario, determine un valor preciso para el mapa de tráfico en la ruta seleccionada. Por ejemplo, si la hora indicada son las 7:00 am y es una ruta concurrida, el tráfico será alto, debido a que en este horario hay muchas personas transitando. Mientras que si son las 12:00 pm el tráfico será bajo debido a que en este horario no encontramos muchos transeúntes.

## Division De Tareas

En el presente trabajo se realizo con exito la distribucion de tareas entre el equipo, gracias a una distribucion correcta de los issues en GitHub. Ademas de facilitar este procedimiento atraves de la plataforma de GitHub. 

La distribucion de los issues fue la siguiente para cada uno de los integrantes del Equipo de desarrollo:

Henry
Interfaz de Usuario y Agregacion de Dijkstra.

Ibrahim
Agregacion de la funcion de visualizacion del mapa de New York por la web.
Reconstruccion de Caminos

Luis
Agregacion de Dijkstra para hallar el camino mas corto entre intersecciones de las calles.
Agregacion de pesos del grafo.
## Conclusiones
En conclusion hemos desarrollado un algoritmo capaz de leer datos para luego armar un grafo. Este grafo representara el mapa de New York. Despues, mi equipo aplico algoritmos de caminos cortos para poder observar el camino mas corto entre estos nodos. Ademas mi equipo desarrollo un camino alternativo para que se vea las diferencias que hay entre nuestro algoritmo, bfs y dijkstra. Este trabajo se logro visualizar por web debido a las condiciones del profesor.
4 de abril de 2022
Lima, Perú
