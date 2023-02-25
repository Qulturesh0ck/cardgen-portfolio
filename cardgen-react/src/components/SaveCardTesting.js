import { useState, useEffect } from "react"

function SaveCardData(props) {
    {
        const saveCard = (cardData) => {
            props.saveCard(cardData)
        }
        {


            useEffect(() => {
                fetch('http://127.0.0.1:5000/cards', {
                    'methods': 'POST',
                    //withCredentials: true,
                    //mode: 'no-cors',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                    .then(resp => resp.json())
                    .then(resp => setCardData(resp))
                    .catch(error => console.log(error))
            }, [])




        }
    }
}

export default SaveCardData()