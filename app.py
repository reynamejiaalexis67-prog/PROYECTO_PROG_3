from flask import Flask,render_template,request

app = Flask(__name__)

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




    
# Ejecutar la app
if __name__ == "__main__":
    app.run(debug=True)
