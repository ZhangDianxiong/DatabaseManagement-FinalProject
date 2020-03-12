import mysql.connector
from mysql.connector import Error
import csv

# connection = mysql.connector.connect(host='classmysql.engr.oregonstate.edu',
#                                 database='cs440_bairdd',
#                                 user ='cs440_bairdd',
#                                 password='Miku5510')
connection = mysql.connector.connect(host='classmysql.engr.oregonstate.edu',
                                database='cs440_group15',
                                user ='cs440_group15',
                                password='49hjP8ML4uQq')
cursor = connection.cursor()

class Loc:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

def insert_Location(country, city, lat, lon):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Location`(`ID`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, %s, %s, %s, %s)"
        record = (country, city, lat, lon)
        cursor.execute(query, record)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))


def select_Location(country, city, lat, lon):
    try:
        query = "SELECT `ID` FROM `Location` WHERE `Country` = %s AND `City` = %s AND `City` = %s AND `City` = %s"
        # record = (city)
        cursor.execute(query, (country, city, lat, lon))
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            return -1
        else:
            for row in records:
                print("Id = ", row[0], )
                return row[0]
                break
        
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))


with open("./city_attributes.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # lats = []
    # lons = []
    count = 0
    for row in readCSV:
        locs = -5
        if (row[0] == "City"):
            continue
        locs = select_Location(row[1],row[0],row[2],row[3])
        print(locs)
        # print(float(row[6]))
        # print(type(float(row[6])))
        # print(type(row[7]))
        # break
        if locs == -1:
            insert_Location(row[1],row[0],row[2],row[3])


if (connection.is_connected()):
    cursor.close()
    connection.close()
