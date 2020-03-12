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

def insert_weather(dId, lId, hum, press, wind_avg, wind_gust, prec, event):
    # INSERT INTO `Location` (`id`, `Country`, `City`, `Latitude`, `Longitude`) VALUES (NULL, NULL, NULL, '-0.02', '-109.46');
    try:
        query = """INSERT INTO `Weather` (`ID`, `dates_ID`, `location_ID`, `Temperature_Avg_Fahrenheit`, `DewPointAvgF`, `Humidity_Avg_Percent`, `Sea_Level_Pressure_Avg_Inches`,
                                            `Visibility_Avg_Miles`, `WindAvgMPH`, `WindGustMPH`, `PrecipitationSumInches`, `Weather_event`)
                                            VALUES (NULL, %s, %s, NULL, NULL, %s, %s, NULL, %s, %s, %s, %s)"""
        record = (dId, lId, hum, press, wind_avg, wind_gust, prec, event)
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
    for _ in range(88003):
        next(readCSV)
    
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

        if(row[16] == "NA"):
            press = None
        else:
            press = 0.029529983071445 * float(row[16])

        if(row[12] == "NA"):
            wind_avg = None
        else:
            wind_avg = 0.621371 * float(row[12])

        if(row[8] == "NA"):
            wind_gust = None
        else:
            wind_gust = 0.621371 * float(row[8])

        if(row[4] == "NA"):
            prec = None
        else:
            prec = 0.0393701 * float(row[4])

        if(row[21]=="Yes"):
            event = "Rain"
        else:
            event = None

        insert_weather(d_id, l_id, row[14], press, wind_avg, wind_gust, prec, event)

        count = count + 1


if (connection.is_connected()):
    cursor.close()
    connection.close()
