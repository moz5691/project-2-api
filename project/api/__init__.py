from flask_restx import Api

from project.api.ping import ping_namespace
from project.api.athletes.views import atheletes_namespace
from project.api.celebrities.views import celebrities_namespace

api = Api(version='1.0', title='Data project #2 API', doc='/doc/')

api.add_namespace(ping_namespace, path="/api/v1/ping")
api.add_namespace(atheletes_namespace, path="/api/v1/athletes")
api.add_namespace(celebrities_namespace, path="/api/v1/celebrities")