-- Active: 1742235493618@@localhost@5432@test_db
-- Create the roles table
CREATE TABLE roles(
  id SERIAL PRIMARY KEY,
  name VARCHAR(20) UNIQUE NOT NULL
);

-- Create users table
CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  email VARCHAR(50) UNIQUE NOT NULL,
  password TEXT NOT NULL,
  role_id INT REFERENCES roles(id) ON DELETE CASCADE
);
-- Create countries table
CREATE TABLE countries(
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) UNIQUE NOT NULL
);
-- Create vacations table
CREATE TABLE vacations(
  id SERIAL PRIMARY KEY,
  country_id INT REFERENCES countries(id) ON DELETE CASCADE,
  description TEXT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
  image_url TEXT,
  CHECK (start_date < end_date)
);
-- Create likes table
CREATE TABLE likes(
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  vacation_id INT REFERENCES vacations(id) ON DELETE CASCADE
);
-- Insert roles to roles table
INSERT INTO roles(name) VALUES
  ('admin'),
  ('user');