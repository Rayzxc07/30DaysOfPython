from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
import os

app = Flask(__name__)
MONGODB_URI = 'mongodb+srv://<your_username>:<your_password>@<your_cluster_address>/<your_database_name>?retryWrites=true&w=majority'  
try:
    client = pymongo.MongoClient(MONGODB_URI)
    db = client['thirty_days_of_python']
except pymongo.errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
    exit(1)


@app.route('/api/v1.0/students', methods=['GET'])
def get_students():
    try:
        students = list(db.students.find())
        return Response(dumps(students), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')


@app.route('/api/v1.0/students/<id>', methods=['GET'])
def get_student(id):
    try:
        student = db.students.find_one({'_id': ObjectId(id)})
        if student:
            return Response(dumps(student), mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Student not found'}), status=404, mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')


@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    try:
        student_data = request.get_json()
        result = db.students.insert_one(student_data)
        return Response(json.dumps({'inserted_id': str(result.inserted_id)}), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')


@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    try:
        student_data = request.get_json()
        result = db.students.update_one({'_id': ObjectId(id)}, {'$set': student_data})
        if result.modified_count > 0:
            return Response(json.dumps({'message': 'Student updated'}), mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Student not found'}), status=404, mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')


@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    try:
        result = db.students.delete_one({'_id': ObjectId(id)})
        if result.deleted_count > 0:
            return Response(json.dumps({'message': 'Student deleted'}), mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Student not found'}), status=404, mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)