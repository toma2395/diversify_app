from typing_extensions import assert_type
from service import get_current_date
import typing_extensions
import json
import datetime

def test_get_current_date_is_output_str():
    '''Tests if output is in str format'''

    #When
    mock=get_current_date()
    #Then
    assert isinstance(mock, str)


def test_get_current_date_has_day_of_week():
    '''Tests day_of_week param'''

    #When
    mock=json.loads(get_current_date())
    day_of_week=mock['day_of_week']
    #Then
    assert 'day_of_week' in mock
    assert isinstance(day_of_week, int)


def test_get_current_date_has_readable_time_format():
    '''test time fromat of the reponse'''
    #Given
    time_format='%H:%M:%S.%f'
    #when
    mock=json.loads(get_current_date())
    #Then
    assert bool(datetime.datetime.strptime(mock['timestamp'], time_format))
