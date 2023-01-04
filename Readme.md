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
