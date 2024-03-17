# Social Media App
## Project Description:
The application simulates the functionality of a typical social media app. It's built using Django framework, PostgreSQL as the database, and HTML/CSS for the front-end. The application is containerized using Docker, orchestrated with docker-compose.

# Installation Instructions:
1 Clone the repository.

2 Make sure you have Docker and docker-compose installed.

3 Build the containers using the command:

    docker compose up -d —build

4 Start the containers using the command:
  
    docker-compose up -d

# Run migrations to set up the database:

    docker-compose exec django python manage.py migrate

# Usage Instructions:

Navigate to the application's home page by opening a web browser and visiting 

    localhost:8000/account/login.
    
# Log in using one of the following sample credentials:

    username: Punk
    password: Sunshine42#2
    
    username: Seth
    password: zAty3s*GP4a9LkQ
    
    username: dean
    password: Sunshine2137
    
    username: roman
    password: Sunshine2222
    
    username: cody
    password: 22Sunshine22

# After following these instructions, test the application
