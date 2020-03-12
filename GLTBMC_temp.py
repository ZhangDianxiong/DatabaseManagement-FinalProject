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

def insert_loc(country, city, lat, lon):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, %s, %s, %s, %s)"
        record = (country, city, lat, lon)
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

def handleDate(date):
    d = date.split("-")
    return d

def handleLat(lat):
    # print(lat)
    if(lat[-1] == "S"):
        return "-" + lat[0:len(lat)-1]
    else:
        return lat[0:len(lat)-1]

def handleLon(lon):
    if(lon[len(lon)-1] == "W"):
        return "-" + lon[0:len(lon)-1]
    else:
        return lon[0:len(lon)-1]

with open("../GlobalLandTemperaturesByMajorCity.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in readCSV:
        if (row[0] == "dt"):
            continue

        date = handleDate(row[0])
        lat = handleLat(row[5])
        lon = handleLon(row[6])

        d_id = find_date(date[0], date[1], date[2])
        l_id = find_loc(lat, lon)

        if (d_id==-1):
            insert_date(date[0], date[1], date[2])
            d_id = find_date(date[0], date[1], date[2])

        if (l_id ==-1):
            insert_loc(row[3], row[4], lat, lon)
            l_id = find_loc(lat, lon)

        insert_temp(d_id, l_id, row[1])

        count = count + 1

if (connection.is_connected()):
    cursor.close()
    connection.close()
