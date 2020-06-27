from project import db
from project.api.celebrities.models import Celebrity


def add_celebrity(name, pay, year, category):
    celebrity = db.session.add(
        Celebrity(name=name, pay=pay, year=year, category=category))
    db.session.commit()
    return celebrity


def get_celebrities(**args):
    celebrities = Celebrity.query.filter_by(**args).all()
    return celebrities


def get_celebrities_by_name(name):
    celebrites = Celebrity.query.filter_by(name=name).all()
    return celebrites


def get_celebrities_by_year(year):
    celebrities = Celebrity.query.filter_by(year=year).all()
    return celebrities


def get_celebrities_by_category(category):
    celebrities = Celebrity.query.filter_by(category=category).all()
    return celebrities