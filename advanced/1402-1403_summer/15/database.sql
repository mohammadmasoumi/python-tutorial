-- Create database
CREATE DATABASE university;
CREATE TABLE Student (
    SID INT,
    NationalID VARCHAR(10),
    Name VARCHAR(255),
    Age INT,
    Address VARCHAR(255),
    Level VARCHAR(4),
    City VARCHAR(255)
);
-- Define level
-- BS, MS, PHD  1M * 4 bytes
-- enhance readability
-- disk consuming
-- 1, 2, 3      1M * 1 bytes
-- decrease readability
-- low disk usage
-- INT
-- INT32, INT64
CREATE TABLE Professor (
    PID INT,
    NationalID VARCHAR(10),
    Name VARCHAR(255),
    Age INT,
    Address VARCHAR(255),
    Degree VARCHAR(10),
    City VARCHAR(255)
);
CREATE TABLE Guide (
    PID INT,
    -- PK(Primary Key)
    SID INT,
    StartDate TIMESTAMP,
    EndDate TIMESTAMP
);
CREATE TABLE Course (
    CID INT,
    DID INT,
    Name VARCHAR(255),
    Type VARCHAR(255),
    Unit INT,
    Content VARCHAR(255)
);
CREATE TABLE CoursePresentation (
    CPID INT,
    PID INT,
    -- FK(ForeignKey)
    CID INT,
    Semester VARCHAR(255)
);
CREATE TABLE Enroll (SID INT, CPID INT, Score INT);
CREATE TABLE Department (
    DID INT,
    Name VARCHAR(255),
    Location VARCHAR(255),
    Detail VACUUM(255)
);
CREATE TABLE DepartmentMembership (
    DMID INT,
    PID INT,
    DID INT,
    StartDate TIMESTAMP,
    EndDate TIMESTAMP
);
CREATE TABLE DepartmentManagement (
    DMAID INT,
    PID INT,
    DID INT,
    StartDate TIMESTAMP,
    EndDate TIMESTAMP
);
-- CREATE TABLE CourseDepartmentDefine (
--     CDDID INT,
--     DID INT,
--     CID INT,
--     Content VARCHAR(255)
-- );
CREATE TABLE StudentDepartmentMembership (
    MID INT,
    SID INT,
    DID INT,
    StartDate TIMESTAMP
)