import csv
#from __future__ import print_function
import string
import random
passwd = 'your password'
import mysql
from mysql import connector
from mysql.connector import errorcode
#import getpass
#passwd = getpass.getpass() #input


cnx = connector.connect(user = 'root', password = passwd, database = 'classdb')
cursor = cnx.cursor()



#Place: PlaceID (key) Latitude (Btree Index) Longitude (Btree Index) Elevation Population Type Country ASCIIName
'''1, 11, 11, 1, 1, id_generator, id_generator, id_generator'''
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))




with open('load_place.txt', 'w') as new_file:
    csv_writer = csv.writer(new_file, delimiter = '\t')
    csv_writer.writerow(('PlaceID','Latitude','Longitude','Elevation','Population','Type','Country'))

    for i in range(1,40):
        #print(i, 10+i, 10+i, i, i,id_generator(),id_generator(),id_generator())
        csv_writer.writerow((i, 10+i, 10+i, i, i,id_generator(),id_generator()))

insert_query = '''
INSERT INTO Place(PlaceID,Latitude,Longitude,Elevation,Population,Type,Country) VALUES (%s, %s, %s, %s, %s, %s, %s);
'''

with open('load_place.txt', 'r') as file:
    csv_reader = csv.DictReader(file, delimiter = '\t')
    count = 0
    for row in csv_reader:
        placeid = row['PlaceID']
        lat = row['Latitude']
        log = row['Longitude']
        ele = row['Elevation']
        pop = row['Population']
        type = row['Type']
        country = row['Country']


        count +=1
        print(cursor)
        cursor.execute(insert_query,(placeid,lat,log,ele,pop,type,country))
        print('==')
    cnx.commit()
    cursor.close()
