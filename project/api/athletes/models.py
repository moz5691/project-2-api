from sqlalchemy.sql import func

from project import db


class Athlete(db.Model):
    __tablename__ = 'athletes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    nationality = db.Column(db.String(128), nullable=False)
    current_rank = db.Column(db.Integer, nullable=False)
    sport = db.Column(db.String(128), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    earnings = db.Column(db.Float, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, name, nationality, current_rank, sport, year, earnings):
        self.name = name
        self.nationality = nationality
        self.current_rank = current_rank
        self.sport = sport
        self.year = year
        self.earnings = earnings
