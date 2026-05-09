from flask import Flask,render_template,request

app = Flask(__name__)

#ruta principal 
@app.route('/')
def supermarket():
    return render_template('supermarket.html')


@app.route('/compras')
def comprar():
    return render_template('comprar.html')

    
# Ejecutar la app
if __name__ == "__main__":
    app.run(debug=True)
