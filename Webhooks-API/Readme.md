# Procore Integration with Flask

## Overview
This project is a Python Flask-based application that integrates with the **Procore API** to manage project data. It enables tracking, importing, and processing of project-related events such as creation, updates, and deletions.

## Features
1. **Procore Registration**
   - Register the system to receive notifications (webhooks) from Procore for project-related events.

2. **Import Previous Projects**
   - An API to import all historical projects for a specific company ID from the Procore API.
   - Store project details in a PostgreSQL database.

3. **Handle Notifications**
   - Process notifications for newly created, updated, or deleted projects from Procore.
   - Store changes in the database.

4. **Secure and Robust API**
   - Secure endpoints.
   - Comprehensive error handling for all APIs.

## Setup
### Prerequisites
- Python 3.8+
- PostgreSQL
- Git
- Procore API credentials (Client ID, Client Secret, and Webhook URL)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo.git
   cd project_name
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Linux/MacOS
   venv\Scripts\activate      # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:
   - Create a PostgreSQL database for the project.
   - Update the database connection string in `config.py`:
     ```python
     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/db_name'
     ```

5. Apply database migrations to set up tables:
   ```bash
   flask db upgrade
   ```

6. Run the application:
   ```bash
   python app.py
   ```
   The app will be available at `http://localhost:5000`.

## API Endpoints
### 1. **Register for Procore Webhooks**
   **Endpoint:** `/register-webhook`
   **Method:** `POST`
   **Description:** Registers the system to receive webhook notifications from Procore for project events.

### 2. **Import Projects**
   **Endpoint:** `/import-projects`
   **Method:** `GET`
   **Parameters:**
   - `company_id` (required): The company ID to fetch projects for.

   **Description:** Imports all previous projects for a specific company ID from the Procore API and stores them in the database.

### 3. **Handle Webhook Notifications**
   **Endpoint:** `/webhook`
   **Method:** `POST`
   **Description:** Processes notifications for new, updated, or deleted projects from Procore and updates the database accordingly.

### 4. **Fetch All Projects**
   **Endpoint:** `/projects`
   **Method:** `GET`
   **Description:** Fetches all project details stored in the database.

## Security
- Use API keys or OAuth tokens to secure endpoints.
- Validate webhook payloads using the Procore signature header to ensure authenticity.

## Error Handling
- Comprehensive error handling for all endpoints.
- Returns appropriate HTTP status codes and messages:
  - `200 OK` for successful requests.
  - `400 Bad Request` for invalid inputs.
  - `500 Internal Server Error` for unexpected errors.

## Project Structure

project_name/
├── app/
│   ├── _init_.py        # Initialize Flask app and configurations
│   ├── config.py          # Configuration settings for Flask and DB
│   ├── models.py          # SQLAlchemy models (e.g., Project)
│   ├── routes/
│   │   ├── _init_.py    # Initialize blueprint
│   │   ├── webhooks.py    # Routes for webhook handling
│   │   ├── import.py      # Routes for importing projects
│   ├── utils/
│   │   ├── _init_.py    # Utility module initialization
│   │   ├── locking.py     # File locking utilities
│   ├── services/
│       ├── procore_api.py # Functions for interacting with Procore API
├── config.py             # Configuration settings for Flask and DB
├── requirements.txt      # Python dependencies
├── run.py                # Entry point to start the application
├── .env                  # Environment variables (optional, if using)
├── README.md             # Documentation about the project


## Running in Production
- Use a production WSGI server like **Gunicorn** or **Waitress**:
  ```bash
  waitress-serve --host=0.0.0.0 --port=5000 app:app
  ```
- Use HTTPS for secure communication.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to suggest improvements.

