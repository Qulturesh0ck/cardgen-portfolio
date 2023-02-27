import React, { useState, useEffect } from 'react'

function CardNameList(props) {
    {
        const [cardName, setCardName] = useState([])

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
                .then(resp => setCardName(resp))
                .catch(error => console.log(error))
        }, [])

        {
            props.cardName && props.cardName.map(card => {
                return (

                    <section>
                        <h1>{card.name}</h1>
                        <select key={card.name}>
                            <option key={card.name} value={cardName}></option>
                        </select>
                    </section>
                )
            })
        }
    }
}

export default CardNameList
