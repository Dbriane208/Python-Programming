from flask import Flask,jsonify,request

app = Flask(__name__)

# POST - as a server, recives data from the user
# GET - as a server, sends data to the user

# mock data for our store
stores = [
    {
        'name':'shop',
        'items': [
            {
            'name':'My item',
            'price':20.00
            }
        ]
    }
]

# POST/store data : {name}
@app.route('/store',methods = ['POST'])
def create_store():
    request_data = request.get_json() 
    new_Store = {
        'name': request_data['name'],
        'items': []
    }  
    stores.append(new_Store)
    return jsonify(new_Store) 

# GET/store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store was not found!'})   

# GET/stores
@app.route('/stores')
def get_stores():
    # returning our stores list as a dictionary
    return jsonify({'stores' : stores})

# POST/store/<string:name>/item{name:,price:}
@app.route('/store/<string:name>/item',methods = ['POST'])
def create_item_in_store(name):
    request_data = request.get_json() 
    for store in stores:
        if store['name'] == name:
            new_item = {
               'name': request_data['name'],
               'price': request_data['price']
            }  
            store['items'].append(new_item)
            return jsonify(new_item) 
    return jsonify({'message':'item was not created!'})  

# GET/store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message':'store was not found!'})   

# run the app
app.run(port=5002)