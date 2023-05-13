from flask import Flask, request, jsonify, render_template
import validaciones

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/validar_numeros', methods=['POST'])
def validar_numeros():
    num1 = request.form['num1']
    
    resultado = {}
    resultado['num1'] = validaciones.validar_numeros(num1)
    
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
