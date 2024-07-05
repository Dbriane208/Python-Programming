from flask import Flask

from flask_restful import Api

from security import authenticate,identity
from resources.user import UserRegister
from resources.items import Items,Item

app = Flask(__name__)
app.secret_key = "Daniel"
api = Api(app)

# represents the auth endpoint => /auth
# jwt = JWT(app,authenticate,identity) 
  
api.add_resource(Items,'/v1/items')     
api.add_resource(Item,'/v1/item/<string:name>')
api.add_resource(UserRegister,'/v1/register')

# preventing the app from running from another file if app was imported
if __name__ == '__main__':
  app.run(port=5000,debug=True)    
