from flask import Flask
from flask_restful import Api, Resource
from redis import Redis

app = Flask(__name__)
api = Api(app)



class Visits(Resource):

    def get(self):
        try:
            client = Redis(host='redis', port=6379)
            visits = client.get('visits')
            if visits == None:
                visits = 0
        except:
            visits = 0
        visits = int(visits)
        visits += 1
        try:
            client.set('visits', visits)
        except:
            pass
        return {'visits': visits}

api.add_resource(Visits, "/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
