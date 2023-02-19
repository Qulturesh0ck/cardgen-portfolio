from flask import Blueprint, jsonify, abort, request
from ..models import Card, User, GeneratedCard,  db


bp = Blueprint('generatedcards', __name__, url_prefix='/generatedcards')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    generatedCard = GeneratedCard.query.all() # ORM performs SELECT query
    result = []
    for g in generatedCard:
        result.append(g.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response



@bp.route(f'/images/Gencards/<string:imagepath>', methods=['GET'])
def show(imagepath: str):
    g = GeneratedCard.query.get_or_404(imagepath)
    return f'/images/Gencards/{g}'

@bp.route('', methods=['POST'])
def create():
    if 'user_id' not in request.json or 'card_id' not in request.json:
        return abort(400)
    User.query.get_or_404(request.json['user_id'])
    Card.query.get_or_404(request.json['card_id'])
    g = GeneratedCard(
        user_id=request.json['user_id'],
        imagepath=request.json['imagepath'],
        card_id=request.json['card_id']
    )
    db.session.add(g) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(g.serialize())

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