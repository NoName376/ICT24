-- Table deleting
-- Delete existing tables if they exist
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Shippings;




-- Create the Companies table
CREATE TABLE companies (
    company_id INT PRIMARY KEY,
    company_name VARCHAR(255)
);

-- Create the Vehicles table
CREATE TABLE vehicles (
    vehicle_id INT PRIMARY KEY,
    vehicle_type VARCHAR(255),
    company_id INT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

-- Create the Cities table
CREATE TABLE cities (
    city_id INT PRIMARY KEY,
    city_name VARCHAR(255),
    country_id INT
);

-- Create the Routes table
CREATE TABLE routes (
    route_id INT PRIMARY KEY,
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

-- Create the Transport_Types table
CREATE TABLE transport_types (
    transport_id INT PRIMARY KEY,
    transport_name VARCHAR(255),
    average_speed DECIMAL
);






-- Insert data into Companies
INSERT INTO companies VALUES (1, 'Alpha Transport'), (2, 'Beta Logistics'), (3, 'Gamma Transit'), (4, 'Delta Movers'), (5, 'Echo Vehicles');

-- Insert data into Vehicles
INSERT INTO vehicles VALUES (1, 'Bus', 1), (2, 'Truck', 2), (3, 'Van', 1), (4, 'Car', 3), (5, 'Motorbike', 5);

-- Insert data into Cities
INSERT INTO cities VALUES (1, 'New York', 1), (2, 'San Francisco', 2), (3, 'Chicago', 3), (4, 'Los Angeles', 4), (5, 'Austin', 5);

-- Insert data into Routes
INSERT INTO routes VALUES (1, 1), (2, 2), (3, 3), (4, 4), (5, 5);

-- Insert data into Transport_Types
INSERT INTO transport_types VALUES (1, 'Bus', 60.0), (2, 'Train', 120.0), (3, 'Plane', 800.0), (4, 'Ship', 30.0), (5, 'Car', 90.0);





-- a)
SELECT c.company_name, COUNT(v.vehicle_id) AS number_of_vehicles
FROM Companies c 
LEFT JOIN Vehicles v ON c.company_id = v.company_id
GROUP BY c.company_name;

-- b)
SELECT company_name 
FROM Companies 
WHERE company_name LIKE 'A%';

-- с)
SELECT city_name 
FROM Cities 
WHERE country_id BETWEEN 3 AND 10;

-- d)
SELECT vehicle_id, vehicle_type FROM Vehicles;

-- e)
SELECT r.route_id, c.city_name 
FROM Routes r
JOIN Cities c ON r.city_id = c.city_id;

-- f)
SELECT * FROM Transport_Types;

UPDATE Transport_Types 
SET average_speed = average_speed + 10 
WHERE average_speed < 100;

SELECT * FROM Transport_Types;

-- g)
SELECT c.city_name, c.country_id FROM Cities c;

-- h)
SELECT * FROM Transport_Types;
