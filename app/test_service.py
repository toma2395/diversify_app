import re
from service import get_current_date, create_volunteer, get_one_volunteer_by_id, get_all_volunteers
import json
import datetime


def test_get_current_date_is_output_str():
    '''Tests if output is in str format'''

    # When
    mock = get_current_date()
    # Then
    assert isinstance(mock, str)


def test_get_current_date_has_day_of_week():
    '''Tests day_of_week param'''

    # When
    mock = json.loads(get_current_date())
    day_of_week = mock['day_of_week']
    # Then
    assert 'day_of_week' in mock
    assert isinstance(day_of_week, int)


def test_get_current_date_has_readable_time_format():
    '''test time fromat of the reponse'''
    # Given
    time_format = '%H:%M:%S.%f'
    # when
    mock = json.loads(get_current_date())
    # Then
    assert bool(datetime.datetime.strptime(mock['timestamp'], time_format))


def test_create_volunteer_checking_types():
    '''testing creating volunteer'''
    # Given
    name='Kazimierz'
    surname='Ziobro'
    city='Wroclaw'
    country='Poland'

    # When
    response=json.loads(create_volunteer(name, surname, city, country))
    #Then
    assert isinstance(response['v_id'], int)
    assert isinstance(response['v_name'], str)
    assert isinstance(response['v_surname'], str)
    assert isinstance(response['v_city'], str)
    assert isinstance(response['v_country'], str)
    assert isinstance(response['v_creation_date'], str)


def test_get_volunteer_is_dict():
    '''testing get volunteer'''
    # Given
    user_id=1
    # When
    response=json.loads(get_one_volunteer_by_id(user_id))
    # Then
    assert isinstance(response, dict)
    assert response['v_name'] == 'Adriano'
    assert response['v_surname'] == 'Italiano'

def test_get_all_volunteers_is_list():
    '''testing get volunteers'''
    # Given
    n=0
   # When
    json_response=get_all_volunteers()
    response=json.loads(json_response)
    for i in response:
        n=n+1
    # Then
    assert isinstance(response, list)
    assert isinstance(json_response, str)
    assert n >= 1
