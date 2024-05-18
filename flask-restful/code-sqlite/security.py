from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username,password):
    # if the username is null we return None
    user = User.find_by_username(username=username)
    if user and safe_str_cmp(user.password,password):
        return user

 # used when we have an endpoint that requires authentication   
def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)