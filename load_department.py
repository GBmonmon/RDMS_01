import mysql
from mysql import connector

cnx = connector.connect(user = 'root', password = 'your password', database = 'classdb' )
cursor = cnx.cursor()

 #     DeptID int(20) NOT NULL,
 #     DeptName varchar(60),
 #     DeptHeadID int(20),
 #     DeptHeadUserID int(20),
 #     DeptAA int(20),
 #     ParentDeptID int(20),
 #     Location varchar(60),
 #     DeptType varchar(60),


query1 = '''
   INSERT INTO Department(DeptID, DeptName, DeptHeadID, DeptHeadUserID, DeptAA, ParentDeptID)values(%s,%s,%s,%s,%s,%s)
'''

cursor.execute(query1,(1,'HR', 1,1,1,None ))
cursor.execute(query1,(2,'Marketing',2,2,2,None))
cursor.execute(query1,(3,'PR',3,3,3,2))
cursor.execute(query1,(4,'Sale',4,4,4,2))
cursor.execute(query1,(5,'Engineering',5,5,5,None))
cnx.commit()
