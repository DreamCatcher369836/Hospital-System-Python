-- Database schema for Hospital Management System

CREATE TABLE Patients (
    patient_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    contact VARCHAR(15),
    address VARCHAR(255)
);

CREATE TABLE Appointments (
    appointment_id INT IDENTITY(1,1) PRIMARY KEY,
    patient_id INT,
    appointment_date DATE,
    appointment_time TIME,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

CREATE TABLE Billing (
    billing_id INT IDENTITY(1,1) PRIMARY KEY,
    patient_id INT,
    billing_amount DECIMAL(10, 2),
    payment_method VARCHAR(50),
    billing_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);
