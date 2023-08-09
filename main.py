from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



#Defino y traigo todos los datasets que voy a utilizar
df_director= pd.read_csv('DirectorFUNCION.csv')
df_reducido= pd.read_csv('DuracionFuncion.csv')
franquicia2= pd.read_csv('Franquicias.csv')
dfidiomas= pd.read_csv('LenguageCANTIDAD.csv')
dfpaises= pd.read_csv('PaisesCANTpelis.csv')
dfprodu= pd.read_csv('ProductorasFuncion.csv')
df_top_5=pd.read_csv('Top15kpelis.csv')
filters=pd.read_csv('filters.csv')
df_concat3=pd.read_csv('FuncionML.csv')

app = FastAPI(title='Trabajo 1 MLO Henry Constanza Florio', description='Sistema de Recomendacion')



@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma: str):
    '''Ingresas el idioma, retornando la cantidad de peliculas producidas en el mismo'''
    # Filtrar el DataFrame para obtener las películas en el idioma dado
    peliculas_en_idioma = dfidiomas[dfidiomas['original_language'] == idioma]
    
    # Si no hay películas en el idioma dado, retornar None o un mensaje indicativo
    if peliculas_en_idioma.empty:
        return {'No hay peliculas en ese idioma'}
    
    # Obtener la cantidad de películas en el idioma dado
    cantidad = peliculas_en_idioma['id'].sum()
    
    # Crear el diccionario de respuesta
    respuesta = {'idioma': idioma, 'cantidad': cantidad}
    
    return respuesta

@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula: str):
    '''Ingresas la pelicula, retornando la duracion y el año'''
    
    # Buscar la fila correspondiente a la película ingresada
    pelicula_info = df_reducido[df_reducido['title'] == pelicula]
    
    # Verificar si se encontró la película en el DataFrame
    if pelicula_info.empty:
        return None  # O un mensaje indicativo de que no se encontró la película
    
    # Obtener la duración y el año de la película
    duracion = pelicula_info['runtime'].values[0]
    anio = pelicula_info['release_year'].values[0]
    
    # Crear el diccionario de respuesta
    respuesta = {'pelicula': pelicula, 'duracion': duracion, 'anio': anio}
    
    return respuesta

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia: str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    
    # Filtrar el DataFrame para obtener las películas de la franquicia dada
    peliculas_franquicia = franquicia2[franquicia2['NAME'] == franquicia]
    
    # Verificar si se encontraron películas para la franquicia dada
    if peliculas_franquicia.empty:
        return {"Ese valor no corresponde a ninguna franquicia en nuestros datos"}  # O un mensaje indicativo de que no se encontraron películas
    
    # Obtener la cantidad de peliculas en el idioma dado
    cantidad = peliculas_franquicia['id'].values[0]
    
    # Obtener la ganancia total de la franquicia
    ganancia_total = peliculas_franquicia['revenue_x'].values[0]
    
    # Obtener la ganancia promedio de la franquicia
    ganancia_promedio = peliculas_franquicia['revenue_y'].values[0]
    
    # Crear el diccionario de respuesta
    respuesta = {
        'franquicia': franquicia,
        'cantidad': cantidad,
        'ganancia_total': ganancia_total,
        'ganancia_promedio': ganancia_promedio
    }
    
    return respuesta

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''
    
    # Filtrar el DataFrame para obtener las películas producidas en el país dado
    peliculas_en_pais = dfpaises[dfpaises['name'] == pais]
    
    # Si no hay películas en un pais dado, retornar None o un mensaje indicativo
    if peliculas_en_pais.empty:
        return {'No se encuentran peliculas realizadas en ese pais'}
    
    # Obtener la cantidad de películas producidas en el país
    cantidad = peliculas_en_pais['id_original'].sum()
    
    # Crear el diccionario de respuesta
    respuesta = {'pais': pais, 'cantidad': cantidad}
    
    return respuesta

@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora: str):
    '''Ingresas la productora, entregandote el revunue total y la cantidad de peliculas que realizo '''
    
    # Filtrar el DataFrame para obtener las películas de la franquicia dada
    peliculas_productora = dfprodu[dfprodu['name'] == productora]
    
    # Verificar si se encontraron películas para la franquicia dada
    if peliculas_productora.empty:
        return {'Valor inexistente'}  # O un mensaje indicativo de que no se encontraron películas
    
    # Obtener la cantidad de peliculas en el idioma dado
    cantidad = peliculas_productora['id'].values[0]
    
    # Obtener la ganancia total de la franquicia
    ganancia_total = peliculas_productora['revenue'].values[0]
    

    
    # Crear el diccionario de respuesta
    respuesta = {
        'franquicia': productora,
        'cantidad': cantidad,
        'ganancia_total': ganancia_total
        
    }
    
    return respuesta

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director: str):
    
    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. 
    
    En formato lista'''
    
    # Filtrar el DataFrame para obtener las películas dirigidas por el director dado
    peliculas_director = df_director[df_director['name'] == nombre_director]
    
    # Verificar si el director se encuentra en el DataFrame
    if peliculas_director.empty:
        return {'Valor inexistente'}  # O un mensaje indicativo de que el director no se encontró
    
    # Calcular el éxito del director sumando los retornos individuales de sus películas
    retorno_total_director = peliculas_director['return'].sum()
    
    # Crear una lista de diccionarios con información detallada de cada película
    peliculas = []
    for index, row in peliculas_director.iterrows():
        pelicula_info = {
            'nombre': row['title'],
            'anio': row['release_date'],
            'retorno_pelicula': row['return'],
            'budget_pelicula': row['budget'],
            'revenue_pelicula': row['revenue']
        }
        peliculas.append(pelicula_info)
    
    # Crear el diccionario de respuesta
    respuesta = {
        'director': nombre_director,
        'retorno_total_director': retorno_total_director,
        'peliculas': peliculas
    }
    
    return respuesta


tfidf= TfidfVectorizer(stop_words='english')
df_top_5['overview'].fillna('', inplace=True)
tfidf_matrix = tfidf.fit_transform(df_top_5['overview'])
cosine_sim= linear_kernel(tfidf_matrix, tfidf_matrix)

count= CountVectorizer(stop_words='english')
count_matrix= count.fit_transform(filters['metadatos'])
cosine_sim2= cosine_similarity(count_matrix, count_matrix)
filters= filters.reset_index()
indices=pd.Series(filters.index, index=filters['title'])

@app.get('/recomendacion/{title}')
def recomendacion_peli(title:str, cosine_sim=cosine_sim2.all()):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
    
    title=title.replace(' ','').lower() 
    
    idx= indices[title]
    
    sim_scores= list(enumerate(cosine_sim[idx]))
    
    sim_scores= sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    sim_scores= sim_scores[1:6]
    
    movie_indices= [i[0] for i in sim_scores]
    
    lista= df_concat3['title'].iloc[movie_indices]
    lista2= lista.to_list()
    
    return lista2



