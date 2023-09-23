# Choose Your Menu API

Choose Your Menu API is a Django-based RESTful web API that helps employees make decisions about where to have lunch. It allows you to manage restaurants, menus, and employee votes for menus.
___
## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Before you begin, make sure you have the following installed:

- [Python](https://www.python.org/) (3.6 or higher)
- [Django](https://www.djangoproject.com/)
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/) (or another database of your choice)

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/VTeteruk/choose_your_menu_API
```
2. Navigate to the project directory:

```bash
cd choose_your_menu_API
```
3. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate
```
4. Create a .env file using .env_sample:

5. Build and Run Docker Container: Use Docker Compose to build the API's Docker container and start the API server:
```bash
docker-compose up --build
```


You can now access the API at http://localhost:8000/.
___
# API Documentation
The API documentation is available using the Swagger interface. Access it at http://127.0.0.1:8000/api/schema/swagger.
