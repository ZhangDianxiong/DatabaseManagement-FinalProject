USE cs440_group15;

CREATE TABLE Location (
ID int NOT NULL AUTO_INCREMENT,
Country varchar(40),
City varchar(40),
Latitude double(16,9),
Longitude double(16,9),
UNIQUE(Country, City, Latitude, Longitude),
PRIMARY KEY(id, City, Latitude, Longitude)
);

CREATE TABLE Dates (
ID int NOT NULL AUTO_INCREMENT,
Years bigint(20),
Months TINYINT(10),
Days TINYINT(10),
UNIQUE(Years, Months, Days),
PRIMARY KEY(ID)
);

CREATE TABLE Humidity (
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL,
location_ID int NOT NULL,
hour int NOT NULL,
humidity Double(3,1) NOT NULL,
PRIMARY KEY (ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID),
CONSTRAINT date_time_loc UNIQUE(location_ID,dates_ID,hour)
);

CREATE TABLE Weather(
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
location_ID int NOT NULL,
Temperature_Avg_Fahrenheit bigint(4),
DewPointAvgF bigint(5),
Humidity_Avg_Percent bigint(3),
Sea_Level_Pressure_Avg_Inches double(2,2),
Visibility_Avg_Miles bigint(5),
WindAvgMPH bigint(5),
WindGustMPH bigint(5),
PrecipitationSumInches double(2,2),
Weather_event varchar(20),
PRIMARY KEY(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID)
);

CREATE TABLE Heat_Wave (
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
location_ID int NOT NULL, 
Heat_Wave_Index double(3,1) NOT NULL,
PRIMARY KEY(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID)
);

CREATE TABLE Green_House_Gas (
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
location_ID int NOT NULL, 
Emission_value double(12,8) NOT NULL,
PRIMARY KEY(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID)
);


CREATE TABLE Air_Temperature (
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
location_ID int NOT NULL,
Zonal_Winds Double(1,1),
Meridional_Winds Double(1,1),
Air_Temperature Double(3,2),
Sea_Surface_Temperature Double(3,2),
PRIMARY KEY(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID)
);

CREATE TABLE Temperature  (
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
location_ID int NOT NULL,
Minimum_Temperature Decimal(12,8),
Average_Temperature Decimal(12,8),
Maxmum_Temperature Decimal(12,8),
PRIMARY KEY(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID)
);

CREATE TABLE Air_Pollution_Death_Rate(
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
location_ID int NOT NULL,
Deaths Decimal(12,8) Not NULL,
PRIMARY KEY(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID)
);

CREATE TABLE Weather(
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
location_ID int NOT NULL,
Temperature_Avg_Fahrenheit bigint(4),
DewPointAvgF bigint(5),
Humidity_Avg_Percent bigint(3),
Sea_Level_Pressure_Avg_Inches double(2,2),
Visibility_Avg_Miles bigint(5),
WindAvgMPH bigint(5),
WindGustMPH bigint(5),
PrecipitationSumInches double(2,2),
Weather_event varchar(20),
PRIMARY KEY(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID)
);

CREATE TABLE CO2_Emission (
ID int NOT NULL AUTO_INCREMENT,
location_ID int NOT NULL,
dates_ID int NOT NULL, 
Average_Emmision Double(8,2),
Interpolated Double(8,2),
Trend Double(8,2),
Unique(location_ID, dates_ID, Average_Emmision, Interpolated, Trend),
PRIMARY KEY(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID)
);

CREATE TABLE Corvallis_Snow (
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
location_ID int NOT NULL,
Total_Percipitation_days int,
Multiday_precipitation_total double(3,2),
Precipitation double(2,2),
Snowfall int,
Snow_depth double(3,2),
PRIMARY KEY(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID)
);

CREATE TABLE Weather_Description (
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL,
location_ID int NOT NULL,
hour int NOT NULL,
description varchar(100),
PRIMARY KEY (ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID),
CONSTRAINT date_time_loc UNIQUE(location_ID,dates_ID,hour)
);

CREATE TABLE Arctic_See_Ice_Grow (
    dates_ID int NOT NULL ,
    Northern_Hemisphere double(12,2),
    Beaufort_Sea double(12,2),
    Chukchi_Sea double(12,2),
    East_Siberian_Sea double(12,2),
    Laptev_Sea double(12,2),
    Kara_Sea double(12,2),
    Barents_Sea double(12,2),
    Greenland_Sea double(12,2),
    Baffin_Bay_Gulf_of_St_Lawrence double(12,2),
    Canadian_Archipelago double(12,2),
    Hudson_Bay double(12,2),
    Central_Arctic double(12,2),
    Bering_Sea double(12,2),
    Baltic_Sea double(12,2),
    Sea_of_Okhotsk double(12,2),
    Yellow_Sea double(12,2),
    Cook_Inlet double(12,2),
    PRIMARY KEY (dates_ID)
);

CREATE TABLE WBAN_Weather_Station (
ID int NOT NULL AUTO_INCREMENT,
location_ID int NOT NULL,
station_ID int NOT NULL UNIQUE,
PRIMARY KEY (ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID)
);

