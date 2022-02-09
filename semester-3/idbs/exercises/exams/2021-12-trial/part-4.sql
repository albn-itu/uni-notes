CREATE TABLE Project (
    PID SERIAL PRIMARY KEY,
    Name TEXT
);

CREATE TABLE Researcher (
    RID SERIAL PRIMARY KEY,
    Name TEXT
);

CREATE TABLE Staff (
    SID SERIAL PRIMARY KEY,
    Name TEXT
);

-- There must be at least one researcher working on the project, yet no such relationship exists in SQL
CREATE TABLE WorksOn (
    ID SERIAL PRIMARY KEY,
    RID INTEGER NOT NULL REFERENCES Researcher,
    PID INTEGER NOT NULL REFERENCES Project,
    -- There must be one staff member that evaluates this Project
    -- So the keys below are the "Evaluates" relation
    EvaluatedBySID INTEGER NOT NULL REFERENCES Staff,
    Rating INTEGER
);

CREATE TABLE Article (
    AID SERIAL PRIMARY KEY,
    Year INTEGER
);

CREATE TABLE JournalArticle (
    AID INTEGER NOT NULL PRIMARY KEY REFERENCES Article,
    Journal TEXT,
    Volume INTEGER,
    -- There must be one staff member that manages this JournalArticle
    -- So the below key is the "Manages" relation
    ManagedBtSID INTEGER NOT NULL REFERENCES Staff
);

CREATE TABLE ConferenceArticle (
    AID INTEGER NOT NULL PRIMARY KEY REFERENCES Article,
    Conference TEXT -- Should probably be a reference to a conference table (Out of scope)
);

-- There must be at least one researcher writing the article, yet no such relationship exists in SQL
CREATE TABLE Writes (
     ID SERIAL PRIMARY KEY,
     RID INTEGER NOT NULL REFERENCES Researcher,
     AID INTEGER NOT NULL REFERENCES Article
);
