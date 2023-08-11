<h1 align="center"> Primer Proyecto Individual Machien Learning Operations (Bootcamp Henry / Data Science) </h1>
<h1 align="center"> Sistema de Recomendacion de peliculas </h1>

<p align="center">![](https://github.com/Constanzafl/Proyecto_Indiv_1_MLO_Henry/assets/121994442/8e125d89-5235-4eee-8411-04b7bfe8a838)</p>

Este proyecto se trata de simular un entorno laboral, en el cual hay que crear un modelo de ML para un sistema de recomendacion de peliculas en una plataforma de streaming. 

Los pasos que realice para lograr este modelo, fueron:

1. Primero realizar un ETL (extract transform y load) partiendo de dos datasets
iniciales que se nos dieron, sacando nulos, duplicados, outliers y generando nuevos datasets mas pequeños mas faciles de manipular. 

2. Ademas realizar un EDA (exploratory data analisis) como para visualizar y graficar las variables de los datasets, y las relaciones entre ellas. A partir de esto podemos sacar algunas conclusiones que pueden servirnos para el analisis de los datos. 

3.Despues de estos dos procesos,se nos pidieron 7 funciones en las consignas, en las cuales, a partir de ingresar determinada palabra, se obtenia una respuesta en modo diccionario o lista. Para esas funciones lo que hice fue crear datasets mas pequeños y uno para cada uno de ellas. La ultima funcion es un modelo de recomendacion de peliculas. Es decir que partir de la colocacion del nombre de una pelicula, el modelo recomienda 5 peliculas parecidas. 

4. Luego para disponibilizar los datos, usamos el framework FastAPI de forma local y para que estos datos esten de manera virtual levantamos un deploy en render. 
