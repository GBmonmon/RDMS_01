/* Please use the MySQL (version 8)!!!  */

show databases;
use classdb;

DROP TABLE IF EXISTS SuppliedName;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Place;
DROP TABLE IF EXISTS Supplier;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Department;


CREATE TABLE IF NOT EXISTS Place(
    PlaceID int(20) NOT NULL,
    Latitude int(20),
    Longitude int(20),
    Elevation int(20),
    Population int(20),
    Type varchar(60),
    Country varchar(60),

    PRIMARY KEY(PlaceID),
    INDEX(Latitude) USING BTREE,
    INDEX(Longitude) USING BTREE


);

CREATE TABLE IF NOT EXISTS Supplier(
    SupplierID int(20) NOT NULL,
    Name varchar(60),
    Country varchar(60),
    ReliabilityScore int(20),
    ContactInfo varchar(60),

    PRIMARY KEY(SupplierID)
);


CREATE TABLE IF NOT EXISTS SuppliedName(
    SnID int(20) NOT NULL,
    Name varchar(60),
    Language varchar(60),
    Status varchar(60),
    Standard varchar(60),
    DateSupplied date,
    PlaceID int(20) NOT NULL, /* FK */
    SupplierID int(20), /* FK */

    PRIMARY KEY(SnID),
    FOREIGN KEY(PlaceID)
    REFERENCES Place(PlaceID),
    FOREIGN KEY(SupplierID)
    REFERENCES Supplier(SupplierID) ON DELETE SET NULL,
    INDEX(Name) USING BTREE

);


CREATE TABLE IF NOT EXISTS Payment(
    Date date,
    Amount int(20),
    SupplierID int(20) NOT NULL,

    FOREIGN KEY(SupplierID)
    REFERENCES Supplier(SupplierID)
);


CREATE TABLE IF NOT EXISTS Department(
    DeptID int(20) NOT NULL,
    DeptName varchar(60),
    DeptHeadID int(20),
    DeptHeadUserID int(20),
    DeptAA int(20),
    ParentDeptID int(20),

    PRIMARY KEY(DeptID)
);


CREATE TABLE IF NOT EXISTS Employee(
    EmpID int(20) NOT NULL,
    Name varchar(60),
    TaxID int(20),
    Country varchar(60),
    HireDate date,
    BirthDate date,
    Salary int(20) CHECK(Salary>0),
    Bonus int(20),
    DeptID int(20) NOT NULL,
    AddressInfo varchar(60),

    PRIMARY KEY(EmpID),
    FOREIGN KEY(DeptID)
    REFERENCES Department(DeptID),
    CHECK(Bonus <= Salary)
);
