from flask import Flask

# creating an object of the Flask class
# __name__ gives each file a unique name
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"

app.run(port=5001)
