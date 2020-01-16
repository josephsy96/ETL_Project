--SQL Schema 
CREATE Table GDP_TABLE(
    id int Primary Key,
    realtime_start date,
    date DATE,
    value float
);

CREATE TABLE UN_TABLE()
    id int primary key,
    realtime_start date,
    date DATE,
    value float
);

SELECT *
FROM GDP_TABLE
LEFT JOIN UN_TABLE
ON GDP_TABLE.date = UN_TABLE.date;