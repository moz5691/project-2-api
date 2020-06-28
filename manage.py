import sys
import os
import csv
from flask.cli import FlaskGroup
from project import create_app, db
from project.api.athletes.models import Athlete, Geocode
from project.api.celebrities.models import Celebrity

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_DATA = os.path.join(APP_ROOT, 'data')
app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db1')
def seed_db1():
    with open(os.path.join(APP_DATA, 'geodata.csv')) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['country_code'], row['latitude'], row['longitude'],
                  row['country'])
            record = Geocode(country_code=row['country_code'],
                             latitude=row['latitude'],
                             longitude=row['longitude'],
                             country=row['country'])
            db.session.add(record)

    db.session.commit()


@cli.command('seed_db2')
def seed_db2():
    with open(os.path.join(APP_DATA, 'athletes.csv')) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Name'], row['Nationality'], row['Current Rank'],
                  row['Sport'], row['Year'], row['earnings ($ million)'],
                  row['Country Code'])
            record = Athlete(name=row['Name'],
                             nationality=row['Nationality'],
                             current_rank=row['Current Rank'],
                             sport=row['Sport'],
                             year=row['Year'],
                             earnings=row['earnings ($ million)'],
                             country_code=row['Country Code'])
            db.session.add(record)

    db.session.commit()


@cli.command('seed_db3')
def seed_db3():
    with open(os.path.join(APP_DATA, 'celebrities.csv')) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Name'], row['Pay (USD millions)'], row['Year'],
                  row['Category'])
            record = Celebrity(name=row['Name'],
                               pay=row['Pay (USD millions)'],
                               year=row['Year'],
                               category=row['Category'])
            db.session.add(record)

    db.session.commit()


#country_code,latitude,longitude,country,usa_state_code,usa_state_latitude,usa_state_longitude,usa_state

if __name__ == '__main__':
    cli()