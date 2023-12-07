import React, { useState } from "react";
import axios from "axios";
import './App.css';

function App() {
  const [charName, setCharName] = useState('');
  const [charData, setCharData] = useState(null);
  const [gifs, setGifs] = useState(null);
  const [error, setError] = useState('');

  const fetchCharData = async () => {
    try {
      const response = await axios.get(`http://localhost:1234/char/${charName}`);
      setCharData(response.data.charData[0]);
      response.data.charData[0] ? setGifs(response.data.gifs) : setGifs(null);
      response.data.charData[0] ? setError('') : setError('Personagem não encontrado.');
    } catch (error) {
      console.error(error);
      setError('Erro ao obter dados do personagem!');
    }
  };

  return (
    <div className="container">
      <div className="header">
      <img src="/images/header.jpg" alt="Marvel Logo" draggable="false" />
      </div>

      <div className="search-container">
        <input
          className="search-input"
          type="text"
          value={charName}
          onChange={(e) => setCharName(e.target.value)}
          placeholder="Enter the name of the character (or group)"
        />
        <button className="search-button" onClick={fetchCharData}>
          Search
        </button>
      </div>

      {error && <p className="error-message">{error}</p>}

      {charData && (
        <div className="result-container">
          <h2>{charData.name}</h2>
          <img src={`${charData.thumbnail.path}.${charData.thumbnail.extension}`} alt={charData.name} />
          <p className="character-info">{charData.description}</p>
          
          <div className="gif-container">
            {gifs && gifs.slice(0, 12).map((gif) => (
              <div className="gif-item">
                <img src={gif.images.original.url} alt="GIF relacionado ao personagem" />
              </div>
            ))
          }</div>
        </div>
      )}
    </div>
  );
}

export default App;
