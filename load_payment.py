from datetime import datetime
import csv
import string
import random
import mysql
from mysql import connector
from mysql.connector import errorcode

cnx = connector.connect(user = 'root', password = 'your password', database = 'classdb')
cursor = cnx.cursor()

#SupplierID
#Date
#Amount


def date_generator():
    year = random.choice(range(1994,2018))
    month = random.choice(range(1,13))
    day = random.choice(range(1,29))
    return datetime(year, month, day)
print(date_generator())

def id_generator(sizes = 6, chars = string.ascii_uppercase+string.digits):
    return ''.join([random.choice(chars) for i in range(sizes)])

def int_generator():
    int_generator = random.randint(1,39)
    return int_generator


with open('load_payment.txt', 'w') as new_file:
     csv_writer = csv.writer(new_file, delimiter = '\t')
     csv_writer.writerow(['SupplierID', 'Date', 'Amount'])
     for i in range(1,40):
        print(int_generator(), date_generator(), int_generator(), i)
        csv_writer.writerow([int_generator(), date_generator(), int_generator(), i])

insert_query = '''
    insert into Payment(SupplierID, Date, Amount) VALUES(%s,%s,%s);
'''

with open('load_payment.txt','r') as file:
    csv_reader =csv.DictReader(file, delimiter = '\t')
    for row in csv_reader:
        suppid = row['SupplierID']
        dat = row['Date']
        amount = row['Amount']

        cursor.execute(insert_query,(suppid, dat, amount))
    cnx.commit()
    cursor.close()
