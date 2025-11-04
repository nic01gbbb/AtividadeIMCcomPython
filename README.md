# 🧮 Calculadora de IMC (Flask + React)

Este projeto é uma **aplicação full stack** desenvolvida em **Python (Flask)** no backend e **React** no frontend.  
O objetivo é calcular o **IMC (Índice de Massa Corporal)** de uma pessoa e exibir sua **classificação oficial**, de forma simples e interativa.

---

## 🚀 Tecnologias Utilizadas

### 🔹 Backend
- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)

### 🔹 Frontend
- [React](https://react.dev/)
- [JavaScript (ES6+)](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
- [CSS3](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
- [Axios](https://axios-http.com/) — para requisições HTTP

---

## 📁 Estrutura do Projeto


imc-app/
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── ...
│
├── frontend/
│ ├── src/
│ ├── package.json
│ └── ...
│
└── README.md ← (este arquivo)

yaml

---

## ⚙️ Como Executar o Projeto Localmente

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/nic01gbbb/AtividadeIMCcomPython.git
cd imc-app
2️⃣ Rodar o Backend (Flask)
Entre na pasta do backend:

bash
cd backend
Crie e ative o ambiente virtual:

bash
python -m venv venv
.\venv\Scripts\activate   # no Windows
Instale as dependências:

bash
pip install -r requirements.txt
Inicie o servidor:

bash
python app.py
O servidor Flask rodará em:

arduino
http://localhost:2500
3️⃣ Rodar o Frontend (React)
Abra outro terminal e vá para a pasta frontend:

bash
cd ../frontend
Instale as dependências:

bash
npm install
Inicie o app React:

bash
npm start
O React será aberto automaticamente em:

arduino
http://localhost:3000
🔄 Comunicação Frontend ↔ Backend
O React envia uma requisição POST para o endpoint:

bash
http://localhost:2500/calcular-imc
O backend Flask processa os dados (altura e peso) e retorna:

json
{
  "imc": 26.7,
  "classificacao": "Sobrepeso"
}

🧠 Fórmula do IMC
IMC = peso / (altura * altura)

​Classificação	IMC (kg/m²)
Abaixo do peso	< 18.5
Peso normal	18.5 – 24.9
Sobrepeso	25.0 – 29.9
Obesidade grau I	30.0 – 34.9
Obesidade grau II	35.0 – 39.9
Obesidade grau III	≥ 40.0

🎨 Interface
A interface é simples e responsiva, com campos para:

Nome

Endereço

Altura

Peso

E um botão para calcular o IMC.
Os resultados são exibidos de forma clara, com o IMC e sua classificação.

🌐 Futuras Melhorias
Hospedar o backend no Render e o frontend no Vercel;

Permitir histórico de cálculos;

Mostrar mensagens personalizadas por categoria de IMC.

👨‍💻 Autor
Nicholas Peterson Gonçalves Garcia
📍 Varginha - MG
📧 nicholasfsdev40@gmail.com
📅 Criado em: Novembro de 2025

🏁 Licença
Este projeto é de uso educacional, criado como parte de estudos da disciplina de Python / Desenvolvimento de Sistemas.
