from flask import Blueprint, request
from flask_restx import Resource, Api, fields, Namespace

from project.api.athletes.crud import (add_athlete, get_athletes,
                                       get_athletes_by_name,
                                       get_athletes_by_nationality,
                                       get_athletes_by_sport,
                                       get_athletes_by_year)

# athletes_blueprint = Blueprint('athletes', __name__)
# api = Api(athletes_blueprint)
atheletes_namespace = Namespace("atheletes")

### add validation here
athlete = atheletes_namespace.model(
    'Athelete', {
        'id': fields.Integer(readOnly=True),
        'name': fields.String(),
        'nationality': fields.String(),
        'current_rank': fields.Integer(),
        'sport': fields.String(),
        'year': fields.Integer(),
        'earnings': fields.Float(),
        'created_date': fields.DateTime,
    })


class AthletesList(Resource):
    @atheletes_namespace.expect(athlete, validate=True)
    @atheletes_namespace.response(201, "New entry was added!")
    def post(self):
        """Create a new athlete"""
        post_data = request.get_json()
        name = post_data.get("name")
        nationality = post.get("nationality")
        current_rank = post.get("current_rank")
        sport = post.get("sport")
        year = post.get("year")
        earnings = post.get("earnings")
        response_object = {}

        ## TBD: add check to find duplicate atheletes.  if both name and year exists reject it.
        add_athlete(name, nationality, current_rank, sport, year, earnings)

        response_object = {'message': f'{name} was added!'}
        return response_object, 201

    @atheletes_namespace.marshal_with(athlete, as_list=True)
    @atheletes_namespace.response(200, "Success")
    @atheletes_namespace.response(404, "No atheletes found")
    def get(self):
        """Return all athletes without query, allows to add query ?name=<name>&nationality=<nationality>&sport=<sport>&year=<year>"""
        args = request.args
        athletes = get_athletes(**args)
        if not athletes:
            atheletes_namespace.abort(
                404, f"Athletes do not exist with query {args}")
        return athletes, 200


class AthletesName(Resource):
    @atheletes_namespace.marshal_with(athlete, as_list=True)
    @atheletes_namespace.response(200, "Success")
    @atheletes_namespace.response(404, "Athlete with <name> does not exist")
    def get(self, name):
        """Return all by name"""
        athletes = get_athletes_by_name(name)
        if not athletes:
            atheletes_namespace.abort(404,
                                      f"Athlete with {name} does not exist")
        return athletes, 200


class AthletesNationality(Resource):
    @atheletes_namespace.marshal_with(athlete, as_list=True)
    @atheletes_namespace.response(200, "Success")
    @atheletes_namespace.response(404,
                                  "Athletes from <nationality> does not exist")
    def get(self, nationality):
        """Return all by nationality"""
        athletes = get_athletes_by_nationality(nationality)
        if not athletes:
            atheletes_namespace.abort(
                404, f"Athletes from {nationality} do not exist")
        return athletes, 200


class AthletesSport(Resource):
    @atheletes_namespace.marshal_with(athlete, as_list=True)
    @atheletes_namespace.response(200, "Success")
    @atheletes_namespace.response(404, "Athletes in <sport> do not exist")
    def get(self, sport):
        """Return all by sport"""
        athletes = get_athletes_by_sport(sport)
        if not athletes:
            atheletes_namespace.abort(404, f"Athletes in {sport} do not exist")
        return athletes, 200


class AthletesYear(Resource):
    @atheletes_namespace.marshal_with(athlete, as_list=True)
    @atheletes_namespace.response(200, "Success")
    @atheletes_namespace.response(404, "Athlete in year <year> do not exist")
    def get(self, year):
        """Return all by year"""
        athletes = get_athletes_by_year(year)
        if not athletes:
            atheletes_namespace.abort(404,
                                      f"Athletes in year {year} do not exist")
        return athletes, 200


atheletes_namespace.add_resource(AthletesList, '')
atheletes_namespace.add_resource(AthletesName, '/name/<string:name>')
atheletes_namespace.add_resource(AthletesNationality,
                                 '/nationality/<string:nationality>')
atheletes_namespace.add_resource(AthletesSport, '/sport/<string:sport>')
atheletes_namespace.add_resource(AthletesYear, '/year/<string:year>')
