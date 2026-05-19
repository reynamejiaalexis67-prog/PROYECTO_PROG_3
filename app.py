# importamos flask
from flask import Flask, render_template, request, redirect, url_for

# importamos nuestras clases
from entidades.producto import Producto
from entidades.carrito import Carrito
from entidades.categoria import Categoria


# creamos la aplicacion
app = Flask(__name__)


# creamos el carrito
carrito = Carrito()


# pagina principal
@app.route('/')
def supermarket():

    return render_template('supermarket.html')


# pagina de compras
@app.route('/compras')
def comprar():

    return render_template(

        'comprar.html',

        productos = carrito.productos,

        subtotal = carrito.calcular_subtotal(),

        iva = carrito.calcular_iva(),

        descuento = carrito.calcular_descuento(),

        total = carrito.calcular_total()
    )


# pagina agregar productos
@app.route('/agregar')
def agregar():

    return render_template('agregar.html')


# guardar productos del formulario
@app.route('/guardar', methods=['POST'])
def guardar():

    # obtenemos datos
    nombre = request.form.get('nombre')

    precio = float(request.form.get('precio'))

    categoria_texto = request.form.get('categoria')


    # verificamos categoria
    if categoria_texto == "bebida":

        categoria = Categoria.BEBIDA

    else:

        categoria = Categoria.REPOSTERIA


    # creamos producto
    producto = Producto(

        nombre,

        precio,

        categoria
    )


    # agregamos al carrito
    carrito.agregar_producto(producto)


    # volvemos al inicio
    return redirect(url_for('supermarket'))


# agregar mokka
@app.route('/agregar_mokka')
def agregar_mokka():

    producto = Producto(
        "Mokka",
        50,
        Categoria.BEBIDA
    )

    carrito.agregar_producto(producto)

    return redirect(url_for('supermarket'))


# agregar croissant
@app.route('/agregar_croissant')
def agregar_croissant():

    producto = Producto(
        "Croissant",
        25,
        Categoria.REPOSTERIA
    )

    carrito.agregar_producto(producto)

    return redirect(url_for('supermarket'))


# agregar americano
@app.route('/agregar_americano')
def agregar_americano():

    producto = Producto(
        "Americano",
        60,
        Categoria.BEBIDA
    )

    carrito.agregar_producto(producto)

    return redirect(url_for('supermarket'))


# agregar dona
@app.route('/agregar_dona')
def agregar_dona():

    producto = Producto(
        "Dona",
        20,
        Categoria.REPOSTERIA
    )

    carrito.agregar_producto(producto)

    return redirect(url_for('supermarket'))


# ejecutar programa
if __name__ == "__main__":

    app.run(debug=True)
