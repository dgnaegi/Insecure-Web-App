from flask import render_template, request, redirect, url_for, session, flash, make_response
from app import app, mysql
import random
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.cookies.get('auth') != app.config['SECRET_KEY']:
            return redirect(url_for('entryprotection'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if request.cookies.get('auth') == app.config['SECRET_KEY']:
        return redirect(url_for('login'))
    return redirect(url_for('entryprotection'))

@app.route('/entry-protection', methods=['GET', 'POST'])
def entryprotection():
    if request.method == 'POST':
        password = request.form['password']
        if password == app.config['SECRET_KEY']:
            response = make_response(redirect(url_for('login')))
            response.set_cookie('auth', password)
            return response
    return render_template('entry_protection.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.cookies.get('auth') != app.config['SECRET_KEY']:
        return redirect(url_for('entryprotection'))
    if request.method == 'POST':
        reference = request.form['reference']
        zip_code = request.form['zip_code']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM parcels WHERE reference=%s AND zip_code=%s", (reference, zip_code))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['reference'] = reference
            return redirect(url_for('tracking'))
        else:
            flash('Invalid login', 'error')
    return render_template('login.html')

@app.route('/tracking', methods=['GET', 'POST'])
@login_required
def tracking():
    if 'reference' not in session:
        return redirect(url_for('login'))
    reference = session['reference']
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        new_address = request.form['new_address']
        cursor.execute("UPDATE parcels SET delivery_address=%s WHERE reference=%s", (new_address, reference))
        mysql.connection.commit()
        flash('Delivery address updated successfully.', 'info')
        return redirect(url_for('tracking'))
    cursor.execute("SELECT * FROM parcels WHERE reference=%s", (reference,))
    parcel = cursor.fetchone()
    cursor.execute("SELECT * FROM parcel_states WHERE parcel_id=%s", (parcel['id'],))
    states = cursor.fetchall()
    return render_template('tracking.html', parcel=parcel, states=states)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('reference', None)
    response = redirect(url_for('entryprotection'))
    response.delete_cookie('auth')
    return response