from flask import Flask, request, render_template, redirect
from flask_ngrok import run_with_ngrok
from data import db_session
from data.simple_table import *

app = Flask(__name__)


run_with_ngrok(app)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        session = db_session.create_session()
        my_table = session.query(SimpleTable).all()
        return render_template('index.html', title='Домашняя страница', my_table=my_table)
    elif request.method == 'POST':
        session = db_session.create_session()
        session.query(SimpleTable).delete()
        session.commit()
        for i in range(1, 6):
            user = SimpleTable()
            user.col1 = request.form['col1_' + str(i)]
            user.col2 = request.form['col2_' + str(i)]
            user.col3 = request.form['col3_' + str(i)]
            user.col4 = request.form['col4_' + str(i)]
            user.col5 = request.form['col5_' + str(i)]
            session.add(user)
            session.commit()
        return redirect('/')


@app.route("/edit_table/<int:row>/<int:col>/<value>")
def edit_table(row, col, value):
    session = db_session.create_session()
    user = session.query(SimpleTable).filter(SimpleTable.id == row).first()
    if col == 1:
        user.col1 = value
    elif col == 2:
        user.col2 = value
    elif col == 3:
        user.col3 = value
    elif col == 4:
        user.col4 = value
    elif col == 5:
        user.col5 = value
    session.commit()
    return redirect('/')


if __name__ == '__main__':
    db_session.global_init("db/table.sqlite")
    app.run()
