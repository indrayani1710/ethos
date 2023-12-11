-- Create Ethos Firmware Database if not exists
CREATE DATABASE IF NOT EXISTS ethos_firmware;

-- Create Role Table
CREATE TABLE IF NOT EXISTS role (
    role_id INTEGER PRIMARY KEY,
    role_name TEXT NOT NULL
);

-- Create Mesh Table
CREATE TABLE IF NOT EXISTS mesh (
    mesh_id INTEGER PRIMARY KEY,
    mesh_name TEXT NOT NULL -- it should be UNIQUE
);

-- Create Finger Point Scan Table
CREATE TABLE IF NOT EXISTS finger_point_scan (
    fp_id INTEGER PRIMARY KEY,
    emp_id INTEGER REFERENCES employee(emp_id) UNIQUE,
    LL INTEGER,
    LR INTEGER,
    LM INTEGER,
    LI INTEGER,
    LT INTEGER,
    RL INTEGER,
    RR INTEGER,
    RM INTEGER,
    RI INTEGER,
    RT INTEGER
);

-- Create Employee Table
CREATE TABLE IF NOT EXISTS employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    emp_dob DATE,
    rf_id INTEGER,
    fp_id INTEGER REFERENCES finger_point_scan(fp_id) UNIQUE,
    face_id TEXT,
    mesh_id INTEGER REFERENCES mesh(mesh_id),
    role_id INTEGER REFERENCES role(role_id),
    emp_image BLOB
);