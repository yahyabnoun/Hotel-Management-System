# Django Reservation System

This is a Django-based reservation system aimed at simplifying the booking process for events, meetings, and community activities. The project is structured with a main settings file and several apps handling different features of the system.

## Project Structure

### Main Configuration
The main settings for the project are located in the `hms` folder, which contains:
- `settings.py`: Central configuration for the project.
- `urls.py`: URL routing for the entire application.

### Apps
The project includes several apps, each with a specific function:
- **`booking`**: Handles reservations and booking functionality.
- **`hotel`**: Manages hotel-specific data, such as room availability and services.
- **`user_dashboard`**: Allows users to view and manage their bookings.
- **`userauths`**: Manages user authentication, including login, registration, and permissions.

### Database
The project uses **SQLite** as the database (`db.sqlite3`), which stores all user data, reservations, and related information.

### Static and Media Files
- **`static/`**: Contains static assets like CSS, JavaScript, and images.
- **`media/`**: Stores user-uploaded content such as profile pictures or documents.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   https://github.com/yahyabnoun/Hotel-Management-System.git
   cd django-reservation-system
