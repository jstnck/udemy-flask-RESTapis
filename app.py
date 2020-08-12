from flask import Flask 
from flask_restful import Api
from flask_jwt import JWT



from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


#flask restful does jsonfiy for us, so we dont need it

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.secret_key = 'justin'





#jwt creats a new entdpoint, called /auth
jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')

#only run app.run if we run app.py. wont run if we 
# import app.py into another file (we probably dont want to start flask in that case)
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)



