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
Copiar código

---

## ⚙️ Como Executar o Projeto Localmente

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/imc-app.git
cd imc-app
2️⃣ Rodar o Backend (Flask)
Entre na pasta do backend:

bash
Copiar código
cd backend
Crie e ative o ambiente virtual:

bash
Copiar código
python -m venv venv
.\venv\Scripts\activate   # no Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Inicie o servidor:

bash
Copiar código
python app.py
O servidor Flask rodará em:

arduino
Copiar código
http://localhost:2500
3️⃣ Rodar o Frontend (React)
Abra outro terminal e vá para a pasta frontend:

bash
Copiar código
cd ../frontend
Instale as dependências:

bash
Copiar código
npm install
Inicie o app React:

bash
Copiar código
npm start
O React será aberto automaticamente em:

arduino
Copiar código
http://localhost:3000
🔄 Comunicação Frontend ↔ Backend
O React envia uma requisição POST para o endpoint:

bash
Copiar código
http://localhost:2500/calcular-imc
O backend Flask processa os dados (altura e peso) e retorna:

json
Copiar código
{
  "imc": 26.7,
  "classificacao": "Sobrepeso"
}
🧠 Fórmula do IMC
𝐼
𝑀
𝐶
=
𝑝
𝑒
𝑠
𝑜
(
𝑎
𝑙
𝑡
𝑢
𝑟
𝑎
)
2
IMC= 
(altura) 
2
 
peso
​
 
Classificação	IMC (kg/m²)
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
