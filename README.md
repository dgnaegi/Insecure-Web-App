# Parcel Tracking Web Application

This is a simple Flask web application for parcel tracking. The application allows users to log in to view their parcel information and send parcels to different locations. It is designed to demonstrate common web security vulnerabilities for educational purposes.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd parcel-tracking-app
   ```

2. Create a `config.py` file in the root directory with the following content:
   ```python
   PASSWORD = "some_password"
   MYSQL_USER = "your_mysql_user"
   MYSQL_PASSWORD = "your_mysql_password"
   MYSQL_DB = "your_database_name"
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```
   python app/__init__.py
   ```

2. Enter the password "DobbyRocks" when prompted to access the application.

3. Navigate to `http://127.0.0.1:5000` in your web browser to access the parcel tracking page.

## Security Considerations

This application is intentionally designed with vulnerabilities to help engineers learn about web security. Please do not use this application in a production environment.

## License

This project is licensed under the MIT License.