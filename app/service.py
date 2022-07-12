import json
import datetime
from datetime_encoder import DateEncoder

from repository import retrive_users, create_volunteer_db, retrive_one_user


def get_current_date():
    ''''Gets current date and prints in json'''

    date = {
        "day_of_week": datetime.datetime.today().weekday(),
        "day_of_month": str(datetime.datetime.today().day),
        "month": str(datetime.datetime.today().month),
        "year": str(datetime.datetime.today().year),
        "timestamp": str(datetime.datetime.today().time()),
    }

    return json.dumps(date)


def create_volunteer(name, surname, city, country):
    '''creates volunteer'''
    row_id = create_volunteer_db(name, surname, city, country)
    response = json.dumps(retrive_one_user(row_id), cls=DateEncoder)
    return response


def get_all_volunteers():
    '''retrive all volunteers from db'''

    all_users = json.dumps(retrive_users(), cls=DateEncoder)
    return all_users


def get_one_volunteer_by_id(user_id):
    '''gets one volunteer by id'''
    response = json.dumps(retrive_one_user(user_id)[0], cls=DateEncoder)
    return response
