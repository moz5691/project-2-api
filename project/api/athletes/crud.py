from project import db
from project.api.athletes.models import Athlete


def add_athlete(name, nationality, current_rank, sport, year, earnings):
    athlete = db.session.add(
        Athlete(name=name,
                nationality=nationality,
                current_rank=current_rank,
                sport=sport,
                year=year,
                earnings=earnings))
    db.session.commit()
    return athlete


def get_athletes(**args):
    athletes = Athlete.query.filter_by(**args).all()
    return athletes


def get_athletes_by_name(name):
    athletes = Athlete.query.filter_by(name=name).all()
    return athletes


def get_athletes_by_nationality(nationality):
    athletes = Athlete.query.filter_by(nationality=nationality).all()
    return athletes


def get_athletes_by_sport(sport):
    athletes = Athlete.query.filter_by(sport=sport).all()
    return athletes


def get_athletes_by_year(year):
    athletes = Athlete.query.filter_by(year=year).all()
    return athletes