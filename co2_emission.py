import mysql.connector
from mysql.connector import Error
import csv
import calendar
connection = mysql.connector.connect(host='classmysql.engr.oregonstate.edu',
                                     database='',
                                     user='',
                                     password='')
cursor = connection.cursor()


def readFile():

    with open("./co2-mm-mlo_csv - co2-mm-mlo_csv.csv") as csvFile:
        render = csv.reader(csvFile)
        next(render)
        counter = 0
        for rows in render:
            print("Loading row #{}/728".format(counter))
            insertIntoTable(rows)
            counter += 1
        print("finish loading data to the database")


def getDatesID(date):
    dates = date.split('-')
    datesID = select_Date(dates[0], dates[1], dates[2])
    if(datesID == -2):
        insert_Date(dates[0], dates[1], dates[2])
        datesID = select_Date(dates[0], dates[1], dates[2])
    return datesID


def insertIntoTable(row):
    try:
        query = """INSERT INTO `Global_CO2_Emission` 
                (`ID`, `dates_ID`, `Average_Emmision`, `Interpolated`, `Trend`) 
                VALUES (NULL, %s, %s, %s, %s)"""
        datesID = getDatesID(row[0])
        row.pop(0)
        row.pop(0)
        row.pop(-1)
        row.insert(0, str(datesID))
        record = tuple(row)
        cursor.execute(query, record)
        connection.commit()
    except mysql.connector.Error as error:
        print("Insertion error: {}".format(error))


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

    except mysql.connector.Error as error:
        print("{}".format(error))


def insert_Date(year, month, day):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Dates`(`ID`, `Years`, `Months`, `Days`) VALUES (NULL, %s, %s, %s)"
        record = (year, month, day)
        cursor.execute(query, record)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))


if (connection.is_connected()):
    readFile()
    cursor.close()
    connection.close()
else:
    print("fail to connect to the mysql server")
