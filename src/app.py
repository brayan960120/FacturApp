from flask import Flask,render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html', titulo_pagina = 'Login')

@app.route('/iniciar')
def iniciar():
    return render_template('inicio.html' , titulo_pagina ='home')

@app.route('/registro')
def registro():
    return render_template('Registro.html')


@app.route('/registrarse')
def registrarse():
    return render_template('index.html')


@app.route('/crear_usuario')
def crear_usuario():
    return render_template('formulario_crear_usuario.html')


@app.route('/lista_usuario')
def lista_usuario():
    return render_template('tabla_usuarios.html')

@app.route('/crear_categoria')
def crear_categoria():
    return render_template('formulario_crear_categoria.html')


@app.route('/tabla_categoria')
def tabla_categoria():
    return render_template('tabla_categorias.html')

@app.route('/crear_cliente')
def crear_cliente():
    return render_template('formulario_crear_cliente.html')

@app.route('/tabla_clientes')
def tabla_cliente():
    return render_template('tabla_clientes.html')

@app.route('/crear_productos2')
def crear_producto():
    return render_template('formulario_crear_productos.html')

@app.route('/tabla_productos2')
def tabla_productos():
    return render_template('tabla_productos.html')

@app.route('/crear_factura')
def crear_factura():
    return render_template('formulario_crear_factura.html')

@app.route('/tabla_facturas')
def tabla_facturas():
    return render_template('tabla_facturas.html')

@app.route('/home')
def home():
    return render_template('inicio.html')

@app.route('/editar_usuario')
def editar_usuario():
    return render_template('editar_usuario.html')


@app.route('/editar_productos')
def editar_producto():
    return render_template('editar_productos.html')


@app.route('/editar_factura')
def editar_factura():
    return render_template('editar_factura.html')


@app.route('/editar_cliente')
def editar_cliente():
    return render_template('editar_clientes.html')


@app.route('/editar_categoria')
def editar_categoria():
    return render_template('editar_categoria.html')