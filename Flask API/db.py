# db.py
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user,
                                   password=db_password,
                                   unix_socket=unix_socket,
                                   db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        return e
    return conn


def get():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM Main Where Count > 2 ;')
        MainTable = cursor.fetchall()
        if result > 0:
            got_Main = jsonify(MainTable)
        else:
            got_Main = jsonify('No Disaster')
    conn.close()
    return got_Main


def update(Tweet, Lat, Long, City):
    conn = open_connection()
    # if City == 'Ahmedabad':
    #     with conn.cursor() as cursor:
    #         cursor.execute('INSERT INTO Ahmedabad (Tweet, Latitude, Longitude) VALUES(%s, %s, %s)',
    #                     (Tweet, float(Lat), float(Long)))
    #         conn.commit()
    #     with conn.cursor() as cursor:
    #         cursor.execute("Update Main SET Count= Count +1 WHERE city = 'Ahmedabad'")
    #         conn.commit()
    #
    # elif City == 'Rajkot':
    #     with conn.cursor() as cursor:
    #         cursor.execute('INSERT INTO Rajkot (Tweet, Latitude, Longitude) VALUES(%s, %s, %s)',
    #                        (Tweet, float(Lat), float(Long)))
    #         conn.commit()
    #     with conn.cursor() as cursor:
    #         cursor.execute("Update Main SET Count= Count +1 WHERE city = 'Rajkot'")
    #         conn.commit()
    #
    # elif City == 'Vadodara':
    #     with conn.cursor() as cursor:
    #         cursor.execute('INSERT INTO Vadodara (Tweet, Latitude, Longitude) VALUES(%s, %s, %s)',
    #                        (Tweet, float(Lat), float(Long)))
    #         conn.commit()
    #     with conn.cursor() as cursor:
    #         cursor.execute("Update Main SET Count= Count +1 WHERE city = 'Vadodara'")
    #         conn.commit()
    #
    # elif City == 'Surat':
    #     with conn.cursor() as cursor:
    #         cursor.execute('INSERT INTO Surat (Tweet, Latitude, Longitude) VALUES(%s, %s, %s)',
    #                        (Tweet, float(Lat), float(Long)))
    #         conn.commit()
    #     with conn.cursor() as cursor:
    #         cursor.execute("Update Main SET Count= Count +1 WHERE city = 'Surat'")
    #         conn.commit()
    #
    # elif City == 'Gandhinagar':
    #     with conn.cursor() as cursor:
    #         cursor.execute('INSERT INTO Gandhinagar (Tweet, Latitude, Longitude) VALUES(%s, %s, %s)',
    #                        (Tweet, float(Lat), float(Long)))
    #         conn.commit()
    #     with conn.cursor() as cursor:
    #         cursor.execute("Update Main SET Count= Count +1 WHERE city = 'Gandhinagar'")
    #         conn.commit()

    if City is not None:
        with conn.cursor() as cursor:
            query = "CREATE TABLE IF NOT EXISTS " + City + " (`Tweet` VARCHAR(250) NOT NULL,`Latitude` DOUBLE NOT NULL,`Longitude` DOUBLE NOT NULL, `Date` DATETIME NOT NULL);"
            cursor.execute(query)
            conn.commit()
        with conn.cursor() as cursor:
            AddMain = "INSERT INTO Main (City, Count) VALUES (%s, %s) ON DUPLICATE KEY UPDATE Count = Count + 1;"
            cursor.execute(AddMain, (City, int(1)))
            conn.commit()
        with conn.cursor() as cursor:
            CityTable = "INSERT INTO " + City + " (Tweet, Latitude, Longitude, Date) VALUES(%s, %s, %s,NOW());"
            cursor.execute(CityTable, (Tweet, float(Lat), float(Long)))
            conn.commit()
        # with conn.cursor() as cursor:
        #     MainT = "Update Main SET Count= Count +1 WHERE City = '" + City + "';"
        #     cursor.execute(MainT)
        #     conn.commit()
    conn.close()


def data(City):
    conn = open_connection()
    with conn.cursor() as cursor:
        query = "select ANY_VALUE(Tweet) as Tweet, ANY_VALUE(Latitude) as Latitude, ANY_VALUE(Longitude) as Longitude, ANY_VALUE(Date) as Date , Count(*) as Count from " + City + " Group BY Round(SQRT((Round(Latitude/0.001)*Round(Latitude/0.001))+(Round(Longitude/0.001)*Round(Longitude/0.001)))/10), DATE(Date) Having count(*) > 2;"
        result = cursor.execute(query)
        LatLong = cursor.fetchall()
        if result > 0:
            latlong = jsonify(LatLong)
        else:
            latlong = jsonify('No Data')
    conn.close()
    return latlong
