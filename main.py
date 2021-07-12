# pip install wikipedia

import wikipedia

# Podemos realizar busquedas específicas y resumirlas
print(wikipedia.summary("Wikipedia", sentences=1))

#Tambien podemos realizar busquedas generales y resumirlas
wikipedia.search("Barack")

# Para obtener la información debemos leer las páginas de los resultados de la busqueda
ny =wikipedia.page("New York City")
print("Título: ", ny.title)     #Título
print("URL: ", ny.url)          #URL de
print("Contenido: ", ny.content) #

# podemos cambiar el idioma de los resultados de la busqueda
wikipedia.set_lang("fr")
print(wikipedia.summary("Wikipedia", sentences=1))