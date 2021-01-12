from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
def hello():
    return jsonify({'text':'Hello World!'})

class Woolballs(Resource):
    def get(self):
        return {
            'woolballs': [
                {
                    'id': 0, 
                    'brand': "dmc", 
                    'designation': "natura-xl", 
                    'price': "8,05", 
                    'currency': "€", 
                    'needle_size': "8 mm", 
                    'wool_composition': "100% Baumwolle"
                },
                {
                    'id': 1, 
                    'brand': "drops", 
                    'designation': "safran", 
                    'price': "1,48", 
                    'currency': "€", 
                    'needle_size': "3 mm", 
                    'wool_composition': "100% Baumwolle"
                },
                {
                    'id': 2, 
                    'brand': "drops", 
                    'designation': "baby-merino-mix", 
                    'price': "2,72", 
                    'currency': "€", 
                    'needle_size': "3 mm", 
                    'wool_composition': "100% Merinowolle"
                }
            ]
        } 

class Woolballs_Name(Resource):
    def get(self, woolball_id):
        print('Wollball id:' + woolball_id)
        result = {
            'data': 
                {
                    'id': 0, 
                    'brand': "dmc", 
                    'designation': "natura-xl", 
                    'price': "8,05", 
                    'currency': "€", 
                    'needle_size': "8 mm", 
                    'wool_composition': "100% Baumwolle"
                }
            }
        return jsonify(result)


api.add_resource(Woolballs, '/woolballs') # Route_1
api.add_resource(Woolballs_Name, '/woolballs/<woolball_id>') # Route_3


if __name__ == '__main__':
   app.run(port=5000)