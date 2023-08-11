<h1 align="center"> Primer Proyecto Individual Machien Learning Operations (Bootcamp Henry / Data Science) </h1>
<h1 align="center"> Sistema de Recomendacion de peliculas </h1>

![.](https://github.com/Constanzafl/Proyecto_Indiv_1_MLO_Henry/assets/121994442/a3f9a312-e16a-4f38-95a0-acb96e292ed2)

### Indice
## Resumen
## Stack tecnológico utilizado
## Descripcion del Proyecto
## Datos
## Links de referencia
## Autora del proyecto

## Resumen
* Este proyecto se trata de simular un entorno laboral, en el cual hay que crear un modelo de ML para un sistema de recomendación de peliculas en una plataforma de streaming.
* Se utilizan dos data sets iniciales que contienen información relacionada con las películas. Y un diccionario de datos que define la información que encontramos en cada columna.
* Se nos dan determinadas consignas básicas para realizar en la limpieza de datos, dejando a libre elección el resto de las transformaciones y se nos solicita crear 7 funciones, que devuelven cierto dato solicitado de las películas, actores y directores. Y una última función que involucra el sistema de recomendación.

## Stack tecnológico utilizado:
-	Python: librerías dentro de Python como, Numpy, Pandas, Scikit-Learn, Matplotlib, WordCloud, Seaborn, nltk.
-	FastApi
-	Uvicorn
-	Render

## Descripcion del Proyecto
# Los pasos que realice para lograr este modelo fueron:

1. Primero realizar un ETL (Extract Transform Load) partiendo de dos data sets iniciales que se nos dieron, sacando nulos, duplicados, outliers y generando nuevos data sets más pequeños más fáciles de manipular. 
1. Además realizar un EDA (Exploratory Data Analisis) como para visualizar y graficar las variables de los data sets, y las relaciones entre ellas. A partir de esto podemos sacar algunas conclusiones que pueden servirnos para el análisis de los datos. 
1.Despues de estos dos procesos, utilicé los datos que obtuve para crear las funciones solicitadas.
1. Luego para disponibilizar los datos, usamos el framework FastAPI de forma local y para que estos datos esten de manera virtual levantamos un deploy en Render.

## Datos 
Los data sets originales están en el siguiente link: 
- Movies: 
https://drive.google.com/file/d/1DbiA12FkEJtCJPcgpRyfeX3nb_EaX3ni/view?usp=drive_link
- Credits:
https://drive.google.com/file/d/1dGMg_oC9glYpXvrhNKZZSbneX6w25jlh/view?usp=drive_link

# Trabaje en VSC utilizando Python y cree carpetas y nuevos data sets:
# Carpetas:

* EDA: se encuentran dos archivos con los gráficos y analisis correspondiente llamados ANALISIS-UNIVARIADO Y ANALISIS-BIVARIADO. Este lo realizo con los data sets que hice yo luego de las transformaciones. 
* ETL: tiene a su vez 3 carpetas adentro:
* A-ETLconsignas: se encuentra un archivo llamado ETL_consignas, en donde aplico las consignas iniciales solicitadas en el instructivo del trabajo. Excepto la de desanidar columnas que la realizo en otra carpeta aparte. Allí creo dos datasets mas pequeños: uno que se llama MoviesSMALL.csv y Movies1.csv.
* CSVNUEVOS: en el archivo creandocsv utilizo el data set Movies1.csv para realizar distintos data set en función a cada columna que quiero desanidar. Por ejemplo, separo la columna belong_to_colecction con el id, para luego desanidar las franquicias en otro archivo aparte. Lo mismo con géneros, productoras y países. Y creo un data set que contiene solo los lenguajes.
* DESANIDANDO: creo distintos archivos ipynb para desanidar cada uno de los data sets creados en la carpeta anterior. Luego de desanidarlos creo nuevo data sets que me van a servir para cada función solicitada. Además de desanidar las columnas necesarias, en base a lo que me pedía cada función fui uniendo los distintos data sets que cree.
* FUNCIONES: luego hice las funciones que se nos solicitaron en las consignas. Para cada función me traje el data set que armé en la carpeta anterior, que tenía las columnas de los datos solicitados en cada una. 
* ML-FUNCION: archivos de como arme las funciones y los data sets creados para esa función. Achique la cantidad de películas, ya que el modelo sino demoraba mucho.
* Myenv: es el medio virtual
* Por fuera de estas carpetas y en la carpeta principal, quedaron los archivos requirements.txt, main.py y el readme. Además, todos los data sets finales que utilizo en el archivo main con las funciones. Tuve que poner los data sets en el mismo lugar que el main, en la carpeta principal para que en Render corriera sin errores. 

## Links de referencia:
1.	Render: 
https://tt-pp34.onrender.com/docs
1.	Video: 
https://drive.google.com/file/d/1RUdnHzmtKkoy0iYVNptMjuBO9V0s-dBX/view?usp=drive_link

## Autora del proyecto
# Maria Constanza Florio
https://www.linkedin.com/in/mar%C3%ADa-constanza-florio-1926b5158/




