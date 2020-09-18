from flask import Flask
from flask_restful import Resource, Api

application = Flask(__name__)
api = Api(application)

class Sample(Resource):
    def get(self):
        return {"About": "Flask Elb Sample application"}

api.add_resource(Sample, '/')
if __name__== '__main__':
    application.run()