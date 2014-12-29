__author__ = 'Amish'

import mysql.connector
import unittest

class DataAccess:
    def __init__(self):
        self.config = {
          'user': 'dev',
          'password': 'willalexseethis',
          'host': 'localhost',
          'database': 'cars',
          'raise_on_warnings': True,
        }

    def get_car_record(self, manufacturer, make, year, model):
        cnx = mysql.connector.connect(**self.config)
        cursor = cnx.cursor()

        query = ("SELECT * FROM car "
                 "WHERE manufacturer = %s AND "
                 "make = %s AND "
                 "year = %s AND "
                 "model = %s")

        cursor.execute(query, (manufacturer, make, year, model))

        if cursor.rowcount > 1:
            cursor.close()
            cnx.close()
            raise Exception("Something bad happened")

        else:
            result = cursor.fetchone()

        cursor.close()
        cnx.close()

        return result


    def insert_car(self, manufacturer, make, year, model):
        cnx = mysql.connector.connect(**self.config)
        cursor = cnx.cursor()

        car_record = self.get_car_record(manufacturer, make, year, model)
        if car_record == None:

            add_search_result = ("INSERT IGNORE INTO car "
                                 "(manufacturer, make, year, model) "
                                 "VALUES (%s, %s, %s, %s)")

            cursor.execute(add_search_result, (manufacturer, make, year, model))
            record_id = cursor.lastrowid
        else:
            record_id = car_record[0]


        cnx.commit()
        cursor.close()
        cnx.close()

        return record_id

    def insert_option(self, car_id, option_description):
        cnx = mysql.connector.connect(**self.config)
        cursor = cnx.cursor()

        add_search_result = ("INSERT INTO carOption "
                             "(carID, optionDescription) "
                             "VALUES (%s, %s)")

        cursor.execute(add_search_result, (car_id, option_description))

        cnx.commit()
        cursor.close()
        cnx.close()

    def insert_search_result(self, car_id, dealership, interest_rate, monthly, number_of_months, notes):
        cnx = mysql.connector.connect(**self.config)
        cursor = cnx.cursor()

        add_search_result = ("INSERT INTO searchResult "
                             "(carID, dealership, interestRate, monthly, numberOfMonths, notes) "
                             "VALUES (%s, %s, %s, %s, %s, %s)")

        cursor.execute(add_search_result, (car_id, dealership, interest_rate, monthly, number_of_months, notes))

        cnx.commit()
        cursor.close()
        cnx.close()

    def return_all_cars(self):
        cnx = mysql.connector.connect(**self.config)
        cursor = cnx.cursor()

        query = ("SELECT * FROM car")

        cursor.execute(query)

        results = list()
        result = dict()

        for (carID, manufacturer, make, year, model) in cursor:
            result = dict()
            result['carID'] = carID
            result['manufacturer'] = manufacturer
            result['make'] = make
            result['year'] = year
            result['model'] = model
            results.append(result)

        cursor.close()
        cnx.close()

        return results

class DataAccessTest(unittest.TestCase):
    def setUp(self):
        self.cut = DataAccess()

    def test_get_car_id_is_none(self):
        car_record = self.cut.get_car_record('x', 'x', 1, 'x')
        self.assertIsNone(car_record)

    def test_get_car_id_is_something(self):
        car_id = self.cut.insert_car('VW', 'Jetta', 2015, 'Sportline')
        car_record = self.cut.get_car_record('VW', 'Jetta', 2015, 'Sportline')
        self.assertEqual(car_id, car_record[0])

    def test_add_new_record(self):
        car_id = self.cut.insert_car('VW', 'Jetta', 2014, 'Sportline')
        self.cut.insert_option(car_id, 'Spoiler')
        self.cut.insert_search_result(car_id, 'Centre-Ville', 2.99, 350.99, 48, 'I liked this car alot')


