from sqlalchemy.sql import func

from project import db


class Celebrity(db.Model):
    __tablename__ = 'celebrities'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    pay = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, name, pay, year, category):
        self.name = name
        self.pay = pay
        self.year = year
        self.category = category


# Name,Pay (USD millions),Year,Category