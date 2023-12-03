import React, { useState } from "react";
import axios from "axios";
import './App.css';

function App() {
  const [charName, setCharName] = useState('');
  const [charData, setCharData] = useState(null);
  const [gifUrl, setGifUrl] = useState('');
  const [error, setError] = useState('');

  const fetchCharData = async () => {
    try {
      const response = await axios.get(`http://localhost:1234/char/${charName}`);
      
      setCharData(response.data.charData[0]);
      const index = Math.floor(Math.random() * 50);
      response.data.charData[0] ? setGifUrl(response.data.gifs[index].images.original.url) : setGifUrl('');
      response.data.charData[0] ? setError('') : setError('Personagem não encontrado.');
    } catch (error) {
      console.error(error);
      setError('Erro ao obter dados do personagem!');
    }
  };

  return (
    <div className="App">
      <h1>Marvel Character Explorer</h1>
      <label>
        Character's Name:
        <input type="text" value={charName} onChange={(e) => setCharName(e.target.value)} />
      </label>
      <button onClick={fetchCharData}>Search</button>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {charData && (
        <div>
          <h2>{charData.name}</h2>
          <p>{charData.description}</p>
          <img src={`${charData.thumbnail.path}.${charData.thumbnail.extension}`} alt={charData.name} />

          {gifUrl && <img src={gifUrl} alt="GIF relacionado ao personagem" />}
        </div>
      )}
    </div>
  );
}

export default App;
