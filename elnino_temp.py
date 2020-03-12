import mysql.connector
from mysql.connector import Error
import csv

connection = mysql.connector.connect(host='classmysql.engr.oregonstate.edu',
                                database='cs440_group15',
                                user ='cs440_group15',
                                password='49hjP8ML4uQq')
cursor = connection.cursor()

def insert_temp(dId, lId, AvT):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Temperature` (`dates_ID`, `location_ID`, `Minimum_Temperature`, `Average_Temperature`, `Maxmum_Temperature`) VALUES (%s, %s, NULL, %s, NULL)"
        record = (dId, lId, AvT)
        cursor.execute(query, record)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

def insert_date(year, month, day):
    # print("inserting date")
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Dates` (`ID`, `Years`, `Months`, `Days`) VALUES (NULL, %s, %s, %s)"
        record = (year, month, day)
        cursor.execute(query, record)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

def insert_loc(lat, lon):
    # print("inserting Loc")
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, %s, %s)"
        record = (lat, lon)
        cursor.execute(query, record)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

def find_date(year, month, day):
    try:
        query = "SELECT `ID` FROM `Dates` WHERE `Years` = %s AND `Months` = %s AND `Days` = %s"
        cursor.execute(query, (year, month, day))
        id = cursor.fetchall()
        if (cursor.rowcount == 0):
            return -1

        for row in id:
            return row[0]

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

def find_loc(lat, lon):
    try:
        query = "SELECT `ID` FROM `Location` WHERE `Latitude` = %s AND `Longitude` = %s"
        cursor.execute(query, (float(lat), float(lon)))
        id = cursor.fetchall()
        if (cursor.rowcount == 0):
            return -1

        for row in id:
            return row[0]

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

with open("../elnino.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in readCSV:
        if (row[0] == "Observation"):
            continue
        d_id = find_date("19"+row[1], row[2], row[3])
        l_id = find_loc(row[5], row[6])

        if (d_id==-1):
            insert_date("19"+row[1], row[2], row[3])
            d_id = find_date("19"+row[1], row[2], row[3])

        if (l_id ==-1):
            insert_loc(row[5], row[6])
            l_id = find_loc(row[5], row[6])

        insert_temp(d_id, l_id, row[10])

        count = count + 1

if (connection.is_connected()):
    cursor.close()
    connection.close()
