from flask import *
from pictogramas import *
import os


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtener los IDs de las imágenes seleccionadas del formulario
        imagenes_seleccionadas = request.form['imagenes_seleccionadas'].split(',')
        if imagenes_seleccionadas[0] != '':
            # Obtener los significados de las imágenes
            significados = obtener_significado(imagenes_seleccionadas)

            # Crear la oración concatenando los significados
            oracion = " ".join(significados)

            # Cargar pictogramas y mostrar la oración en el frontend
            resultados = ver_pictogramas()
            return render_template('index.html', resultados=resultados, oracion=oracion)

    # Si es un GET, solo mostrar los pictogramas
    resultados = ver_pictogramas()
    return render_template('index.html', resultados=resultados)

@app.route("/gestion/<action>", methods=['GET', 'POST'])
def gestion(action):
    mensaje = ''
    if action == 'subir':
        if request.method == 'POST':
            image = request.files['file']
            significado = request.form['significado']
            categoria = request.form['categoria']
            ruta = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(ruta)
            ruta_relativa = f"uploads/{image.filename}"
            mensaje = subir_pictograma(ruta_relativa, significado, categoria)
        return render_template('gestion.html', action=action, mensaje=mensaje)
    
    elif action == 'borrar':
        if request.method == 'POST':
            pictograma_id = request.form['id']
            mensaje = borrar_pictograma(pictograma_id)
        return render_template('gestion.html', action=action, mensaje=mensaje)
    
    elif action == 'subir_categoria':
        if request.method == 'POST':
            image = request.files['file']
            nombre = request.form['nombre']
            ruta = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(ruta)
            ruta_relativa = f"uploads/{image.filename}"
            mensaje = subir_categoria(nombre, ruta_relativa)
            print(mensaje)
        return render_template('gestion.html', action=action, mensaje=mensaje)
    else:
        mensaje = 'No se encontro la ruta'
        return render_template('gestion.html', action='none', mensaje=mensaje)
    
@app.route('/mostrar_categorias', methods=['GET', 'POST'])
def mostrar_categorias():
    resultados = ver_categorias()
    return render_template('mostrar_categorias.html', resultados=resultados)

@app.route('/categorias/<categoria>', methods=['GET', 'POST'])
def categorias(categoria):
    resultados = filtrar_categoria(categoria)
    return render_template('categorias.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=False, port=5000)
