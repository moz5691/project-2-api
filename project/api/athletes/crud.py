from project import db
from project.api.athletes.models import Athlete, Geocode
from sqlalchemy.orm import joinedload
# import pprint as pp


def add_athlete(name, nationality, current_rank, sport, year, earnings,
                country_code):
    athlete = db.session.add(
        Athlete(name=name,
                nationality=nationality,
                current_rank=current_rank,
                sport=sport,
                year=year,
                earnings=earnings,
                country_code=country_code))
    db.session.commit()
    return athlete


def get_athletes(**args):
    athletes = db.session.query(Athlete, Geocode).filter_by(**args).join(
        Geocode, Athlete.country_code == Geocode.country_code).all()

    recordsList = combine_geocode(athletes)
    return recordsList


def get_athletes_by_name(name):
    athletes = db.session.query(
        Athlete, Geocode).filter(Athlete.name == name).join(
            Geocode, Athlete.country_code == Geocode.country_code).all()

    recordsList = combine_geocode(athletes)

    return recordsList


def get_athletes_by_nationality(nationality):
    athletes = db.session.query(
        Athlete, Geocode).filter(Athlete.nationality == nationality).join(
            Geocode, Athlete.country_code == Geocode.country_code).all()

    recordsList = combine_geocode(athletes)
    return recordsList


def get_athletes_by_sport(sport):
    athletes = db.session.query(
        Athlete, Geocode).filter(Athlete.sport == sport).join(
            Geocode, Athlete.country_code == Geocode.country_code).all()

    recordsList = combine_geocode(athletes)
    return recordsList


def get_athletes_by_year(year):
    athletes = db.session.query(
        Athlete, Geocode).filter(Athlete.year == year).join(
            Geocode, Athlete.country_code == Geocode.country_code).all()

    recordsList = combine_geocode(athletes)
    return recordsList


# Refer query schema.
#https://hackersandslackers.com/database-queries-sqlalchemy-orm/
def combine_geocode(records):
    recordsList = list()
    for record in records:
        recordObj = dict()
        recordObj['id'] = record[0].__dict__['id']
        recordObj['name'] = record[0].__dict__['name']
        recordObj['nationality'] = record[0].__dict__['nationality']
        recordObj['current_rank'] = record[0].__dict__['current_rank']
        recordObj['sport'] = record[0].__dict__['sport']
        recordObj['year'] = record[0].__dict__['year']
        recordObj['earnings'] = record[0].__dict__['earnings']
        recordObj['latitude'] = record[1].__dict__['latitude']
        recordObj['longitude'] = record[1].__dict__['longitude']
        recordObj['created_date'] = record[0].__dict__['created_date']
        recordsList.append(recordObj)

    return recordsList