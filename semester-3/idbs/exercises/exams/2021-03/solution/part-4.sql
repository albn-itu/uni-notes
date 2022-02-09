CREATE SCHEMA IF NOT EXISTS part4;
SET SEARCH_PATH TO part4;

DROP TABLE IF EXISTS Grades;
DROP TABLE IF EXISTS Examiner;
DROP TABLE IF EXISTS Takes;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Term;

CREATE TABLE Term (
    TID SERIAL PRIMARY KEY,
    description VARCHAR NOT NULL
);

CREATE TABLE Student (
    SID SERIAL PRIMARY KEY,
    startsIn INTEGER NOT NULL REFERENCES Term -- StartsIn relation
);

CREATE TABLE Course (
    CID SERIAL PRIMARY KEY
);

CREATE TABLE Takes (
    SID INTEGER NOT NULL REFERENCES Student,
    CID INTEGER REFERENCES Course,
    TID INTEGER REFERENCES Term,
    room VARCHAR NOT NULL,
    PRIMARY KEY (SID, CID, TID)
);

CREATE TABLE Examiner (
    EID SERIAL PRIMARY KEY
);

CREATE TABLE Grades (
    EID INTEGER REFERENCES Examiner,
    SID INTEGER NOT NULL REFERENCES Student,
    CID INTEGER REFERENCES Course,
    TID INTEGER REFERENCES Term,
    FOREIGN KEY (SID, CID, TID)
        REFERENCES Takes(SID, CID, TID),
    PRIMARY KEY (EID, SID, CID, TID)
);
