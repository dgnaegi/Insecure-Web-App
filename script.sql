CREATE DATABASE IF NOT EXISTS parcel_service;

USE parcel_service;

CREATE TABLE IF NOT EXISTS parcels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reference VARCHAR(9) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    verification_code VARCHAR(6),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    delivery_address VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS parcel_states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parcel_id INT NOT NULL,
    state VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parcel_id) REFERENCES parcels(id)
);

-- Insert dummy data
INSERT INTO parcels (reference, zip_code, phone, verification_code, first_name, last_name, delivery_address) VALUES
('123456789', '12345', '555-1234', NULL, 'John', 'Doe', '123 Elm St'),
('987654321', '54321', '555-4321', NULL, 'Jane', 'Smith', '456 Oak St'),
('111222333', '11111', '555-1111', NULL, 'Alice', 'Johnson', '789 Pine St'),
('444555666', '22222', '555-2222', NULL, 'Bob', 'Brown', '101 Maple St');

INSERT INTO parcel_states (parcel_id, state) VALUES
(1, 'Shipped'),
(1, 'In Transit'),
(1, 'Out for Delivery'),
(2, 'Shipped'),
(2, 'In Transit'),
(3, 'Shipped'),
(4, 'Shipped'),
(4, 'In Transit'),
(4, 'Delivered');