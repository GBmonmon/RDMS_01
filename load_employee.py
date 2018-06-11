
from datetime import datetime
import csv
import mysql
from mysql import connector
from mysql.connector import errorcode
import string
import random

cnx = connector.connect(user = 'root', password = 'uvux0623023444', database = 'classdb')
cursor = cnx.cursor()


  #    EmpID int(20) NOT NULL,
  #    Name varchar(60),
  #    TaxID int(20),
  #    Country varchar(60),
  #    HireDate date,
  #    BirthDate date,
  #    Salary int(20) CHECK(Salary>0),
  #    Bonus int(20),
  #    DeptID int(20) NOT NULL,
  #    AddressInfo varchar(60),



def date_generator():
    year = random.randint(1994,2019)
    month = random.randint(1,12)
    day = random.randint(1,28 )
    return datetime(year, month, day)

def int_generator():
    return random.randint(1,80)

def int_generator_fk():
    return random.randint(1,5)

def string_generator(size = 6, chars = string.ascii_uppercase + string.digits):
    return ''.join([random.choice(chars) for i in range(size)])


with open('load_employee.txt', 'w') as new_file:
    csv_writer = csv.writer(new_file, delimiter = '\t')
    csv_writer.writerow(('EmpID','Name','TaxID','Country', 'HireDate', 'BirthDate', 'Salary', 'Bonus', 'DeptID','AddressInfo'))
    for i in range(1,80):
        csv_writer.writerow([i,string_generator(),int_generator(),string_generator(),date_generator(),date_generator(),int_generator(),int_generator(),int_generator_fk(),string_generator()])

insert_query = '''
    INSERT INTO Employee(EmpID, Name, TaxID,Country,HireDate, BirthDate,Salary, Bonus, DeptID, AddressInfo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
'''
with open('load_employee.txt','r') as file:
    csv_reader = csv.DictReader(file, delimiter = '\t')
    for row in csv_reader:
        print(row)
        empid = row['EmpID']
        name = row['Name']
        taxid = row['TaxID']
        country = row['Country']
        hiredate = row['HireDate']
        birth = row['BirthDate']
        salary = row['Salary']
        bonus = row['Bonus']
        dep = row['DeptID']
        address = row['AddressInfo']
        cursor.execute(insert_query,(empid, name, taxid, country, hiredate, birth, salary, bonus, dep, address))
    cnx.commit()
    cursor.close()
