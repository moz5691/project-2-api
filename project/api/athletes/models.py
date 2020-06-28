from sqlalchemy.sql import func
from project import db


class Athlete(db.Model):
    """Athlete model. """

    __tablename__ = 'athletes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    nationality = db.Column(db.String(128), nullable=False)
    current_rank = db.Column(db.Integer, nullable=False)
    sport = db.Column(db.String(128), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    earnings = db.Column(db.Float, nullable=False)
    country_code = db.Column(db.String,
                             db.ForeignKey('geocodes.country_code'),
                             nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    geocode = db.relationship("Geocode", backref="athletes")

    def __init__(self, name, nationality, current_rank, sport, year, earnings,
                 country_code):
        self.name = name
        self.nationality = nationality
        self.current_rank = current_rank
        self.sport = sport
        self.year = year
        self.earnings = earnings
        self.country_code = country_code

    def __repr__(self):
        return f"{self.name}-{self.nationality}-{self.current_rank}-{self.sport}-{self.year}-{self.earnings}-{self.country_code}"


class Geocode(db.Model):
    __tablename__ = 'geocodes'
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_code = db.Column(db.String, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    country = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, country_code, latitude, longitude, country):
        self.country_code = country_code
        self.latitude = latitude
        self.longitude = longitude
        self.country = country

    def __repr__(self):
        return f"{self.country_code}-{self.country}-{self.latitude}-{self.longitude}"
