from app import db
import datetime

class IndividualDetails(db.Document):
    age = db.IntField()
    workclass = db.StringField()
    fnlwgt = db.IntField()
    education = db.StringField()
    education_number = db.IntField()
    marital_status = db.StringField()
    occupation = db.StringField()
    relationship = db.StringField()
    race = db.StringField()
    gender = db.StringField()
    capital_gain = db.IntField()
    capital_loss = db.IntField()
    work_hours = db.IntField()
    native_country = db.StringField()
    wage_class = db.StringField()