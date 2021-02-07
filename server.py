from flask import Flask, json, jsonify, request, render_template


app = Flask(__name__)
stores=[
    {
        'name': 'Pavans Store',
        'items': [
            {
                'name':'item1',
                'price': 9.99
            }
        ]
    }
]
#home
@app.route('/')
def home():
    return render_template('index.html')


# Creating a new store to the List stores as a dictionary
@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    print (request_data)
    new_store = {
        'name' : request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

# /retrieve a store by iterating over a store and if store name matches, return that and if not, return error message
@app.route('/store/<string:name>')
def get_one_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'Message': 'Store not found'})
    

    
# return all the stores present in our list
@app.route("/store")
def get_store():
    return jsonify({'stores': stores})

# creating an item in a store
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_a_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'Message': 'Store Not found'})

# Return all items in a store
@app.route('/store/<string:name>/item')
def get_items_in_a_store(name):
    # run other code here.
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items'] })
    return jsonify({'Message': 'Store Not Found'})