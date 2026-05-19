from flask import Flask,render_template, request, redirect, url_for
from entidades.producto import Producto
from entidades.carrito import Carrito
from entidades.categoria import Categoria


app = Flask(__name__)

# Creamos el carrito en donde se guardara todo
carrito = Carrito()

#ruta principal 
@app.route('/')
def supermarket():
    return render_template('supermarket.html')

#creamos nuestras rutas secundarias de compras
@app.route('/compras')
def comprar():
    return render_template('comprar.html')



#creamos una segunda ruta secundaria para agregar productos 
@app.route('/agregar')
def agregar():
    return render_template('agregar.html')

# esta ruta recibe los datos del formulario agregar.html y los guarda en el carrito
@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form.get('nombre')
    precio = float(request.form.get('precio'))
    # Creamos el objeto y lo metemos al carrito
    nuevo = Producto(nombre, precio, Categoria.Bebida) 
    carrito.agregar_producto(nuevo)
    return redirect(url_for('supermarket'))




    
# Ejecutar la app
if __name__ == "__main__":
    app.run(debug=True)
