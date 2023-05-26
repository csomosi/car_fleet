from flask import Flask
from flask_restful import Resource, Api

from resources.car import Car

app = Flask(__name__)
api = Api(app)

api.add_resource(Car, '/car/<string:plate>')