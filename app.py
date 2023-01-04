from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask import abort
from flask_marshmallow import Marshmallow
import json

app = Flask(__name__)
cors = CORS(app)
ma = Marshmallow(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/flask_mysql_rel_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db  = SQLAlchemy(app)

if __name__=='__main__':
    with app.app_context():
        app.run(debug=True)

#Model
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Post', backref='person')

    def __repr__(self) -> str:
        return f"{self.id}"

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

#SCHEMAS
class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance=True
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance=True
    posts = ma.Nested(PostSchema, many=True)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return jsonify({"message": "Hello, Its Wainaina"})

#POST persons
#http://127.0.0.1:5000/persons
@cross_origin()
@app.route("/persons", methods=["POST"])
def create_person():
    data = request.json

    name = data['name']
    age = data['age']
    city = data['city']

    person = Person(name=name, age=age, city=city)
    db.session.add(person)
    db.session.commit()

    return jsonify({"message": "Person created successfully", "Person": data})

'''
#GET PERSONS
#http://127.0.0.1:5000/persons-get
@cross_origin()
@app.route("/persons-get", methods=["GET"])
def get_persons():
    all_persons = []
    persons = Person.query.all()
    for person in persons:
        results = {
            "id": person.id,
            "name": person.name,
            "age": person.age,
            "city": person.city,
        }
        all_persons.append(results)

    return jsonify(
        {
            "success": True,
            "persons": all_persons,
            "total": len(persons)
        }
    )
'''

#GET PERSONS
#http://127.0.0.1:5000/persons-get
@cross_origin()
@app.route("/persons-get", methods=["GET"])
def get_persons():
    persons = Person.query.all()
    persons_schema = PersonSchema(many=True)
    dump_data = persons_schema.dump(persons)
    return jsonify({'persons' : dump_data})


# UPDATE person
#http://127.0.0.1:5000/persons/1
@cross_origin()  
@app.route("/persons/<int:id>", methods = ["PATCH"])
def update_person(id):
    person = Person.query.get(id)
    name = request.json['name']
    age = request.json['age']
    city = request.json['city']

    if person is None:
        abort(404)
    else:
        person.name = name
        person.age = age
        person.city = city
        db.session.add(person)
        db.session.commit()
        return jsonify({"success": True, "response": "Person Details updated", "Person": request.json})

#DEEETE Person
#http://127.0.0.1:5000/persons/1
@cross_origin()  
@app.route("/persons/<int:id>", methods = ["DELETE"])
def delete_persons(id):
    person = Person.query.get(id)

    if person is None:
        abort(404)
    else:
        db.session.delete(person)
        db.session.commit()
        return jsonify({"success": True, "response": "Person deleted successfully"})



#########################################################################################################################################
#POSTS


#POST persons
#http://127.0.0.1:5000/posts/1
@cross_origin()
@app.route("/posts/<int:person_id>", methods=["POST"])
def create_post(person_id):
    person = Person.query.get(person_id)

    if person is None:
        abort(404, "Error: No person with that id ")
    else:
        data = request.json

        content = data['content']
        person_id = data['person_id']

        post = Post(content=content, person_id=person_id)
        db.session.add(post)
        db.session.commit()
        return jsonify({"message": "Post created successfully", "post": data})
