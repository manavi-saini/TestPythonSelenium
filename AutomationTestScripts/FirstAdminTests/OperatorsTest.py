import random
import calendar
from datetime import datetime
import psycopg2
from Utils.BaseClass import BaseClass
from Utils import Utility as util


class TestOperators(BaseClass):

    def test_verify(self):
        func_name = util.func_name()
        log = self.getLogger(func_name)
        month = self.get_month('11')
        print(month)
        date = datetime.today().strftime('%m/%d/%Y')
        print(date)
        count = self.auto_inc()
        print("COUNT: "+str(count))
        log.info("Hello Test message")

    def get_month(self, date):
        if date.startswith('0'):
            date = date.replace('0', '')

        return calendar.month_name[int(date)]

    def auto_inc(self):
        global connection, cursor, counter
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Misha254@@",
                                          host="localhost",
                                          port="5432",
                                          database="RetrofitDB")
            cursor = connection.cursor()
            select_query = "select max(id) from counter_id"

            cursor.execute(select_query)
            id_records = cursor.fetchall()

            for x in id_records:
                print("ID: " + str(x[0]))
                counter = x[0] + 1

            insert_query = "insert into counter_id (id) values (%s)"
            cursor.execute(insert_query, (counter,))

            connection.commit()

            return counter

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # Closing Database Connection
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

