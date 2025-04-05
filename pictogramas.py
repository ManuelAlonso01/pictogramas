import sqlite3


def subir_pictograma(url, significado, categoria):
    try:
        conexion = sqlite3.connect('database/database.db')
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO pictogramas(url, significado, categoria) VALUES (?, ?, ?)', (url, significado, categoria))
        conexion.commit()
        conexion.close()
        return 'El picotograma se subio con exito'
    except sqlite3.Error:
        return 'Se produjo un error al subir el pictograma'
    finally:
        if conexion:
            conexion.close()
    
def borrar_pictograma(pictograma_id):
    try:
        conexion = sqlite3.connect('database/database.db')
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM pictogramas WHERE id == (?)', (pictograma_id,))
        conexion.commit()
        conexion.close()
        return 'El picotograma se borro con exito'
    except sqlite3.Error:
        return 'Se produjo un error al borrar el pictograma'
    finally:
        if conexion:
            conexion.close()
            
            
def ver_pictogramas():
    try:
        conexion = sqlite3.connect('database/database.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT id, url FROM pictogramas')
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except sqlite3.Error:
        return 'Se produjo un error'
    
    
def obtener_significado(list_ids):
    try:
        lista_palabras = []
        conexion = sqlite3.connect('database/database.db')
        cursor = conexion.cursor()
        for i in list_ids:
            cursor.execute('SELECT significado FROM pictogramas WHERE id = (?)', (i,))
            resultado = cursor.fetchone()
            lista_palabras.append(resultado[0])
        conexion.close()
        return lista_palabras
    except sqlite3.Error:
        return 'Se produjo un error'
    finally:
        if conexion:
            conexion.close()
    
            
def subir_categoria(nombre, url):
    try:
        conexion = sqlite3.connect('database/database.db')
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO categorias(nombre, url) VALUES(?, ?)', (nombre, url,))
        conexion.commit()
        conexion.close()
        return 'La categoria se subio con exito'
    except sqlite3.Error:
        return 'Se produjo un error'
    finally:
        if conexion:
            conexion.close()
            
            
def ver_categorias():
    try:
        conexion = sqlite3.connect('database/database.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT nombre, url FROM categorias')
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except sqlite3.Error:
        return 'Se produjo un error'
    finally:
        if conexion:
            conexion.close()
            
def filtrar_categoria(categoria):
    try:
        conexion = sqlite3.connect('database/database.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT id, url FROM pictogramas WHERE categoria = (?)', (categoria,))
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except sqlite3.Error:
        return 'Se produjo un error'
    finally:
        if conexion:
            conexion.close()



resultados = filtrar_categoria('saludo')
for pictograma in resultados:
    print(pictograma)