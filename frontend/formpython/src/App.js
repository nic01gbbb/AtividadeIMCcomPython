import React, {useState} from "react";
import "./App.css";

function App() {
    const [nome, setNome] = useState("");
    const [endereco, setEndereco] = useState("");
    const [altura, setAltura] = useState("");
    const [peso, setPeso] = useState("");
    const [resultado, setResultado] = useState("");

    const calcularIMC = async () => {
        if (!nome || !endereco || !altura || !peso) {
            alert("⚠️ Por favor, preencha todos os campos antes de calcular.");
            return; // interrompe a execução
        }

        try {
            const response = await fetch("http://localhost:2500/calcular-imc", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    nome: nome,
                    endereco: endereco,
                    altura: parseFloat(altura),
                    peso: parseFloat(peso),
                }),
            });
            const data = await response.json();
            console.log(data.mensagem)
            setResultado(data.mensagem);
        } catch (error) {
            setResultado("Erro ao calcular o IMC.");
        }
    };

    const reiniciar = () => {
        setNome("");
        setEndereco("");
        setAltura("");
        setPeso("");
        setResultado("");
    };

    const sair = () => {
        window.close();
    };

    return (
        <div className="container">
            <h2>Cálculo do IMC - Índice de Massa Corporal</h2>

            <label>Nome do Paciente:</label>
            <input value={nome} onChange={(e) => setNome(e.target.value)}/>

            <label>Endereço Completo:</label>
            <input value={endereco} onChange={(e) => setEndereco(e.target.value)}/>

            <div className="row">
                <div className="col">
                    <label>Altura (cm):</label>
                    <input value={altura} onChange={(e) => setAltura(e.target.value)}/>
                    <label>Peso (Kg):</label>
                    <input value={peso} onChange={(e) => setPeso(e.target.value)}/>
                </div>

                <div className="resultado-box">
                    {resultado || "Resultado"}
                </div>
            </div>

            <div className="botoes">
                <button onClick={calcularIMC}>Calcular</button>
                <button onClick={reiniciar}>Reiniciar</button>
                <button onClick={sair}>Sair</button>
            </div>
        </div>
    );
}

export default App;
