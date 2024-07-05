import sqlite3
from models.user_model import UserModel
from flask_restful import Resource,reqparse
from werkzeug.security import generate_password_hash

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        # check for Duplicates
        if UserModel.find_by_username(data['username']):
            return {"message":"A user with the same name already exists!"}

        # Establish a connection
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() 

        query = "INSERT INTO users VALUES(NULL,?,?)"
        cursor.execute(query,(data['username'],generate_password_hash(data['password'])))

        # closing the connection
        connection.commit()
        connection.close()
        return {"message":"User created successfully"}, 201  

