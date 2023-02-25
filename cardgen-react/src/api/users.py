from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Card #,cards_table
import hashlib
import secrets
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token

def scramble(password: str):
    """Hash and salt the given password"""
    return hashlib.sha512((password).encode('utf-8')).hexdigest()


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


###Test this later !!!

@bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 400

    if user.password != hashlib.sha512((password).encode('utf-8')).hexdigest():
        return jsonify({'message': 'Incorrect password'}), 400

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200
### Test this later !!
""""""


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
