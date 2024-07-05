from werkzeug.security import safe_str_cmp
from flask_sql_alchemy.models.user_model import UserModel


def authenticate(username,password):
    # if the username is null we return None
    user = UserModel.find_by_username(username=username)
    if user and safe_str_cmp(user.password,password):
        return user

 # used when we have an endpoint that requires authentication   
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)