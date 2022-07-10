import json
import datetime


def get_current_date():
    ''''Gets current date and prints in json'''

    date = {
        "day_of_week": datetime.datetime.today().weekday(),
        "day_of_month": str(datetime.datetime.today().day),
        "month": str(datetime.datetime.today().month),
        "year": str(datetime.datetime.today().year),
        "timestamp": str(datetime.datetime.today().timestamp()),
    }

    return json.dumps(date)
