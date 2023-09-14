from flask import Flask, request, jsonify
import mysql.connector as mycon

app = Flask(__name__)

db = mycon.connect(
    host="localhost",
    user="root",
    password="IAmAtMySQL1101!!!",
    database="boating"
)

@app.route("/", methods=['GET'])
def home():
    return "Hello World"

@app.route("/user", methods=['POST'])
def create_user():
    data = request.get_json()
    cursor = db.cursor()
    cursor.execute("INSERT INTO user (user_id, username, email, password, contact) VALUES ({}, '{}', '{}', '{}', '{}')".format(
        data['user_id'],
        data['username'],
        data['email'],
        data['password'],
        data['contact']
    ))
    db.commit()
    cursor.close()
    return jsonify({"message": "User created successfully"}), 201

@app.route('/user', methods=['GET'])
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user")
    items = cursor.fetchall()
    cursor.close()
    return jsonify(items), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user WHERE user_id = {}".format(user_id))
    item = cursor.fetchone()
    cursor.close()
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404
    
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM user WHERE user_id = {}".format(user_id))
    db.commit()
    cursor.close()
    return jsonify({"message": "Item deleted successfully"}), 204

@app.route('/user', methods=['DELETE'])
def delete_all_users():
    cursor = db.cursor()
    cursor.execute("DELETE FROM user")
    db.commit()
    cursor.close()
    return jsonify({"message": "All items deleted successfully"}), 204

if __name__ == "__main__":
    app.run(debug=True)