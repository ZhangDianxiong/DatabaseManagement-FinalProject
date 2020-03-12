import mysql.connector
from mysql.connector import Error
import csv

connection = mysql.connector.connect(host='classmysql.engr.oregonstate.edu',
                                database='cs440_group15',
                                user ='cs440_group15',
                                password='49hjP8ML4uQq')

# connection = mysql.connector.connect(host='classmysql.engr.oregonstate.edu',
#                                 database='cs440_kirchchr',
#                                 user ='cs440_kirchchr',
#                                 password='5540')

cursor = connection.cursor()

def insert_temp(dId, lId, min_t, max_t):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Temperature` (`dates_ID`, `location_ID`, `Minimum_Temperature`, `Average_Temperature`, `Maxmum_Temperature`) VALUES (%s, %s, %s, NULL, %s)"
        record = (dId, lId, min_t, max_t)
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

def insert_loc(country, city):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, %s, %s, NULL, NULL)"
        record = (country, city)
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

def find_loc(country, city):
    try:
        query = "SELECT `ID` FROM `Location` WHERE `Country` = %s AND `City` = %s"
        cursor.execute(query, (country, city))
        id = cursor.fetchall()
        if (cursor.rowcount == 0):
            return -1

        for row in id:
            return row[0]

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

def handleDate(date):
    d = date.split("-")
    return d


with open("../weatherAUS.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in readCSV:
        if (row[0] == "Date"):
            continue

        date = handleDate(row[0])

        d_id = find_date(date[0], date[1], date[2])
        l_id = find_loc("Australia", row[1])

        if (d_id==-1):
            insert_date(date[0], date[1], date[2])
            d_id = find_date(date[0], date[1], date[2])

        if (l_id ==-1):
            insert_loc("Australia", row[1])
            l_id = find_loc("Australia", row[1])

        insert_temp(d_id, l_id, row[2], row[3])

        count = count + 1

if (connection.is_connected()):
    cursor.close()
    connection.close()
