USE cs440_group15;

CREATE TABLE Location (
ID int NOT NULL AUTO_INCREMENT,
Country varchar(40),
City varchar(40),
Latitude double(16,9),
Longitude double(16,9),
PRIMARY KEY(id, City, Latitude, Longitude)
);

CREATE TABLE Dates (
ID int NOT NULL AUTO_INCREMENT,
Years TINYINT(4),
Months TINYINT(2),
Days TINYINT(2),
PRIMARY KEY(ID)
);

CREATE TABLE WeatherAUS (
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
location_ID int NOT NULL, 
MinTemp double(3,1) NOT NULL, 
MaxTemp double(3, 1) NOT NULL, 
RainFall double(3, 1) NOT NULL, 
Wind_Gust_Direction varchar(4) NOT NULL,
Wind_Gust_Speed bigint(10) NOT NULL,
PRIMARY KEY(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID)
);

CREATE TABLE Mt_Rainier_Weather (
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
location_ID int NOT NULL, 
Average_Temperature double(12,8) NOT NULL,
Relative_Humidity double(12,8) NOT NULL,
Wind_Speed_Average double(12,8) NOT NULL,
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

CREATE TABLE Global_Land_Temperature (
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
location_ID int NOT NULL,
Average_Temperature Double(8,5) NOT NULL,
Average_Temperature_Uncertainty Double(8,5) NOT NULL,
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

CREATE TABLE Air_Pollution_Death_Rate(
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
location_ID int NOT NULL,
Deaths Decimal(12,8) Not NULL,
PRIMARY KEY(ID),
FOREIGN KEY (dates_ID) REFERENCES Dates(ID),
FOREIGN KEY (location_ID) REFERENCES Location(ID)
);

CREATE TABLE Austin_Weather(
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

CREATE TABLE Global_CO2_Emission (
ID int NOT NULL AUTO_INCREMENT,
dates_ID int NOT NULL, 
Average_Emmision Double(8,2),
Interpolated Double(8,2),
Trend Double(8,2),
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