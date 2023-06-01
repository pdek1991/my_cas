import datetime
import configparser
import mysql.connector.pooling
import time
import socket

config = configparser.ConfigParser()
config.read(r'stage_cycle.ini')

db_config = {
    "host": "192.168.56.112",
    "user": "omi_user",
    "password": "omi_user",
    "database": "cas",
}

connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="my_pool", pool_size=10, **db_config)

# Create a cursor to interact with the database

connection = connection_pool.get_connection()
cursor = connection.cursor()
cursor.execute("SELECT endtime, emmdata, emmtype FROM emmg limit 100")
rows = cursor.fetchall()
cursor.close()
connection.close()

cycle_osm = int(config.get(str(44), 'cycle'))
stage_osm = int(config.get(str(44), 'stage'))
cycle_adddevice = int(config.get(str(10), 'cycle'))
stage_adddevice = int(config.get(str(10), 'stage'))
cycle_entitlement = int(config.get(str(21), 'cycle'))
stage_entitlement = int(config.get(str(21), 'stage'))

# Iterate over each row
for row in rows:
    endtime, emmdata, emmtype = row
    # Check if current time (in epoch) is less than end time for the emmtype
    if int(time.time()) < endtime:
        if str(emmtype) == '21':
            print('entitlement')
        else:
            print('other')




time.sleep(cycle_entitlement)