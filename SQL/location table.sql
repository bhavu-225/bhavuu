CREATE TABLE location(
location_id varchar(5) NOT NULL,
location varchar(50) NOT NULL,
office_size int,
PRIMARY KEY(location_id),
FOREIGN KEY(location) REFERENCES dataflair(emp_id)
);