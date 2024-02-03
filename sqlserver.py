import pyodbc 
import datetime


server = '192.168.145.59'
database = 'ITT'
username = 'grafana'
password = 'Gr@fana!2023'

def insertTemperature(temperatureValue):
# Establishing a connection to the SQL Server
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};\
                        SERVER='+server+';\
                        DATABASE='+database+';\
                        UID='+username+';\
                        PWD='+ password+';\
                        TrustServerCertificate=yes;')

    cursor = cnxn.cursor()


    _table = "iot_Thermometer"
    _columns =["signal", "temperature"]
    now = datetime.datetime.now()
    _signal = now.strftime("%Y-%m-%d %H:%M:%S")
    _temperature = temperatureValue

    query = "INSERT INTO " + _table + "(signal, temperature) VALUES (CONVERT(DATETIME, '" + _signal + "'), CONVERT(FLOAT, '" + _temperature + "'))"
    print("Temperature:" + _temperature + " at: " + _signal)
    cursor.execute(query)
    cnxn.commit()
    cursor.close()

'''
    print("Insert " + _temperature + " at :" + _signal) 
    query = "SELECT * FROM " + _table
    cursor.execute(query)
    # Fetch one row at a time
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

    # Fetch all rows at once
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
'''
   
