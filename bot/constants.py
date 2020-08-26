from enum import Enum


BASE_ENDPOINT='https://api.binance.com/'
CONTENT_TYPE='application/x-www-form-urlencoded'

class interval_letter(Enum):
    SECOND = 'S'
    MINUTE = 'M'
    HOUR = 'H'
    DAY = 'D'
