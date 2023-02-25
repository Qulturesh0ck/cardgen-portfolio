from PIL import Image, ImageDraw, ImageFont
from flask_cors import CORS
import requests
def GenerateCard(id):
    trueURL = f"http://localhost:5000/cards"
    response = requests.get(f"{trueURL}/{id}")
    if response.ok:
        data = response.json()
        #print(f"Generating image for {trueURL}/{id}")
        #for item in data:
            #print(item)
    else:
        print("ERROR")

    # -- Put fonts here
    fontLora = ImageFont.truetype("Lora-VariableFont_wght.ttf", size=65)
    fontLora45 = ImageFont.truetype("Lora-VariableFont_wght.ttf", size=45)
    # -- End Fonts

    uploadedImg = Image.open("src/images/magmawyrm.png")
    templateChoice = Image.open("src/images/CardTemplates/OrangeCardTemplate.png")
    draw = ImageDraw.Draw(templateChoice)

    cardNameWidth = 1010
    cardNameheight = 109
    maxWidthName = cardNameWidth - 50
    minHeightName = cardNameheight - 5


    template = templateChoice
    cardNameString = f"{data['name']}"

    bBoxcardName = draw.textbbox(
        (100, 100), f"{cardNameString}", font=fontLora)
    bBox = draw.textbbox(
        (100, 100), f"{cardNameString}", font=fontLora)

    cardNameWidth = bBoxcardName[2] - bBoxcardName[0]
    cardNameHeight = bBoxcardName[3] - bBoxcardName[1]
    txtWidthName = bBox[2] - bBox[0]

    #cardName
    draw.text((155, 115, 10, 10+minHeightName),
                        cardNameString, font=fontLora, fill='#191919')
    
    img = uploadedImg

    #cardDesc 
    draw.text((125, 1414), f"{data['description']}"
                        , font=fontLora45, fill='#191919')

    #battlePoints
    draw.text((780, 1680), f"BP/ {data['bp']}"
                        , font=fontLora45, fill='#191919')

    #healthPoints
    draw.text((970, 1680), f"HP/ {data['hp']}", font=fontLora45, fill='#191919')

    #genCard
    template.paste(img, (189, 323))
    print(f"Saving template... to ./images/Gencards/user{data['user_id']}_card{data['card_id']}.png")
    #Save image
    imagepath = f"{data['user_id']}_{data['card_id']}.png"
    filename = f"./public/images/Gencards/{data['user_id']}_{data['card_id']}.png"
    template.save(f"{filename}", format='PNG')

    return {
		"card_id": data['card_id'],
		"card_name": cardNameString,
		"imagepath": imagepath,
        "user_id": data['user_id']
    }






###
# Name box x-155 y-115
# Class Spot x-128, y-1410
#  artbox dimensions: x-646 y-794
# topleft corner: 194,324
# bottomright corner: 1099, 1266
# resize 905 924
# note 188
