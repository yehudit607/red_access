# Red Access – Interview Exercise for Backend Engineer

This project is composed of two Django services: a Configuration service and an Anti-Virus service. The Configuration service allows for updating and retrieving a list of malicious words, while the Anti-Virus service scans files for the presence of these malicious words. The Anti-Virus service uses Celery to fetch the malicious words every 60 seconds from the Configuration service and updates Redis accordingly, along with the version number.

Requirements
Docker
Docker Compose
Getting Started
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/yourrepository.git
Change directory to the project root:
bash
Copy code
cd yourrepository
Start the services using Docker Compose:
Copy code
docker-compose up -d
This command will start the Configuration and Anti-Virus services, as well as the required PostgreSQL and Redis instances.

Access the Configuration service API endpoints on port 8000, e.g., http://localhost:8000/api/config.

Access the Anti-Virus service API endpoints on port 8001, e.g., http://localhost:8001/api/scan.

API Usage
Configuration Service
To update the configuration, send a PUT request to /api/config with a JSON payload containing the malicious words and the company id:
json
Copy code
{
  "malicious_words": ["word1", "word2"],
  "company_id": 1
}
To retrieve the configuration, send a GET request to /api/config with the version number as a query parameter:
bash
/api/config?version=1
Anti-Virus Service
To scan a file, send a POST request to /api/scan with the file as a form-data payload. The API will return either "clean" or "detected" based on the presence of malicious words in the file.
Implementation Details

The project uses Django for both services. The Configuration service provides an API to update and retrieve the list of malicious words. The Anti-Virus service fetches the malicious words from the Configuration service every 60 seconds using Celery, updating Redis if there is a version difference. The file scanning API in the Anti-Virus service checks for the presence of malicious words fetched from Redis.

When scanning a file, the words will be accessed and scanned accordingly. If a malicious word is found in the file, the API returns "detected", otherwise it returns "clean".
