#pip install flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# Database simulato
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# Endpoint per ottenere tutti gli utenti
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Endpoint per ottenere un utente specifico
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    return jsonify(user) if user else ("Utente non trovato", 404)

# Endpoint per aggiungere un nuovo utente
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

# Endpoint per aggiornare un utente
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user.update(request.json)
        return jsonify(user)
    return ("Utente non trovato", 404)

# Endpoint per eliminare un utente
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return ("Utente eliminato", 200)

if __name__ == '__main__':
    app.run(debug=True)

