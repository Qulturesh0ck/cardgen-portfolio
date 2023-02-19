import { useEffect, useState } from 'react';
import axios from "axios"
import { format } from "date-fns";
import './App.css';
import { Card, User } from './models.py'

const baseUrl = "http://localhost:5000"
//const card = [Card]


function Navbar() {
  return (
    <div className="navbar">
      <img src="images\logo.png" alt="logo" className="navlogo" />
      <div className="header">
        <h1>Card Generator α</h1>
      </div>
      <div className="upper">
        <button className="topbutton" type="button" onClick={() => console.log('Login')}>Login</button>
        <button className="topbutton" type="button" onClick={() => console.log('Logout')}>Logout</button>
        <button className="topbutton" type="button" onClick={() => console.log('Load')}>Load</button>
      </div>
    </div >
  );
}


function CardImage() {
  return (
    <section className="genCard" >
      <img src="images\cardmockupALPH1.png" alt="Placeholder" />
    </section>
  );


}




function CardImagetest() {
  {
    {
      const [cardImage, setCardImage] = useState([])

      useEffect(() => {
        fetch('http://127.0.0.1:5000/cards', {
          'methods': 'GET',
          //withCredentials: true,
          //mode: 'no-cors',
          headers: {
            'Content-Type': 'application/json'
          }
        })
          .then(resp => resp.json())
          .then(resp => setCardImage(resp))
          .catch(error => console.log(error))
      }, [])



      return (
        <section className="genCard">
          <h2>Placeholder value</h2>
          {cardImage.map(card => {
            return (
              <section key={card.id}>
                <h2>{card.name}</h2>
              </section>
            )
          })}
        </section>
      )
    }
  }
}


function CardImagePath() {
  {
    {
      const [cardImage, setCardImage] = useState([])

      useEffect(() => {
        fetch('http://127.0.0.1:5000/generatedcards', {
          'methods': 'GET',
          //withCredentials: true,
          //mode: 'no-cors',
          headers: {
            'Content-Type': 'application/json'
          }
        })
          .then(resp => resp.json())
          .then(resp => setCardImage(resp))
          .catch(error => console.log(error))
      }, [])



      return (
        <section className="genCard">
          <h2>Testing Card Image</h2>
          {cardImage.map(card => {
            return (
              <section key={card.gen_id}>
                <img src={"http://localhost:3000/images/Gencards/" + card.imagepath} alt="Placeholder" />
                <h2>{card.imagepath}</h2>
              </section>
            )
          })}
        </section>
      )
    }
  }
}


function Form() {
  const [cardName, setCardName] = useState('');
  const [cost, setCost] = useState('');
  const [cardClass, setCardClass] = useState('');
  const [cardType, setCardType] = useState('Artifact');
  const [alignment, setAlignment] = useState('Air');
  const [battlePoints, setBattlePoints] = useState('');
  const [healthPoints, setHealthPoints] = useState('');
  const [description, setDescription] = useState('');

  fetch('')

  return (
    <main className="flex-container">
      <section className="keySpace"></section>
      <section className="genForm">
        <form>
          <div className="form-container">
            <label htmlFor="cardName">Name</label>

            <input
              type="text"
              id="cardName"
              name="cardName"
              value={cardName}
              onChange={(e) => setCardName(e.target.value)}
            />
          </div>
          <div className="form-container">
            <label htmlFor="PHcost">Cost</label>
            <input
              type="text"
              value={cost}
              onChange={(e) => setCost(e.target.value)}
            />
          </div>
          <div className="form-container">
            <label htmlFor="PHclass">Class</label>
            <input
              type="text"
              value={cardClass}
              onChange={(e) => setCardClass(e.target.value)}
            />
          </div>
          <div className="form-container">
            <label htmlFor="cardType">Card Type</label>
            <select
              name="cardPicker"
              id="cardPicker"
              value={cardType}
              onChange={(e) => setCardType(e.target.value)}
            >
              <option value="Artifact">Artifact</option>
              <option value="Magic">Magic</option>
              <option value="Champion">Champion</option>
              <option value="Creature">Creature</option>
              <option value="Source">Source</option>
            </select>
          </div>
          <div className="form-container">
            <label htmlFor="PHalignment">Alignment</label>

            <select
              name="alingmentPicker"
              id="alingmentPicker"
              value={alignment}
              onChange={(e) => setAlignment(e.target.value)}
            >
              <option value="Air">Air</option>
              <option value="Blood">Blood</option>
              <option value="Earth">Earth</option>
              <option value="Fire">Fire</option>
              <option value="Radiant">Radiant</option>
              <option value="Shadow">Shadow</option>
              <option value="Water">Water</option>
            </select>
          </div>
          <div className="form-container">
            <label htmlFor="statLine1">Battle Points</label>
            <input
              type="text"
              className="statLine"
              id="statLine1"
              name="statLine1"
              value={battlePoints}
              onChange={(e) => setBattlePoints(e.target.value)}
            />
            <label htmlFor="statLine2">Health Points</label>
            <input
              type="text"
              className="statLine"
              id="statLine2"
              name="statLine2"
              value={healthPoints}
              onChange={(e) => setHealthPoints(e.target.value)}
            />
          </div>
          <div className="form-container">
            <textarea
              id="description"
              name="description"
              rows="10"
              cols="35"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
            >
              Enter card text...
            </textarea>
          </div>
          <div className="buttonContainer">
            <button type="button" onClick={() => console.log('Save')}>
              Save
            </button>
            <button type="button" onClick={() => console.log('Load')}>
              Load
            </button>
            <button type="button" onClick={() => console.log('Clear')}>
              Clear
            </button>
            <button type="button" onClick={() => console.log('Export')}>
              Export
            </button>
          </div>
        </form>
      </section >
      <CardImagePath />
    </main >
  );
}





function App() {
  return (
    <div>
      <Navbar />
      <Form />
    </div>
  );
}

export default App;

