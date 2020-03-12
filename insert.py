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


def insert_Temp(date_ID, Loc_id, val, val2):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        # query = "INSERT INTO `Heat_Wave`(`ID`, `dates_ID`, `location_ID`, `Heat_Wave_Index`) VALUES (NULL, (SELECT `ID` FROM `Dates` WHERE `ID` = %s LIMIT 1),1233, %s)"
        # query = "INSERT INTO `CO2_Emission`(`ID`, `dates_ID`, `Average_Emmision`, `Interpolated`, `Trend`) VALUES (NULL, (SELECT `ID` FROM `Dates` WHERE `ID` = %s LIMIT 1), %s, %s, %s)"
        # query = "INSERT INTO `Green_House_Gas`(`ID`, `dates_ID`, `location_ID`, `Emission_value`) VALUES (NULL, %s, %s, %s)"
        # query = "INSERT INTO `Air_Pollution_Death_Rate`(`ID`, `dates_ID`, `location_ID`, `Deaths`) VALUES (NULL, %s, %s, %s)"
        query = "INSERT INTO `Earthquake`(`ID`, `dates_ID`, `location_ID`, `Depth`, `Magnitude`) VALUES (NULL, %s, %s, %s, %s)"

        record = (date_ID, Loc_id, val, val2)
        print(record)
        cursor.execute(query, record)
        connection.commit()
        print("Insert Success temp")
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


def insert_Location(year, x):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        print(year)
        query = "INSERT INTO `Location`(`ID`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, %s, %s)"
        record = (year, x, )
        cursor.execute(query, record)
        connection.commit()
        print("Successfully insert Location")
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


def select_Location(station, y):
    try:
        query = "SELECT `ID` FROM `Location` WHERE `Latitude` = %s AND `Longitude` = %s"
        # record = (city)
        cursor.execute(query, (station, y, ))
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            return -2
        else:
            for row in records:
                return row[0]
                break

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))


with open("./database.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        date = -5
        loc = -5

        if (row[0] == "Date"):
            continue

        print(row[0])

        data = row[0].split("/")

        date = select_Date(data[2], data[1], data[0])

        if date == -2:
            insert_Date(data[2], data[1], data[0])
            date = select_Date(data[2], data[1], data[0])

        loc = select_Location(row[2], row[3])

        if(loc == -2):
            insert_Location(row[2], row[3])
            loc = select_Location(row[2], row[3])

        insert_Temp(date, loc, row[5], row[8])


if (connection.is_connected()):
    cursor.close()
    connection.close()
