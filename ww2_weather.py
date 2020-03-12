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

def insert_Temp(loc_ID , date_ID, max, min, avg):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Temperature`(`ID`, `dates_ID`, `location_ID`, `Minimum_Temperature`, `Average_Temperature`, `Maxmum_Temperature`) VALUES (NULL, (SELECT `ID` FROM `Dates` WHERE `ID` = %s LIMIT 1),(SELECT `ID` FROM `Location` WHERE `ID` = %s LIMIT 1), %s, %s, %s)"
        record = (date_ID, loc_ID, min, avg, max)
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



def select_Location(station):
    try:
        query = "SELECT `location_ID` FROM `WBAN_Weather_Station` WHERE `station_ID` = %s"
        # record = (city)
        cursor.execute(query, (station,))
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


with open("./Summary of Weather.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # lats = []
    # lons = []
    count = 0
    for row in readCSV:
        date = -5
        if (row[0] == "STA"):
            continue
        locID = select_Location(row[0])
        # print(locs)
        date = select_Date(('19'+row[9]),row[10],row[11])
        # locs = ('19'+row[9])
        # print(date)
        # print(float(row[6]))
        # print(type(float(row[6])))
        # print(type(row[7]))
        # break
        # print(('19'+row[9]))
        if date == -2:
            insert_Date(('19'+row[9]),row[10],row[11])
        # select_Location(row[1],locs)
        date = select_Date(('19'+row[9]),row[10],row[11])
        print(date)
        insert_Temp(locID, date, row[4],row[5],row[6])
        # break


if (connection.is_connected()):
    cursor.close()
    connection.close()
