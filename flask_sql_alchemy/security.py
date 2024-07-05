from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import UserModel


def authenticate(username,password):
    # if the username is null we return None
    user = UserModel.find_by_username(username=username)
    if user and check_password_hash(user.password,password):
        return user

 # used when we have an endpoint that requires authentication   
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)