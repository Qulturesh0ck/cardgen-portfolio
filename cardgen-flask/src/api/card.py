from flask import Blueprint, jsonify, abort, request
from ..models import Card, User, db


bp = Blueprint('cards', __name__, url_prefix='/cards')

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
    return jsonify(c.serialize())

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