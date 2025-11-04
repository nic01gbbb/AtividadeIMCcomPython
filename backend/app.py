from flask import Flask, request, jsonify
from flask_cors import CORS  # <- importa o CORS

app = Flask(__name__)

app = Flask(__name__)

CORS(app)  # <- permite acesso de qualquer origem (React incluso)


@app.route('/')
def home():
    return "Servidor Flask rodando com sucesso!"


@app.route('/calcular-imc', methods=['POST'])
def calcular_imc():
    data = request.get_json()
    print("📦 JSON recebido:", data)

    try:
        nome = data.get('nome')
        endereco = data.get('endereco')
        peso = float(data.get('peso'))
        altura = float(data.get('altura'))
    except (TypeError, ValueError):
        return jsonify({'erro': 'Peso e altura devem ser números.'}), 400

    imc = peso / (altura * altura)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc <= 24.9 and imc >= 18.5:
        classificacao = "Peso normal"
    elif imc <= 29.9 and imc >= 24.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    mensagem = f"Olá, {nome}, do endereço {endereco}! Seu IMC é {imc:.2f} ({classificacao})."
    print(mensagem)
    return jsonify({
        "mensagem": mensagem,
        "imc": round(imc, 2),
        "classificacao": classificacao
    })


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2500, debug=True)
