from flask import Blueprint, Response, request
from models import User
from extensions import db

apiUser = Blueprint(
    "apiUser",
    __name__,
    url_prefix="/api/user"
)


@apiUser.route("/", methods=["GET"])
def index():

    users = User.query.all()

    result = []

    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })

    return result


@apiUser.route("/ekle/", methods=["GET","POST"])
def add_user():

  
    data = request.get_json()

    new_user = User(
        name=data["name"],
        email=data["email"]
    )

    db.session.add(new_user)
    db.session.commit()

    return {
        "message": "Kullanıcı başarıyla eklendi",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }
    }, 201


@apiUser.route("/profile/")
def userr():
    return Response("user api")