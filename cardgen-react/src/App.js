import { useEffect, useState } from 'react';
import './App.css';
/*
import axios from "axios";
import { format } from "date-fns";
import { Card, User } from './models.py';
import CardNameList from './components/CardNameList.js';
import Login from './components/UserLogin';
import SaveCardData from './components/SaveCardTesting.js'
const card = [Card]
*/

function CardNameList2() {
  {
    const baseUrl = 'http://127.0.0.1:5000/'
    const [selectedCardID, setSelectedCardID] = useState("");
    const [selectedCardImage, setSelectedCardImage] = useState("");
    const [cardName, setCardName] = useState([])
    useEffect(() => {
      fetch(`${baseUrl}generatedcards`, {
        'methods': 'GET',
        //withCredentials: true,
        //mode: 'no-cors',
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(resp => resp.json())
        .then(resp => setCardName(resp))
        .catch(error => console.log(error))
    }, []);

    const handleLoadImage = () => {
      fetch(`http://127.0.0.1:5000/images/Gencards/${selectedCardID}`, {
        methods: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.blob())
        .then((resp) => setSelectedCardImage(URL.createObjectURL(resp)))
        .catch((error) => console.log(error));
    };

    const handleSelectChange = (event) => {
      setSelectedCardID(event.target.value);
      setSelectedCardImage("");
    };

    return (
      <section className='genCard'>
        <div className='cardList'>
          <select onChange={handleSelectChange} value={{ selectedCardID }}>
            <option value="">--Select a card--</option>
            {cardName.map(list => {
              return (
                <option key={list.imagepath} value={list.imagepath}>
                  {list.card_name}
                </option>
              )
            })}
          </select>
          <button onClick={handleLoadImage} disabled={!{ selectedCardID }}>
            Load
          </button>
          <CardImagePath selectedCardID={selectedCardID} />
        </div>
      </section >
    )
  }
}


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

function CardImagePath(props) {
  {
    {
      const baseURL = 'http://127.0.0.1:5000/'
      const frontEndURL = 'http://127.0.0.1:3000/images/Gencards/'
      const [cardImage, setCardImage] = useState([])

      useEffect(() => {
        fetch(`${baseURL}generatedcards/${props.selectedCardID}`, {
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
      }, [props.selectedCardID])



      return (
        <section className="genCard">
          <h2>Testing Card Image</h2>

          <section className="genCard">
            <h2>{props.selectedCardID}</h2>
            <img src={frontEndURL + props.selectedCardID} alt="Generated Card" />
          </section>
        </section>
      )
    }
  }
}




function Form() {
  const [name, setCardNameForm] = useState('');
  const [cost, setCost] = useState('');
  const [cardClass, setCardClass] = useState('');
  const [cardType, setCardType] = useState('Artifact');
  const [alignment, setAlignment] = useState('Air');
  const [bp, setBattlePoints] = useState('');
  const [hp, setHealthPoints] = useState('');
  const [description, setDescription] = useState('');
  const [cardData, setCardData] = useState([]);
  const [image, setImage] = useState('');
  const user_id = 1;
  //const [user_idDELETE, getUser] = useState(user.user_id)
  const handleSave = (e) => {
    e.preventDefault();
    const formData = {
      user_id,
      name,
      image,
      //cost,
      //cardClass,
      //cardType,
      //alignment,
      bp,
      hp,
      description,
    };
    fetch('http://127.0.0.1:5000/cards', {
      method: 'POST',
      //mode: 'no-cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
      .then(resp => resp.json())
      .then(data => {
        setCardData([...cardData, data]);
        console.log('Card data saved successfully!');
      })
      .catch(error => console.error(error));
  };

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
              value={name}
              onChange={(e) => setCardNameForm(e.target.value)}
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
              name="alignmentPicker"
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
          <div className='form-container'>
            <label
              htmlFor="img"
            >Select image:</label>
          </div>
          <div className="form-container">

            <input
              type="file"
              id="img"
              name="img"
              accept="image/png, image/jpeg"
              value={image}
              onChange={(e) => setImage(e.target.value)} />
            <label htmlFor="statLine1">Battle Points</label>
            <input
              type="text"
              className="statLine"
              id="statLine1"
              name="statLine1"
              value={bp}
              onChange={(e) => setBattlePoints(e.target.value)}
            />
            <label htmlFor="statLine2">Health Points</label>
            <input
              type="text"
              className="statLine"
              id="statLine2"
              name="statLine2"
              value={hp}
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
            <button type="button" onClick={handleSave}>
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
      <CardNameList2 />
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

