import React, { useState } from "react";
import axios from "axios";

function App() {
  const [pergunta, setPergunta] = useState("");
  const [resposta, setResposta] = useState("");

  const perguntar = async () => {
    const res = await axios.post("/perguntar", { pergunta });
    setResposta(res.data.resposta);
  };

  return (
    <div>
      <h1>Me pergunte algo!</h1>
      <input
        value={pergunta}
        onChange={(e) => setPergunta(e.target.value)}
        placeholder="Digite sua dúvida"
      />
      <button onClick={perguntar}>Perguntar</button>
      <p><strong>Resposta:</strong> {resposta}</p>
    </div>
  );
}

export default App;