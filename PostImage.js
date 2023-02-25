import React, { useState } from 'react';

function ImageUpload() {
    const [image, setImage] = useState('');

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();

        reader.onload = () => {
            const dataURL = reader.result;
            setImage(dataURL);
        };

        reader.readAsDataURL(file);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const response = await fetch('http://localhost:5000/images', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image }),
        });

        const data = await response.json();

        // handle response from server
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Upload Image:
                <input type="file" accept="image/*" onChange={handleImageChange} />
            </label>
            <br />
            <button type="submit">Upload</button>
        </form>
    );
}

export default ImageUpload;