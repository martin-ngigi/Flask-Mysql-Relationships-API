# FLASK API IN MYSQL 
## Prerequisites
- Python 3.6 and above installed on your computer.
- Postman installed on your computer.
- Apache XAMPP installed on your computer.
- Favourite code editor installed. I use Pycharm community edition which is free.
- Some knowledge of the Python programming language.  
## Steps:
- Create and activate a virtual environment named .venv:

           
            py -3 -m venv .venv
            .venv\scripts\activate
- Update pip in the virtual environment:


            python -m pip install --upgrade pip
- Install Flask in the virtual environment:

            python -m pip install flask
- Install required libraries from the requirements file:

            pip install -r requirements.txt
- Create a new file in your project folder named app.py
- Runs the Flask development server(i.e. app.py):

            flask run
 - Create new dabase in MYSQL xampp database named "flask_mysql_db":

            flask_mysql_rel_db

## API
1. POST -> Create Person
- body ->

            {
                "name": "Ken",
                "age": 25,
                "city": "Nairobi"
            }
- response ->

            {
                "Person": {
                    "age": 25,
                    "city": "Nairobi",
                    "name": "Ken"
                },
                "message": "Person created successfully"
            }

2. GET - get all persons
- endpoint: http://127.0.0.1:5000/persons-get
- response:

            {
                "persons": [
                    {
                        "age": 52,
                        "city": "Kiambu",
                        "id": 1,
                        "name": "David"
                    },
                    {
                        "age": 27,
                        "city": "Nairobi",
                        "id": 2,
                        "name": "Ken"
                    }
                ],
                "success": true,
                "total": 2
            }


3. PATCH - > Update person .
- endpoint -> http://127.0.0.1:5000/persons/1
- body ->

            {
                "name": "David 1",
                "age": 52,
                "city": "Kiambu 1"
            }
- response ->

            {
                "Person": {
                    "age": 52,
                    "city": "Kiambu 1",
                    "name": "David 1"
                },
                "response": "Person Details updated",
                "success": true
            }

4. DELETE -> delete person
- endpoint -> http://127.0.0.1:5000/persons/1
- response:

            {
                "response": "Person deleted successfully",
                "success": true
            }

## POST API
1. 1. POST -> Create a new post:
- full endpoint -> http://127.0.0.1:5000/posts/<int:person_id>
- endpoint -> http://127.0.0.1:5000/posts/1
- Body:

            {
                "content": "Content 1",
                "person_id": 1
            }
-response ->

            {
                "message": "Post created successfully",
                "post": {
                    "content": "Content 4",
                    "person_id": 2
                }
            }

1. 2. GET - get all persons
- endpoint: http://127.0.0.1:5000/persons-get
- response:

            {
                "persons": [
                    {
                        "age": 27,
                        "city": "Nairobi",
                        "id": 2,
                        "name": "Ken",
                        "posts": [
                            {
                                "content": "Content 1",
                                "id": 1
                            },
                            {
                                "content": "Content 1",
                                "id": 4
                            },
                            {
                                "content": "Content 1",
                                "id": 9
                            },
                            {
                                "content": "Content 4",
                                "id": 10
                            }
                        ]
                    },
                    {
                        "age": 23,
                        "city": "Nairobi",
                        "id": 3,
                        "name": "Martin",
                        "posts": [
                            {
                                "content": "Content 1",
                                "id": 5
                            },
                            {
                                "content": "Content 1",
                                "id": 6
                            },
                            {
                                "content": "Content 1",
                                "id": 7
                            }
                        ]
                    }
                ]
            }

2. GET - Get all posts
- endpoint -> http://127.0.0.1:5000/posts-get
- response :

            {
                "posts": [
                    {
                        "content": "Content 1",
                        "id": 1
                    },
                    {
                        "content": "Content 1",
                        "id": 5
                    }
                ]
            }

3. PATCH -> Update Post
- enpoint -> http://127.0.0.1:5000/post/5
- body -> 

            {
                "content": "Content 5"
            }
- response ->

            {
                "Post": {
                    "content": "Content 5"
                },
                "response": "Post Details updated",
                "success": true
            }

4. DELETE -> delete post 
- endpoint -> http://127.0.0.1:5000/post/11
- response ->

            {
                "response": "Post deleted successfully",
                "success": true
            }


## PROFILE API
1. 1. POST -> Create a new PROFILE:
- full endpoint -> http://127.0.0.1:5000/profile/<int:person_id>
- endpoint -> http://127.0.0.1:5000/profile/3
- Body:

            {
                "name": "Profile 3",
                "person_id": 3
            }
- response :

            {
                "message": "Profile created successfully",
                "profile": {
                    "name": "Profile 3",
                    "person_id": 3
                }
            }

2. GET - Get all profile
- endpoint -> http://127.0.0.1:5000/profile-get
- response :

            {
                "profile": [
                    {
                        "id": 1,
                        "name": "Profile 2"
                    },
                    {
                        "id": 5,
                        "name": "Profile 3"
                    }
                ]
            }