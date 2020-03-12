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

def insert_Description(date_ID , loc_ID, hour, description):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Weather_Description`(`ID`, `dates_ID`, `location_ID`, `hour`, `description`) VALUES (NULL, (SELECT `ID` FROM `Dates` WHERE `ID` = %s LIMIT 1),(SELECT `ID` FROM `Location` WHERE `ID` = %s LIMIT 1), %s, %s)"
        record = (date_ID, loc_ID, hour, description)
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

def insert_Location(country, city):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Location`(`ID`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, %s, %s, NULL, NULL)"
        record = (country, city)
        cursor.execute(query, record)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

def select_Location(city, country):
    try:
        query = "SELECT `ID` FROM `Location` WHERE `City` = %s AND `Country` = %s LIMIT 1"
        # record = (city)
        cursor.execute(query, (city,country,))
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            return -1
        else:
            for row in records:
                # print("Id = ", row[0], )
                return row[0]
                break
        
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

def select_Date(year, month, day):
    try:
        query = "SELECT `ID` FROM `Dates` WHERE `Years` = %s AND `Months` = %s AND `Days` = %s"
        # record = (city)
        cursor.execute(query, (year,month,day,))
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


with open("./weather_description.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    locations = []
    count = 0
    for row in readCSV:
        date = -5

        if (row[0] == "datetime"):
            for x in range(37):
                locations.append(row[x])

            continue
      
        dateTime = (row[0].split())
        date = dateTime[0].split('-')
        time = dateTime[1].split(':')
        year = date[0]
        month = date[1]
        day = date[2]
        hour = time[0]

        date = select_Date(year, month, day)
        if date == -2:
            insert_Date(year, month, day)
        date = select_Date(year, month, day)
        for x in range(37):
            if x == 0:
                continue
            locID = select_Location(locations[x], "United States")
            if locID == -1:
                continue
            # locID = select_Location(locations[x], "United States")
            if row[x] != "":
                insert_Description(date, locID, hour, row[x])
            
        break
        # print(row[0])



if (connection.is_connected()):
    cursor.close()
    connection.close()
