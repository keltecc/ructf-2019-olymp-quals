#!/usr/bin/python3

from flask import Flask, request, session
from flask import make_response, abort, redirect, url_for
from flask import render_template, send_from_directory

from os import environ
from hashlib import sha256


app = Flask(__name__, static_folder='./static/')
app.secret_key = 'p13453_d0_n07_h4ck_17'


def check_username(username):
    return username != 'admin'


def calculate_hash(username):
    salt = ''.join(map(''.join, environ.items()))
    data = salt + username + salt
    return sha256(data.encode()).hexdigest()


@app.route('/', methods=['GET', 'POST'])
def index():
    action = request.form.get('action', None)
    username = session.get('username', None)
    if username is None and action != 'login':
        return render_template('login.html')
    if request.method == 'GET' or 'action' is None:
        return render_template('index.html', username=username)
    if action == 'logout':
        del session['username']
        return render_template('login.html')
    if action == 'login':
        if username is not None:
            return render_template('index.html', username=username, error='You have already logged in!')
        username = request.form.get('username', None)
        if username is None:
            return render_template('login.html', error='You should specify a username!')
        if not check_username(username):
            return render_template('login.html', error='Logging in with specified username is highly prohibited!')
        session['username'] = username
        return render_template('index.html', username=username)
    return render_template('index.html', username=username, error='Wrong action! Do you attempt to hack?')


if __name__ == '__main__':
    app.run(port=8888, threaded=True)
