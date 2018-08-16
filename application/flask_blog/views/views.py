from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import appa
from functools import wraps


def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner


@appa.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != appa.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != appa.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')


@appa.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))