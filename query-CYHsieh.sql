/* Please use the MySQL (version 8)!!!  */


USE classdb;


/*1  Find the elevation and population of a place*/
SELECT elevation, population FROM place LIMIT 1;


/*2. Find a place by a partial name.*/
SELECT P.PlaceID, P.Latitude, P.Longitude, P.Elevation, P.Population, P.Type, P.Country, S.Name
FROM Place AS P JOIN SuppliedName AS S ON P.PlaceID = S.PlaceID
WHERE S.Name LIKE '%JOSE%' LIMIT 1;


/*3. Find a place in a latitude/longitude box (within a range of latitudes/longitudes)*/
/* range_latitude(14~25), range_longitudes(14,25) */
SELECT * FROM Place
WHERE latitude > 14 AND latitude<25 AND longitude > 14 AND longitude < 25
LIMIT 1;


/*4. Find a place by any of its names, listing its type, latitude, longitude, country, population and elevation.*/
SELECT P.Type, P.Latitude, P.Longitude, P.Country, P.Population, P.elevation, S.Name
FROM Place AS P JOIN SuppliedName AS S
ON P.PlaceID = S.PlaceID WHERE name LIKE '%CLARA%' LIMIT 1;


/*5. List all the alternate names of a place, along with language, type of name, and standard.*/
SELECT Status, Language, Type, Standard
FROM Place JOIN SuppliedName
ON Place.PlaceID = SuppliedName.PlaceID LIMIT 1;


/*6. Find the supplier who supplied a particular name, along with other information about the supplier.*/
SELECT s.Name, n.Name, s.Country, s.ReliabilityScore, s.ContactInfo, s.SupplierID
FROM Supplier AS s JOIN SuppliedName AS n
ON s.SupplierID = n.SupplierID WHERE n.Name = 'SAN FRANCISCO';


/*7. Find how many more names are in each language this month (you can assume none are deleted – ever!)*/
SELECT
(SELECT count(*) FROM SuppliedName
WHERE DateSupplied<=CURRENT_DATE())
-
(SELECT count(*) FROM SuppliedName
WHERE DateSupplied<=(DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH )))
AS number_of_added_name_this_month;


/*8. Find how much was paid out to suppliers this month, total*  (2018-6)*/
SELECT SUM(Amount)
FROM payment
WHERE YEAR(Date) = YEAR(CURRENT_DATE()) AND MONTH(Date) = MONTH(CURRENT_DATE());


/*9. Find how much was paid out to suppliers this month, by supplier.*/
SELECT SUM(Amount), Supplier.Name FROM Supplier JOIN Payment
ON Supplier.SupplierID = Payment.SupplierID
WHERE YEAR(Date) = YEAR(CURRENT_DATE()) AND MONTH(CURRENT_DATE())
GROUP BY Supplier.Name;


/*10. Show all employee information in a particular department.*/
SELECT e.EmpID, e.Name, e.TaxID, e.Country, e.HireDate, e.BirthDate, e.Salary, e.Bonus, e.DeptID, e.AddressInfo, d.DeptName FROM
Employee AS e JOIN Department AS d
ON d.DeptID = e.DeptID
WHERE DeptName = 'HR';


/*11. Increase salary by 10% and set bonus to 0 for all employees in a particular department.*/
UPDATE Employee JOIN Department
ON Department.DeptID = Employee.DeptID
SET Salary = Salary*1.1, Bonus = 0
WHERE Department.DeptName = 'HR';


/*12. Show all current employee information sorted by manager name and employee name.*/
SELECT e.EmpID,d.DeptID,e.Name, e.TaxID, e.Country, e.HireDate, e.BirthDate, e.Salary, e.Bonus, e.DeptID, e.AddressInfo
FROM Employee AS e JOIN Department AS d
ON d.DeptID = e.DeptID
ORDER BY d.DeptHeadID, e.Name;


/*13. Show all supplier information sorted by country, including number of names supplied in current month and potential suppliers.*/
SELECT Supplier.*,(SELECT COUNT(*) FROM SuppliedName WHERE SuppliedName.SupplierID = Supplier.SupplierID) AS Total_Name_Supplied
FROM Supplier JOIN SuppliedName
ON Supplier.SupplierID = SuppliedName.SupplierID
WHERE YEAR(SuppliedName.DateSupplied) = YEAR(CURRENT_DATE()) AND MONTH(SuppliedName.DateSupplied) = MONTH(CURRENT_DATE())
GROUP BY Supplier.SupplierID
ORDER BY Supplier.Country;



/*14. Describe how you implemented the access restrictions on the previous page.
DROP ROLE IF EXISTS employee;
CREATE ROLE IF NOT EXISTS employee;                  <-- create employee role
GRANT SELECT ON classdb.Place TO employee;           <-- grant select, which allows employee to see the info to employee
GRANT SELECT ON classdb.SuppliedName TO employee;    <-- grant select, which allows employee to see the info to employee



DROP ROLE IF EXISTS HR_employee;
CREATE ROLE IF NOT EXISTS HR_employee;                      <-- create role called HR_employee
GRANT SELECT, UPDATE ON classdb.Department TO HR_employee;  <-- grant select, update delete to people who are in HR
GRANT SELECT, UPDATE ON classdb.Employee TO HR_employee;    <-- department so they can change the data.

DROP ROLE IF EXISTS manager;
CREATE ROLE IF NOT EXISTS manager;                          <-- create role called manager
GRANT SELECT, UPDATE ON classdb.Employee TO manager;        <-- grant select, update to manager but they cannot delete the data
                                                                meaning they cannot fire the any employees.
*/


/*15. Describe how you implement the constraints shown in the ERD and on the employee info.*/
/* circle in connection means Option so we don't need to put any constraints
   connection without the circle or with a line means It is manditory. So we
   need to put some constraints(Place & SuppliedName, Payment & Supplier, Employee & Department)
   which I set it as NOT NULL. As for (SuppliedName & Supplier) is not manditory, I set the foreign
   key in SuppliedName as ON DELETE SET NULL*/
