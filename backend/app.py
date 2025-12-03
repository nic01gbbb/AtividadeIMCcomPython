from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

# ============================================================
# CONFIGS DO BANCO
# ============================================================
DB_HOST = "localhost"
DB_USER = "postgres"
DB_PASS = "SUA SENHA AQUI"  # <- coloque sua senha correta
DB_PORT = "5432"
DB_NAME = "imcdb"

# ============================================================
# FUNÇÃO PARA CRIAR O BANCO (SE NÃO EXISTIR)
# ============================================================
def criar_banco():
    # conecta no banco padrão "postgres" para poder criar outro banco
    conn = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT,
        dbname="postgres"
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # criar banco se não existir
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}';")
    existe = cursor.fetchone()

    if not existe:
        print("📌 Criando banco imcdb...")
        cursor.execute(f"CREATE DATABASE {DB_NAME};")
    else:
        print("✔ Banco já existe.")

    cursor.close()
    conn.close()


# ============================================================
# CONECTAR AO BANCO IMCDB
# ============================================================
def conectar():
    return psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT,
        dbname=DB_NAME
    )


# ============================================================
# CRIAR TABELA SE NÃO EXISTIR
# ============================================================
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            endereco TEXT NOT NULL,
            peso REAL NOT NULL,
            altura REAL NOT NULL,
            imc REAL NOT NULL,
            classificacao TEXT NOT NULL
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("✔ Tabela criada/verificada com sucesso.")


# ============================================================
# FLASK
# ============================================================
app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "Servidor Flask ativo!"


@app.route('/calcular-imc', methods=['POST'])
def calcular_imc():
    data = request.json

    nome = data['nome']
    endereco = data['endereco']
    peso = float(data['peso'])
    altura = float(data['altura'])

    imc = peso / (altura * altura)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc <= 24.9:
        classificacao = "Peso normal"
    elif imc <= 29.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    # salvar no banco
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pacientes (nome, endereco, peso, altura, imc, classificacao)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nome, endereco, peso, altura, imc, classificacao))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "mensagem": f"Olá, {nome}! Seu IMC é {imc:.2f} ({classificacao}).",
        "imc": round(imc, 2),
        "classificacao": classificacao
    })


# ============================================================
# EXECUÇÃO PRINCIPAL — FAZ TUDO AUTOMATICAMENTE
# ============================================================
if __name__ == "__main__":
    print("🔍 Verificando banco...")
    criar_banco()

    print("🔍 Verificando tabela...")
    criar_tabela()

    print("🚀 Iniciando servidor Flask...")
    app.run(host='127.0.0.1', port=2500, debug=True)
