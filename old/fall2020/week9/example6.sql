CREATE TABLE [PROJECTS] (  
    [ProjectNum] TEXT  NOT NULL PRIMARY KEY,
    [ProjectTitle] TEXT NOT NULL,
    [ProjectMgr] TEXT NOT NULL,
    [Phone] INTEGER NOT NULL
);

INSERT INTO PROJECTS VALUES("30-452-T3", "STAR manual", "Garrison", "2756");
INSERT INTO PROJECTS VALUES("30-457-T3", "ISO procedures", "Jacanda", "2954");
INSERT INTO PROJECTS VALUES("30-482-TC", "Web site", "Friedman", "2846");
INSERT INTO PROJECTS VALUES("31-124-T3", "Employee handbook", "Jones", "3102");
INSERT INTO PROJECTS VALUES("31-238-TC", "STAR prototype", "Garrison", "2756");
INSERT INTO PROJECTS VALUES("31-241-TC", "New catalog", "Jones", "3102");
INSERT INTO PROJECTS VALUES("35-152-TC", "STAR pricing", "Vance", "3022");
INSERT INTO PROJECTS VALUES("36-272-TC", "Order system", "Jacanda", "2954");

