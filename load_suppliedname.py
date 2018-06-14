from datetime import datetime
import csv
import mysql
from mysql import connector
from mysql.connector import errorcode
import string
import random

cnx = connector.connect(user = 'root', password = 'your password', database = 'classdb')
cursor = cnx.cursor()

#SnID (key)
#Name (Btree Index)
#Language
#Status
#Standard
#PlaceID
#SupplierID
#DateSupplied


def date_generator():
    year = random.randint(1994,2019)
    month = random.randint(1,12)
    day = random.randint(1,28 )
    return datetime(year, month, day)

def int_generator():
    return random.randint(1,39)

def string_generator(size = 6, chars = string.ascii_uppercase + string.digits):
    return ''.join([random.choice(chars) for i in range(size)])


with open('load_suppliedname.txt', 'w') as new_file:
    csv_writer = csv.writer(new_file, delimiter = '\t')
    csv_writer.writerow(('SnID','Name','Language','Status', 'Standard', 'PlaceID', 'SupplierID', 'DateSupplied'))
    for i in range(1,40):
        #print(i, string_generator(), string_generator(),string_generator(), string_generator(), int_generator(), int_generator(), date_generator(), int_generator())
        csv_writer.writerow([i,string_generator(),string_generator(),string_generator(),string_generator(),int_generator(),int_generator(),date_generator(),int_generator()])

insert_query = '''
    INSERT INTO SuppliedName(SnID,Name,Language,Status, Standard, PlaceID, SupplierID, DateSupplied) values(%s,%s,%s,%s,%s,%s,%s,%s)
'''
with open('load_suppliedname.txt','r') as file:
    csv_reader = csv.DictReader(file, delimiter = '\t')
    for row in csv_reader:
        #print(row)
        snid = row['SnID']
        name = row['Name']
        langu = row['Language']
        status = row['Status']
        standard = row['Standard']
        placeid = row['PlaceID']
        Supplierid = row['SupplierID']
        datesupp = row['DateSupplied']

        cursor.execute((insert_query), (snid, name, langu, status, standard, placeid, Supplierid, datesupp ))
    cnx.commit()
    cursor.close()
