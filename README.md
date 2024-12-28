
# Sistem Pemesanan Bioskop  

**Download the code, install the required dependencies, customize, and enjoy! 😄**  

---

## Installation  

1. **Clone the project:**  
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the project directory:**  
   ```bash
   cd <project-folder>
   ```

3. **Install the required dependencies:**  
   ```bash
   python -m pip install -r requirements.txt
   ```

4. **Paste query.sql into MYSQL database**
   ```bash
   CREATE DATABASE cinema_system;
   USE cinema_system;
   
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL UNIQUE,
       password VARCHAR(255) NOT NULL,
       role ENUM('admin', 'customer') NOT NULL
   );
   CREATE TABLE movies (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       genre VARCHAR(100),
       duration INT,  -- duration in minutes
       show_time TIME
   );
   CREATE TABLE bookings (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(100) NOT NULL,
       movie_id INT NOT NULL,
       quantity INT NOT NULL,
       booking_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       FOREIGN KEY (username) REFERENCES users(username),
       FOREIGN KEY (movie_id) REFERENCES movies(id)
   );
   CREATE TABLE movie_schedule (
       id INT AUTO_INCREMENT PRIMARY KEY,
       movie_id INT NOT NULL,
       show_time TIME NOT NULL,
       FOREIGN KEY (movie_id) REFERENCES movies(id)
   );
   ```
   
6. **Run the application:**  
   ```bash
   python main.py
   ```

7. **Customize the code as needed.**

---  
