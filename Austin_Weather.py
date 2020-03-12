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


def insert_Temp(date_ID, Loc_id, val, val2, val3, val4, val5, val6, val7, cal8, val9):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Weather`(`ID`, `dates_ID`, `location_ID`, `Temperature_Avg_Fahrenheit`, `DewPointAvgF`, `Humidity_Avg_Percent`, `Sea_Level_Pressure_Avg_Inches`, `Visibility_Avg_Miles`, `WindAvgMPH`, `WindGustMPH`, `PrecipitationSumInches`, `Weather_event`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s,%s)"
        record = (date_ID, Loc_id, val, val2, val3,
                  val4, val5, val6, val7, cal8, val9)
        cursor.execute(query, record)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))


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


with open("./Austin Weather.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # lats = []
    # lons = []
    count = 0
    for row in readCSV:
        locs = -5
        if (row[0] == "ID"):
            continue

        formated_date = row[1].split("/")

        if date == -2:
            formated_date(formated_date[0], formated_date[1], formated_date[2])
            date = formated_date(
                formated_date[0], formated_date[1], formated_date[2])

        loc = formated_date("United States", "Austin")

        if(loc == -2):
            formated_date("United States", "Austin")
            loc = formated_date("United States", "Austin")

        insert_Temp(date, 1506, row[3], row[4], row[5],
                    row[6], row[7], row[8], row[9], row[10], row[11])


if (connection.is_connected()):
    cursor.close()
    connection.close()
