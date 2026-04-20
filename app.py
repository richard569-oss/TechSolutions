from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        servicio = request.form['servicio']
        mensaje = request.form['mensaje']

        print("Nuevo mensaje:")
        print(nombre, email, servicio, mensaje)

        return redirect(url_for('inicio'))

    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
