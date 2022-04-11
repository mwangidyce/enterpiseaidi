from flask import Flask, request, Response, jsonify

from pathlib import Path

from models import StudentModel, db

import datetime

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='dev',
                        SQLALCHEMY_DATABASE_URI='sqlite:///flaskr.sqlite',
                        SQLALCHEMY_TRACK_MODIFICATIONS=False)

db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


# Creation
@app.route('/create_student', methods=['POST'])
def create():
    print(request.data)
    data = request.get_json()
    print(data)
    # Add hardcoded date
    data["dob"] = datetime.date(1994, 1, 1)
    student = StudentModel(**data)
    db.session.add(student)
    db.session.commit()
    return Response(status=201)


# Retrieval
@app.route('/view_students')
def RetrieveDataList():
    students = StudentModel.query.all()
    return jsonify([student.to_dict() for student in students])


# Update
@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    student = StudentModel.query.filter_by(student_id=id).first()
    if student:
        print(request.get_json())
        for key, value in request.get_json().items():
            setattr(student, key, value)
        db.session.commit()
        return Response()
    return f"Student with id = {id} Does not exist"


# Delete
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    student = StudentModel.query.filter_by(student_id=id).first()
    if student:
        db.session.delete(student)
        db.session.commit()
        return Response()
    return f"Student with id = {id} Does not exist"


app.run(host='localhost', port=5000)