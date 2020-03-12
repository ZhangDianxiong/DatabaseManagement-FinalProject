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

def insert_weather(dId, lId, temp, wind_gust, prec, event):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = """INSERT INTO `Weather` (`ID`, `dates_ID`, `location_ID`, `Temperature_Avg_Fahrenheit`, `DewPointAvgF`, `Humidity_Avg_Percent`, `Sea_Level_Pressure_Avg_Inches`,
                                            `Visibility_Avg_Miles`, `WindAvgMPH`, `WindGustMPH`, `PrecipitationSumInches`, `Weather_event`)
                                            VALUES (NULL, %s, %s, %s, NULL, NULL, NULL, NULL, NULL, %s, %s, %s)"""
        record = (dId, lId, temp, wind_gust, prec, event)
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

def insert_loc(country, lat, lon):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = "INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, %s, NULL, %s, %s)"
        record = (country, lat, lon)
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


with open("../Weather_Data__Daily__-_Environment_Canada.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count = 0
    for _ in range(55505):
        next(readCSV)

    for row in readCSV:
        if (row[0] == "Row ID"):
            continue

        # date = handleDate(row[0])
        lat = handleLat(row[4])
        lon = handleLon(row[5])

        d_id = find_date(row[11], row[12], row[13])
        l_id = find_loc(lat, lon)

        if (d_id==-1):
            insert_date(row[11], row[12], row[13])
            d_id = find_date(row[11], row[12], row[13])

        if (l_id ==-1):
            insert_loc("Canada", lat, lon)
            l_id = find_loc(lat, lon)

        if(row[18]==''):
            temp = None
        else:
            temp = 1.8 * float(row[18]) + 32

        if(row[27] == '' or row[27] == '<31'):
            wind_gust = None
        else:
            wind_gust = 0.621371 * float(row[27])

        if(row[25] == ""):
            prec = None
        else:
            prec = 0.0393701 * float(row[25])

        if(row[22]=="M" and row[24]=="M"):
            event = None
        elif (row[24] == "T" or row[24] == "S" or row[24] == "L" or row[24] == "F" or row[24] == "E" or row[24] == "A" or row[24] == "C" ):
            event = "Snow"
        elif (row[22] == "T" or row[24] == "S" or row[24] == "L" or row[24] == "F" or row[24] == "E" or row[24] == "A" or row[24] == "C" ):
            event = "Rain"
        else:
            event = None

        insert_weather(d_id, l_id, temp, wind_gust, prec, event)

        count = count + 1

if (connection.is_connected()):
    cursor.close()
    connection.close()
