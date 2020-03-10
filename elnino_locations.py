import mysql.connector
from mysql.connector import Error
import csv

connection = mysql.connector.connect(host='classmysql.engr.oregonstate.edu',
                                database='cs440_kirchchr',
                                user ='cs440_kirchchr',
                                password='5540')
cursor = connection.cursor()

class Loc:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

def insert(lat, lon):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, %s, %s)"
        record = (lat, lon)
        cursor.execute(query, record)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

def unique(lat, lon, locs):
    count = 0
    if (len(locs) == 0):
        locs.append(Loc(lat, lon))
    for x in locs:
        if (lat == x.lat or lon == x.lon):
            count = 1
            break
    if (count == 0):
        insert(lat, lon)
        locs.append(Loc(lat, lon))

with open("../elnino.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    lats = []
    lons = []
    locs = []
    count = 0
    for row in readCSV:
        if (row[0] == "Observation"):
            continue
        unique(row[5], row[6], locs)
        count = count + 1
        if (count == 1000):
            print(1000)
            print("length: ", len(locs))
        elif ( count == 10000):
            print(10000)
            print("length: ", len(locs))
        elif ( count == 100000):
            print(100000)
            print("length: ", len(locs))
    print("total tuples: ", len(locs))


if (connection.is_connected()):
    cursor.close()
    connection.close()
