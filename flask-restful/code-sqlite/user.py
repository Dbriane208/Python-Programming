import sqlite3
from flask_restful import Resource,reqparse

class User:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        # Establishing a connection
        connection = sqlite3.connect("data.db")  
        cursor = connection.cursor() 

        # creating a username query
        query = "SELECT * FROM users WHERE username =?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()

        # print the details of the result
        if row:
            user = cls(*row)
        else:
            user = None
            connection.close()
        return user        

    @classmethod
    def find_by_id(cls,_id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query,(_id,))
        # returns the only row with the result from the query
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
            connection.close()
        return user    

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
        if User.find_by_username(data['username']):
            return {"message":"A user with the same name already exists!"}

        # Establish a connection
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() 

        query = "INSERT INTO users VALUES(NULL,?,?)"
        cursor.execute(query,(data['username'],data['password']))

        # closing the connection
        connection.commit()
        connection.close()
        return {"message":"User created successfully"}, 201  

