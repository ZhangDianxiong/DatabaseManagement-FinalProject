# This is the script to populate the tabel Arctic_See_Ice_Grow
# the data is from masie_4km_allyears_extent_sqkm.csv

import mysql.connector
from mysql.connector import Error
import csv
import pandas as pd
import calendar

# set up connection to the php server
connection = mysql.connector.connect(host='classmysql.engr.oregonstate.edu',
                                     user='cs440_group15',
                                     password="49hjP8ML4uQq",
                                     db="cs440_group15")
# build a cursor based on connection
cursor = connection.cursor()

# read in the csv file which is going to be used to populate the table


def readFile():

    with open("./masie_4km_allyears_extent_sqkm.csv") as csv_file:
        render = csv.reader(csv_file)
        next(render)
        next(render)
        counter = 0
        for rows in render:
            print("Loading row #{}/5139".format(counter))
            uploadToDB(rows)
            counter += 1
        print("finish loading data to the database")


def uploadToDB(rows):
    try:

        # conver the day of years to format of MM/DD/YYYY
        (month, day, year) = JulianDate_to_MMDDYY(
            int(rows[0][:5]), int(rows[0][5:]))
        # find the Dates id of a time
        idOfDates = select_Date(str(year), str(month), str(day))
        # if no dates found need insert this new dates
        if(idOfDates == -2):
            insert_Date(str(year), str(month), str(day))
            # acquire the dates id again agyer insert new date
            idOfDates = select_Date(str(year), str(month), str(day))

        query = """INSERT INTO `Arctic_See_Ice_Grow` (`dates_ID`, `Northern_Hemisphere`, `Beaufort_Sea`,
                                                    `Chukchi_Sea`, `East_Siberian_Sea`, `Laptev_Sea`,
                                                    `Kara_Sea`, `Barents_Sea`, `Greenland_Sea`, `Baffin_Bay_Gulf_of_St_Lawrence`,
                                                    `Canadian_Archipelago`, `Hudson_Bay`, `Central_Arctic`, `Bering_Sea`,
                                                    `Baltic_Sea`, `Sea_of_Okhotsk`, `Yellow_Sea`, `Cook_Inlet`) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        rows.pop(0)
        rows.insert(0, str(idOfDates))
        record = tuple(rows)
        # print(record)
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


def JulianDate_to_MMDDYY(year, julianDay):
    month = 1
    while julianDay - calendar.monthrange(year, month)[1] > 0 and month <= 12:
        julianDay = julianDay - calendar.monthrange(year, month)[1]
        month = month + 1
    return (month, julianDay, year)


if(connection.is_connected()):
    readFile()
    cursor.close()
    connection.close()
else:
    print("fail to connect to the mysql server")
