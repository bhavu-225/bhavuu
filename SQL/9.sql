CREATE TABLE location_1(
location_id varchar(5) NOT NULL,
location varchar(50) NOT NULL,
office_size int,
PRIMARY KEY(location_id),
FOREIGN KEY(location) REFERENCES dataflair(locationlocation)
);