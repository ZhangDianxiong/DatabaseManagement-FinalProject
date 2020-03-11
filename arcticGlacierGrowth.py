# This is the script to populate the tabel Arctic_See_Ice_Grow
# the data is from masie_4km_allyears_extent_sqkm.csv

import mysql.connector
from mysql.connector import Error
import csv
import pandas as pd
# set up connection to the php server
connection = mysql.connector.connect(host='classmysql.engr.oregonstate.edu',
                                     user='',
                                     password="",
                                     db="")
# build a cursor based on connection
cursor = connection.cursor()

# read in the csv file which is going to be used to populate the table


def readFile():
    # columnName = ['DAYAndYear', 'Northern_Hemisphere', 'Beaufort_Sea',
    #               'Chukchi_Sea', 'East_Siberian_Sea', 'Laptev_Sea',
    #               'Kara_Sea', 'Barents_Sea', 'Greenland_Sea', 'Baffin_Bay_Gulf_of_St_Lawrence',
    #               'Canadian_Archipelago', 'Hudson_Bay', 'Central_Arctic', 'Bering_Sea',
    #               'Baltic_Sea', 'Sea_of_Okhotsk', 'Yellow_Sea', 'Cook_Inlet']
    # df = pd.read_csv('./masie_4km_allyears_extent_sqkm.csv',
    #                  header=None, skiprows=2, names=columnName)

    with open("./masie_4km_allyears_extent_sqkm.csv") as csv_file:
        render = csv.reader(csv_file)
        next(render)
        next(render)
        counter = 0
        for rows in render:
            print("Loading row #{}/5139".format(counter))
            uploadToDB(rows)
            counter += 1
        print("finish loading data to the data base")


def uploadToDB(rows):
    try:
        query = """INSERT INTO `Arctic_See_Ice_Grow` (`DAYAndYear`, `Northern_Hemisphere`, `Beaufort_Sea`,
                                                    `Chukchi_Sea`, `East_Siberian_Sea`, `Laptev_Sea`,
                                                    `Kara_Sea`, `Barents_Sea`, `Greenland_Sea`, `Baffin_Bay_Gulf_of_St_Lawrence`,
                                                    `Canadian_Archipelago`, `Hudson_Bay`, `Central_Arctic`, `Bering_Sea`,
                                                    `Baltic_Sea`, `Sea_of_Okhotsk`, `Yellow_Sea`, `Cook_Inlet`) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record = tuple(rows)
        cursor.execute(query, record)
        connection.commit()
    except mysql.connector.Error as error:
        print("Insertion error: {}".format(error))


if(connection.is_connected()):
    readFile()
    cursor.close()
    connection.close()
else:
    print("fail to connect to the mysql server")
