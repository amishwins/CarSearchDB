__author__ = 'Amish'

from bottle import route, run
from dbaccess import *
import json

@route('/cars')
def hello():
    da = DataAccess()
    cars = da.return_all_cars()
    return json.dumps(cars, sort_keys=True, indent=4)

run(host='localhost', port=8080, debug=True)
