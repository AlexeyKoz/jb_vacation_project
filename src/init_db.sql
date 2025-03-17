-- After creating the database,
-- run this script to initialize the tables and populate them with data.

-- Create the users table
CREATE TABLE roles(
  id SERIAL PRIMARY KEY,
  name VARCHAR(20) UNIQUE NOT NULL
);

-- Create user form
CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  email VARCHAR(50) UNIQUE NOT NULL,
  password TEXT NOT NULL,
  role_id INT REFERENCES roles(id) ON DELETE CASCADE
);

-- Create the countries table
CREATE TABLE countries(
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) UNIQUE NOT NULL
);

-- Create the vacations table
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

-- Create the likes table
CREATE TABLE likes(
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  vacation_id INT REFERENCES vacations(id) ON DELETE CASCADE
);


-- Insert data into Roles tables
INSERT INTO roles(name) VALUES
  ('admin'),
  ('user');


-- Insert data into the users table
INSERT INTO users (first_name, last_name, email, password, role_id) VALUES
('Alexey', 'Kozlov', 'alexey.kozlov@example.com', 'hashed_password_1', 1),
('Noa', 'Kirell', 'noa.kirell@example.com', 'hashed_password_5', 2),
('Guy', 'Baskin', 'guy.baskin@example.com', 'hashed_password_6', 2),
('Roi', 'Sirota', 'roi.sirota@example.com', 'hashed_password_7', 2),
('Maor', 'Shlomo', 'maor.shlomo@example.com', 'hashed_password_8', 2),
('Doron', 'Shalom', 'doron.shalom@example.com', 'hashed_password_9', 2);

-- Insert data into countries table
INSERT INTO countries (name) VALUES
    ('Israel'),
    ('Ukraine'),
    ('Russia'),
    ('France'),
    ('Spain'),
    ('Italy'),
    ('USA'),
    ('Germany'),
    ('Turkey'),
    ('Greece');

-- Insert data into the vacations table
INSERT INTO vacations (country_id, description, start_date, end_date, price, image_url) VALUES
    (1, 'Beach vacation on the Mediterranean coast in Tel Aviv', '2025-06-01', '2025-06-15', 1500.00, 'tel_aviv.jpg'),
    (2, 'Ski resort Bukovel in the Carpathians', '2025-12-20', '2026-01-05', 1200.00, 'bukovel.jpg'),
    (3, 'Golden Ring of Russia Tour', '2025-07-10', '2025-07-20', 1300.00, 'golden_ring.jpg'),
    (4, 'French Riviera: Vacation in Nice', '2025-08-01', '2025-08-14', 2000.00, 'nice.jpg'),
    (5, 'Barcelona and Costa Brava: Beach and cultural tour', '2025-07-15', '2025-07-30', 1800.00, 'barcelona.jpg'),
    (6, 'Rome and Venice: Excursion tour through Italy', '2025-09-10', '2025-09-25', 2200.00, 'rome_venice.jpg'),
    (7, 'Miami Beach: A sunny paradise in Florida', '2025-05-05', '2025-05-20', 2500.00, 'miami.jpg'),
    (8, 'Bavarian Alps: Mountain retreat in Germany', '2025-10-01', '2025-10-15', 1600.00, 'bavaria.jpg'),
    (9, 'Antalya: Five-star holiday in Turkey', '2025-06-10', '2025-06-25', 1400.00, 'antalya.jpg'),
    (10, 'Santorini Island: A romantic getaway', '2025-07-01', '2025-07-15', 1700.00, 'santorini.jpg'),
    (6, 'Tuscany: Wine and gastronomy tour in Italy', '2025-09-01', '2025-09-15', 2000.00, 'tuscany.jpg'),
    (5, 'Madrid and Seville: Cultural journey through Spain', '2025-10-05', '2025-10-20', 1900.00, 'madrid_seville.jpg');

