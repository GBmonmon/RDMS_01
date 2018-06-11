import csv
import string
import random
password = 'uvux0623023444'
import mysql
from mysql import connector
from mysql.connector import errorcode

cnx = connector.connect(user = 'root', password = password , database = 'classdb')
cursor =cnx.cursor()


#SupplierID (key)
#Name
#Country
#ReliabilityScore
#ContactInfo


def id_generator(size=6, chars = string.ascii_uppercase + string.digits):
    return ''.join([random.choice(chars) for i in range(size)])


with open('load_supplier.txt','w') as new_file:
    csv_writer = csv.writer(new_file, delimiter = '\t')
    csv_writer.writerow(['SupplierID', 'Name', 'Country', 'ReliabilityScore', 'ContactInfo'])
    for i in range(1,40):
        #print(i, id_generator(), id_generator(), i+60, id_generator(), i+50)
        csv_writer.writerow([i, id_generator(), id_generator(), i+60, id_generator(), i+50])

insert_query = '''
    INSERT INTO Supplier(SupplierID, Name, Country, ReliabilityScore, ContactInfo) VALUES(%s, %s, %s, %s, %s);
'''
with open('load_supplier.txt','r') as file:
    csv_reader = csv.DictReader(file, delimiter = '\t')
    #print(csv_reader)
    for row in csv_reader:
        suppid = row['SupplierID']
        name = row['Name']
        country = row['Country']
        reliab = row['ReliabilityScore']
        coninfo = row['ContactInfo']


        cursor.execute(insert_query, (suppid, name, country, reliab, coninfo))
    cnx.commit()
    cursor.close()
