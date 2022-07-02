## Complejidad Algoritmica - CC184
![](https://github.com/IbrahimImanol/TF-201716094-20191E650-20201C579/blob/henry/Imagenes/UPC.png)
## Integrantes
- Ibrahim Imanol Jordi, Arquiñigo Jacinto -  U20191E650
- Luis Roberto, Arroyo Bonifaz            -  U201716094
- Henry Josué, Diaz Huarcaya              -  U20201C579 

## Introduccion
En este trabajo se continuará el trabajo realizado del parcial del curso de Complejidad Algoritmica. En el presente trabajo se desarrollara la competencia de "Responsabilidad y Ética profesional". De esta manera debemos tener detallada la informacion de los entregables pasados, presentes y futuros.

Para el presente trabajo se agregara las funciones de visualizacion para mostrar el grafo como un mapa. Ademas de la creacion de una interfaz para que el usuario pueda interactuar con el grafo en diferentes horas del dia. Asimismo agregaremos la funcion del calculo del trafico aleatorio utilizando SimplexNoise. De esta manera desarrollaremos el trabajo para la finalizacion del curso de Complejidad Algoritmica 2022-1.
## Objetivos
El objetivo como grupo es demanera responsable y ética, poder a través del trabajo parcial, complementarlo con funcionalidades que le permitan convertirse de un generador de grafo de una ciudad, a un sistema de búsqueda de rutas. Este sistema además deberá contar con un factor de tráfico que estará regulado por la hora del día.

Con esto buscamos crear una aplicación similar a "Waze", aplicación móvil de tránsito automotor en tiempo real y navegación asistida por GPS. Para esto usaremos conceptos aprendidos en el curso como la teoría de grafos, algoritmos de búsqueda en grafos como el algoritmo de Dijkstra y agregandole funciones adicionales como la función perlin noise la cual es una función matemática que utliza interpolaciones para así lograr valores seudo-aleatorios y conseguir un mapa de tráfico condicionado por la hora del día que se encuentre.

## Video Previo TP

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/kyKOBNskkek/0.jpg)](http://www.youtube.com/watch?v=kyKOBNskkek)

## Resumen Ejecutivo

El presente trabajo tiene como finalidad crear una aplicacion de búsqueda de rutas para obtener la ruta minima entre dos intersecciones de calles. Asimismo nos apoyaremos en una visualizacion del grafo para observar cual es el camino mas corto entre puntos. Estos puntos para el presente trabajo se trabajaran como intersecciones entre calles (latitud y longitud).

Ademas de entrgarle al usuario una interaccion con el trafico en diferentes horas del dia. Para el trabajo realizado como ya se menciono antes se utilizara la ciudad de New York. 

Imagen Referencial de la ciudad de Nueva York: 

![](https://github.com/IbrahimImanol/TF-201716094-20191E650-20201C579/blob/henry/Imagenes/NEW%20YORK.png)

Para logar nuestro objetivo, debemos contar con la latitud y longitud de cada intersección en nuestro grafo, el peso de las aristas calculados, en función a la latitud y longitud, y el factor de tráfico. Además, tenemos en cuenta que el factor del tráfico varia según la hora del día y la ubicación. Para esto crearemos una función seudoaleatoria la cual en función a la hora ingresada por el usuario, determine un valor preciso para el mapa de tráfico en la ruta seleccionada. Por ejemplo, si la hora indicada son las 7:00 am y es una ruta concurrida, el tráfico será alto, debido a que en este horario hay muchas personas transitando. Mientras que si son las 12:00 pm el tráfico será bajo debido a que en este horario no encontramos muchos transeúntes.

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

## Descripción de los datos
Nuestros datos nos indican información respecto a todas las avenidas y calles de la ciudad de New York.
La información se encuentra estructurada de la siguiente manera:
- Objeto con información de una calle o avenida
- Cada objeto contiene un arreglo de coordenadas, ordenadas en un sentido, que representan la conexión entre los puntos

![](https://github.com/IbrahimImanol/TF-201716094-20191E650-20201C579/blob/main/Imagenes/ejmdatos.png)

## Explicación de la elaboracion del grafo
Para poder realizar la elaboración del grafo primero tuvimos que hallar una fuente confiable en la que se nos brinde la mayor información posible respecto a la ciudad de estudio, en nuestro caso New York.

Obtuvimos un archivo de tipo geojson con información de todas las calles y avenidas disponibles, para un total de 65000 puntos. Se intentó reducir la cantidad de información, pero al no estar seccionada por bloques, lo que terminaba ocurriendo era que desconectabamos muchas calles, algo que terminaría afectando al desarrollo de nuestro trabajo. 

Para el desarrollo del grafo tuvimos que leer mediante proceso iterativo toda la información del geojson, unicamente nos quedariamos con la información que está contenida en el arreglo de las coordenadas y mediante un diccionario guardariamos toda la información de las rutas que seguian estas coordenadas.

Para lograr la lista de adyacencia, mediante iban apareciendo las coordenadas, se les asignaba un indice, y se calculaba las distancias entre los puntos, que despues se ingresarian a nuestra lista de adyacencia.

Finalmente registramos en un archivo txt la relación entre los indices y coordenadas respectivas para poder hacer una comprobación del éxito de nuestro trabajo de manera más rápida.

## Conclusiones
- Para el desarrollo del trabajo es necesario tener conocimientos de los distintos algoritmos SSSP.
- Es importante poder realizar un algoritmo de recolección de información de manera eficiente a fin de reducir los tiempos de ejecución del proyecto.
- El algoritmo de Dijkstra nos permite encontrar el camino más corto entre dos ubicaciones del mapa.
- Para poder realizar un trabajo de manera responsable y ética, se recomienda utilizar un programa de gestión de proyectos como GitHub

4 de abril de 2022
Lima, Perú

