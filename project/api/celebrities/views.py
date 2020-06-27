from flask import Blueprint, request
from flask_restx import Resource, Api, fields, Namespace

from project.api.celebrities.crud import (add_celebrity, get_celebrities,
                                          get_celebrities_by_name,
                                          get_celebrities_by_year,
                                          get_celebrities_by_category)

celebrities_namespace = Namespace("celebrities")

### add validation here
celebrity = celebrities_namespace.model(
    'Celebrity', {
        'id': fields.Integer(readOnly=True),
        'name': fields.String(),
        'pay': fields.Float(),
        'year': fields.Integer(),
        'category': fields.String(),
        'created_date': fields.DateTime,
    })


class CelebritiesList(Resource):
    @celebrities_namespace.expect(celebrity, validate=True)
    @celebrities_namespace.response(201, "New entry was added!")
    def post(self):
        """Create a new celebrity"""
        post_data = request.get_json()
        name = post_data.get("name")
        pay = post.get("pay")
        year = post.get("year")
        category = post.get("category")
        response_object = {}

        ## TBD: add check to find duplicate atheletes.  if both name and year exists reject it.
        add_celebrity(name, pay, year, category)

        response_object = {'message': f'{name} was added!'}
        return response_object, 201

    @celebrities_namespace.marshal_with(celebrity, as_list=True)
    @celebrities_namespace.response(200, "Success")
    @celebrities_namespace.response(404, "No celebrities found")
    def get(self):
        """Return all celebrities, allows to add query ?name=<name>&year=<year>&category=<category>"""
        args = request.args
        celebrities = get_celebrities(**args)
        if not celebrities:
            celebrities_namespace.abort(
                404, f"Celebrities do not exist with query {args}")
        return celebrities, 200


class CelebritiesName(Resource):
    @celebrities_namespace.marshal_with(celebrity, as_list=True)
    @celebrities_namespace.response(200, "Success")
    @celebrities_namespace.response(404,
                                    "Celebrity with <name> does not exist")
    def get(self, name):
        """Return all by name"""
        celebrities = get_celebrities_by_name(name)
        if not celebrities:
            celebrities_namespace.abort(
                404, f"Celebrity with {name} does not exist")
        return celebrities, 200


class CelebritiesYear(Resource):
    @celebrities_namespace.marshal_with(celebrity, as_list=True)
    @celebrities_namespace.response(200, "Success")
    @celebrities_namespace.response(404,
                                    "Celebrities in year <year> do not exist")
    def get(self, year):
        """Return all by year"""
        celebrities = get_celebrities_by_year(year)
        if not celebrities:
            celebrities_namespace.abort(
                404, f"Celebrities in year {year} do not exist")
        return celebrities, 200


class CelebritiesCategory(Resource):
    @celebrities_namespace.marshal_with(celebrity, as_list=True)
    @celebrities_namespace.response(200, "Success")
    @celebrities_namespace.response(404,
                                    "Celebrities in <category> do not exist")
    def get(self, category):
        """Return all by category"""
        celebrities = get_celebrities_by_category(category)
        if not celebrities:
            celebrities_namespace.abort(
                404, f"Celebrities in {category} do not exist")
        return celebrities, 200


celebrities_namespace.add_resource(CelebritiesList, '')
celebrities_namespace.add_resource(CelebritiesName, '/name/<string:name>')
celebrities_namespace.add_resource(CelebritiesYear, '/year/<string:year>')
celebrities_namespace.add_resource(CelebritiesCategory,
                                   '/category/<string:category>')
