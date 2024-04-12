# Social Media App
## Project Description:
## Description: 

A social media app project built using Django + PostgreSQL and deployed in Docker. The application encompasses typical social media functionalities such as user profiles, post creation, commenting, and likes.

Technologies and skills utilized:

**Django**: Leveraged the Django framework for rapid and scalable web application development.

**PostgreSQL**: Employed PostgreSQL database for its reliability, scalability, and ability to handle large amounts of data.

**Docker**: The project was containerized with Docker, facilitating dependency management and ensuring consistent runtime environments for developers.

**Web** Application: The developed application serves as a full-fledged social media platform, enabling user interaction through post creation, commenting, and liking.


# Installation Instructions:
1 Clone the repository.

2 Make sure you have Docker and docker-compose installed.

3 Start the containers using the command:
  
    docker-compose up -d

# Run migrations to set up the database:

    docker-compose exec django python manage.py migrate

# Usage Instructions:

Navigate to the application's home page by opening a web browser and visiting 

    localhost:8000/account/login/
  
  ![login page](https://github.com/MrW0ody/socialapp/assets/140981101/c2cacfca-9943-4ef6-9c9f-4ed2835e48b5)

    
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

# After passing the following sample credentials, you will be on the home page:

    http://localhost:8000/account/home/

  ![home page after login](https://github.com/MrW0ody/socialapp/assets/140981101/8371f2b2-5329-41e8-a646-55964f72e9fb)

  
# The logged in user's profile page
## In url 9 is user id
  
    http://localhost:8000/account/profile/9/
    
  ![profilepage](https://github.com/MrW0ody/socialapp/assets/140981101/e0de1a68-dff4-433f-b4bd-7c26e02132e2)

# Registration new user

    http://localhost:8000/account/register/
  
  ![register](https://github.com/MrW0ody/socialapp/assets/140981101/c60c0c1f-f8ac-4b0f-9b95-22cdda3a5014)

## After register you can go to profile page and your account will be look like that
  ![registeredprofile](https://github.com/MrW0ody/socialapp/assets/140981101/62c9bbeb-1aea-45c1-b17a-65673efb5eb1)


# Logged user post list
## In url 9 is user id

    http://localhost:8000/feed/list_posts/9/
    
  ![userpostlist](https://github.com/MrW0ody/socialapp/assets/140981101/b5432737-b61d-4fe8-a286-b34208e23c0f)

# Post detail
## In url 48 is post id

    http://localhost:8000/feed/detail_post/48/
    
  ![postdetail](https://github.com/MrW0ody/socialapp/assets/140981101/1861cc9d-009c-456a-830a-088fe5189c7b)

# Add Post

Click button Add post in 
    
    http://localhost:8000/account/profile/9/  
or go to url 
    
    http://localhost:8000/feed/add_post/

  ![addpost](https://github.com/MrW0ody/socialapp/assets/140981101/5cad9fac-3a86-4ffc-93f2-0a9b969e8edc)

added post you can see in

    http://localhost:8000/feed/list_posts/9/

  ![addedpost](https://github.com/MrW0ody/socialapp/assets/140981101/ee54471f-5770-4d6e-baf7-aaf8473596f6)

# Add comment
In url

    http://localhost:8000/feed/detail_post/50/

  ![addingcomment](https://github.com/MrW0ody/socialapp/assets/140981101/1d4be56f-0142-4abf-9f85-a20a1110ef31)

## added comment  
  ![addedcomment](https://github.com/MrW0ody/socialapp/assets/140981101/84788dec-a32e-4283-a752-fb46e06f1e0e)

# Search Post

    http://localhost:8000/feed/search_posts/
    
  ![searchingpost](https://github.com/MrW0ody/socialapp/assets/140981101/cf02dfdb-5015-4c64-8ec8-593c72e0b70e)

## searched post  
  ![searchedpost](https://github.com/MrW0ody/socialapp/assets/140981101/7b8b90e7-1c54-4e50-ad86-cddebbfed476)

# Serch Profile and Follow people
Go to:

    http://localhost:8000/account/follow/
    
and after this click Seach Profile on this page you can also go to profile which you aren't following yet

![follow](https://github.com/MrW0ody/socialapp/assets/140981101/410b0ea6-ead7-4c0f-b817-a889354bafe0)

    http://localhost:8000/account/profile_search/
  ![searchingprofile](https://github.com/MrW0ody/socialapp/assets/140981101/348ffcf6-b10f-41d4-9502-d5a21185004d)

## serched profile  
  ![searchedprofile](https://github.com/MrW0ody/socialapp/assets/140981101/77465f08-7c9e-4844-a2eb-e3b9a0621f43)
