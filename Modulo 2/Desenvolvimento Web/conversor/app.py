from flask import Flask, request, render_template

app = Flask (__name__)

@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        valor1 = float(request.args.get('valor1', 0))
        cotação_do_dólar = 5.29

        resultado =valor1 * cotação_do_dólar
        return render_template('index.html', valor1=valor1, resultado=resultado)
        return '<h1 color="red"> erro</h1>'
    