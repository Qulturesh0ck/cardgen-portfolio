from flask import Blueprint, jsonify, abort, request
from ..models import Card, User, GeneratedCard, db
from ..cardgenprotoV2 import GenerateCard
from  .generatedcard import create_with_app
bp = Blueprint('cards', __name__, url_prefix='/cards')
extra = Blueprint('generatedcards',__name__, url_prefix='/generatedcards')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    cards = Card.query.all() # ORM performs SELECT query
    result = []
    for c in cards:
        result.append(c.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    c = Card.query.get_or_404(id)
    return jsonify(c.serialize())

@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id, name, image, description, bp, and hp
    if not all(key in request.json for key in ('user_id', 'name', 'image', 'description', 'bp', 'hp')):
        return abort(400)

    # user with id of user_id must exist
    User.query.get_or_404(request.json['user_id'])

    # construct Card
    c = Card(
        user_id=request.json['user_id'],
        name=request.json['name'],
        image=request.json['image'],
        description=request.json['description'],
        bp=request.json['bp'],
        hp=request.json['hp']
    )

    # commit Card to database
    db.session.add(c)
    db.session.commit()

    # generate card image and create GeneratedCard object
    g = create_generated_card({'user_id': request.json['user_id'], 'card_id': c.card_id})
    if not g:
        return abort(500)

    return jsonify(c.serialize())

@extra.route('', methods=['POST'])
def create_generated_card(data):
    user_id = data.get('user_id')
    card_id = data.get('card_id')
    if not user_id or not card_id:
        return abort(400)

    response = GenerateCard(card_id)
    if response:
        g = GeneratedCard(
            user_id=user_id,
            imagepath=response['imagepath'],
            card_id=card_id
        )
        db.session.add(g)
        db.session.commit()
        return jsonify(g.serialize())
    else:
        return abort(500)

"""
@bp.route('', methods=['POST'])
def create():
    # req body must contain and content
        if 'user_id' not in request.json:
            return abort(400)
        # user with id of user_id must exist
        User.query.get_or_404(request.json['user_id'])
        #Card.query.get_or_404(request.json['card_id'])
        # construct Card
        c = Card(
            user_id=request.json['user_id'],
            name=request.json['name'],
            image=request.json['image'],
            description=request.json['description'],
            bp=request.json['bp'],
            hp=request.json['hp']
        )
        db.session.add(c) # prepare CREATE statement
        db.session.commit() # execute CREATE statement
        create_with_app()
        return jsonify(c.serialize())
"""        
    

@bp.route('/<int:id>', methods=['PUT'])
def edit(id: int):
    pass



@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    c = Card.query.get_or_404(id)
    try:
        db.session.delete() # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


### Start Tests

@bp.route('userless', methods=['POST'])
def createUserles():
    # req body must contain and content
    if 'user_id' not in request.json:
        return abort(400)
    # user with id of user_id must exist
    User.query.get_or_404(request.json['user_id'])
    #Card.query.get_or_404(request.json['card_id'])
    # construct Card
    c = Card(
        user_id=request.json['user_id'],
        name=request.json['name'],
        image=request.json['image'],
        description=request.json['description'],
        bp=request.json['bp'],
        hp=request.json['hp']
    )
    db.session.add(c) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(c.serialize())#

### End Tests 


