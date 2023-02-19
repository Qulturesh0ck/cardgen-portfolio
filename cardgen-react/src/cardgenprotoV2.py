from PIL import Image, ImageDraw, ImageFont
from flask_cors import CORS
# Version 2
# -- Put fonts here
fontLora = ImageFont.truetype("Lora-VariableFont_wght.ttf", size=65)


# -- End Fonts


uploadedImg = Image.open("images\SAM.png")
templateChoice = Image.open("images\BlackCardTemplate.png")
draw = ImageDraw.Draw(templateChoice)


cardNameWidth = 1010
cardNameheight = 109
maxWidthName = cardNameWidth - 50
minHeightName = cardNameheight - 5


template = templateChoice
cardNameString = "How Long Can I Possibly Make This Before I Break It Baby"

bBoxcardName = draw.textbbox(
    (100, 100), f"{cardNameString}", font=fontLora)
bBox = draw.textbbox(
    (100, 100), "How Long Can I Possibly Make T", font=fontLora)

cardNameWidth = bBoxcardName[2] - bBoxcardName[0]
cardNameHeight = bBoxcardName[3] - bBoxcardName[1]
txtWidthName = bBox[2] - bBox[0]


while cardNameWidth > maxWidthName:
    fontLora = ImageFont.truetype(
        "Lora-VariableFont_wght.ttf", fontLora.size - 1)
    cardNameWidth = draw.textlength(cardNameString, font=fontLora)


while cardNameHeight < minHeightName:
    fontLora = ImageFont.truetype(
        "Lora-VariableFont_wght.ttf", fontLora.size + 1)
    newbBox = draw.textbbox((10, 10), f"{cardNameString}", font=fontLora)
    cardNameHeight = newbBox[3] - newbBox[1]

newWidth = cardNameWidth * minHeightName / cardNameHeight

cardName = draw.text((155, 115, 10+newWidth, 10+minHeightName),
                     cardNameString, font=fontLora, fill='#0000')
img = uploadedImg
cardDesc = "PH"
battlePoints = "PH"
healthPoints = "PH"

genCard = template.paste(img, (189, 323))
template.save(f"images\Gencards\{cardNameString}.png")


# FINISH THIS TODAY
# Name box x-155 y-115
# Class Spot x-128, y-1410


"""

Deprecated method

dontUse, txtHeight = draw.textsize(cardNameString, font=fontLora)
while txtHeight < minHeightName:
    fontLora = ImageFont.truetype(
        "Lora-VariableFont_wght.ttf", fontLora.size - 1)
    txtHeight = draw.textsize(cardNameString, font=fontLora)
"""

"""

template = Image.open("CardTemplates/OrangeCardTemplate.png")
pic = Image.open(
    "images/SAM.png").resize((911, 944), Image.ANTIALIAS)

card = template.paste(pic, (189, 323))

template.save("images/Gencards/Genimage.png")
"""
#  artbox dimensions: x-646 y-794
# topleft corner: 194,324
# bottomright corner: 1099, 1266
# resize 905 924
# note 188
