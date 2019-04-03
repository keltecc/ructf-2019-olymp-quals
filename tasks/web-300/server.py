#!/usr/bin/python3

import re

from flask import Flask, request, session, redirect, url_for, render_template, make_response
from utils import check_username, check_filename, check_content, enumerate_files, read_file, write_file


app = Flask(__name__, static_url_path='', static_folder='./static/')
app.secret_key = 'p13453_d0_n07_h4ck_17'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    username = request.form.get('username', None)
    if request.method == 'GET' or username is None:
        return render_template('login.html')
    if not check_username(username):
        return render_template('login.html', error='Logging in with specified username is highly prohibited!')
    session['username'] = username
    return redirect(url_for('index'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        del session['username']
    return redirect(url_for('index'))


@app.route('/read', methods=['GET'])
def read():
    username = session.get('username', None)
    filename = request.args.get('filename', None)
    if username is None:
        return make_response('error: you must be logged in!')
    if filename is None:
        return make_response('error: specify a filename!')
    return make_response(read_file(username, filename))


@app.route('/', methods=['GET', 'POST'])
def index():
    username = session.get('username', None)
    if username is None:
        return redirect(url_for('login'))
    files = enumerate_files(username)
    filename = request.form.get('filename', None)
    content = request.form.get('content', None)
    if request.method == 'GET' or filename is None or content is None:
        return render_template('index.html', files=files)
    if not check_filename(filename):
        return render_template('index.html', files=files, error='Invalid filename!')
    if not check_content(content):
        return render_template('index.html', files=files, error='Content is too long or invalid!')
    write_file(username, filename, content)
    return render_template('index.html', files=enumerate_files(username))


def _put_flag():
    filename = 'flag.txt'
    with open(filename, 'r') as file:
        write_file('admin', filename, file.read())


_put_flag()
if __name__ == '__main__':
    app.run('0.0.0.0', port=8888, threaded=True)
