from flask import render_template, request, redirect, url_for, session
from app import app, mysql

@app.route('/')
def index():
    if 'loggedin' in session:
        return redirect(url_for('tracking'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        if password == app.config['SECRET_KEY']:
            session['loggedin'] = True
            return redirect(url_for('tracking'))
    return render_template('login.html')

@app.route('/tracking', methods=['GET', 'POST'])
def tracking():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        # Handle parcel redirection logic here
        pass
    return render_template('tracking.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    return redirect(url_for('login'))