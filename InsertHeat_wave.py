import mysql.connector
from mysql.connector import Error
import csv

connection = mysql.connector.connect(host='classmysql.engr.oregonstate.edu',
                                     database='cs440_group15',
                                     user='cs440_group15',
                                     password='49hjP8ML4uQq')
cursor = connection.cursor()


class Loc:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


def insert_Temp(date_ID, val):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Heat_Wave`(`ID`, `dates_ID`, `location_ID`, `Heat_Wave_Index`) VALUES (NULL, (SELECT `ID` FROM `Dates` WHERE `ID` = %s LIMIT 1),1233, %s)"
        record = (date_ID, val)
        cursor.execute(query, record)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table insert_Temp {}".format(error))


def insert_Date(year, month, day):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Dates`(`ID`, `Years`, `Months`, `Days`) VALUES (NULL, %s, %s, %s)"
        record = (year, month, day)
        cursor.execute(query, record)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))


def select_Date(year, month, day):
    try:
        query = "SELECT `ID` FROM `Dates` WHERE `Years` = %s AND `Months` = %s AND `Days` = %s"
        # record = (city)
        cursor.execute(query, (year, month, day,))
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            return -2
        else:
            for row in records:
                # print("Id = ", row[0], )
                return row[0]
                break

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))


with open("./heatWave.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    count = 0

    for row in readCSV:
        date = -5
        if (row[0] == "Entity"):
            continue

        date = select_Date(row[2], 1, 1)

        if date == -2:
            insert_Date(row[2], 1, 1)

        print(row[3])

        insert_Temp(date, row[3])


if (connection.is_connected()):
    cursor.close()
    connection.close()
