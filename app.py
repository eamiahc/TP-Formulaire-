from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import hashlib
import sqlite3
import re

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_strong_password(password):
    # Au moins 8 caractères, une lettre majuscule et un chiffre
    if re.fullmatch(r'^(?=.*[A-Z])(?=.*\d).{8,}$', password):
        return True
    return False

def add_user(username, password):
    # Vérifiez si le mot de passe est fort
    if not is_strong_password(password):
        return 'weak_password'
    
    hashed_password = hash_password(password)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True

def check_login(username, password):
    hashed_password = hash_password(password)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    user = cursor.fetchone()
    conn.close()
    return user



app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form['username']
        password = request.form['password']
        if action == 'login':
            if check_login(username, password):
                flash("Vous êtes connecté", "success")
            else:
                flash("Identifiant ou mot de passe incorrect", "error")
        elif action == 'register':
            result = add_user(username, password)
            if result == True:
                flash("Compte créé avec succès", "success")
            elif result == 'weak_password':
                flash("Le mot de passe doit contenir au moins 8 caractères, une lettre majuscule et un chiffre", "error")
            else:
                flash("L'identifiant existe déjà ou il y a eu une erreur", "error")
    return render_template('login.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
