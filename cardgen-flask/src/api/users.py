from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Card #,cards_table
import hashlib
import secrets
from flask_sqlalchemy import SQLAlchemy

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all()  # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize())  # build list of Users as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)

    if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        return abort(400)

    u = User(
        username=request.json['username'],
        password=scramble(request.json['password'])
    )

    db.session.add(u)
    db.session.commit()
    return jsonify(u.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)

    try:
        db.session.delete(u)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    u = User.query.get_or_404(id)

    if 'username' not in request.json and 'password' not in request.json:
        return abort(400)

    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        u.username = request.json['username']
    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        u.password = request.json['password']

    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)

'''

@bp.route('/<int:id>/created_cards', methods=['GET'])
def created_cards(id: int):
    u = User.query.get_or_404(id)
    result = []
    for c in u.created_cards:
        result.append(c.serialize())
    return jsonify(result)


# ################
# #### BONUS  ####
# ################


@bp.route('/<int:id>/cards', methods=['POST'])
def like(id: int):
    if 'card_id' not in request.json:
        return abort(400)

    card_id = request.json['card_id']

    # check user and tweet exist
    User.query.get_or_404(id)
    Card.query.get_or_404(card_id)

    try:
        stmt = sqlalchemy.insert(cards_table).values(
            user_id=id, card_id=card_id)
        db.session.execute(stmt)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)


@bp.route('/<int:user_id>/cards/<int:card_id>', methods=['DELETE'])
def unlike(user_id: int, card_id: int):
    # check user and tweet exist
    User.query.get_or_404(user_id)
    Card.query.get_or_404(card_id)

    try:
        stmt = sqlalchemy.delete(cards_table).where(
            cards_table.c.user_id == user_id,
            cards_table.c.card_id == card_id
        )
        db.session.execute(stmt)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

'''
