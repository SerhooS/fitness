from flask import Flask, request

import sqlite3

app = Flask(__name__)



def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_from_db(query, many=True):
    con = sqlite3.connect('db.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute(query)
    if many:
        res = cur.fetchall()
    else:
        res = cur.fetchone()
    con.close()
    return res


def insert_to_db(query):
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    con.close()


@app.get('/register')
def new_user_register_invitation():
    return f"""<form action='/register' method='post'>
  <label for="login">login:</label><br>
  <input type="text" id="login" name="login"><br>
  <label for="password">password:</label><br>
  <input type="password" id="password" name="password">
  <label for="birth_date">birth_date:</label><br>
  <input type="date" id="birth_date" name="birth_date">
  <label for="phone">phone:</label><br>
  <input type="text" id="phone" name="phone">
  <input type="submit" value="Submit">
</form>"""


@app.post('/register')
def new_user_register():
    form_data = request.form
    insert_to_db(f'insert into user (login, password, birth_date, phone) values (\'{form_data["login"]}\', \'{form_data["password"]}\', \'{form_data["birth_date"]}\', \'{form_data["phone"]}\')')
    return 'new user registered'


@app.post('/login')
def user_login():
    return 'new user is logged in'


@app.get('/login')
def user_login_form():
    return 'please enter credentials'


@app.post('/user')
def add_user_info():
    return 'user data were modified'


@app.get('/user')
def get_info():
    res = get_from_db('select login, phone, birth_date from user where id=1')
    return str(res)


@app.put('/user')
def user_update():
    return 'user info was successfully updated'


@app.post('/funds')
def add_funds():
    return 'user account was successfully funded'


@app.get('/funds')
def add_deposit_info():
    res = get_from_db('select * from funds where user_id=1')
    return str(res)


@app.get('/fitness_center/<gym_id>/services/')
def get_service_list(gym_id):
    res = get_from_db(f'select * from services where gym_id={gym_id}')
    return str(res)


@app.get('/fitness_center/<gym_id>/services/<service_id>')
def get_service_details(gym_id, service_id):
    res = get_from_db(f'select * from services where gym_id={gym_id}, service_id={service_id}')
    return str(res)


@app.get('/fitness_center/<gym_id>/trainer/')
def get_trainers(gym_id):
    res = get_from_db(f'select * from trainer where gym_id={gym_id}')
    return str(res)


@app.get('/fitness_center/<gym_id>/trainer/<coach_id>')
def get_coach_info(gym_id, coach_id):
    res = get_from_db(f'select * from trainer where gym_id={gym_id}, coach_id={coach_id}')
    return str(res)


@app.get('/fitness_center/<gym_id>/trainer/<coach_id>/score')
def get_coach_score(gym_id, coach_id):
    res = get_from_db(f'select * from trainer where gym_id={gym_id}, coach_id={coach_id}')
    return f'fitness center {gym_id} trainer {coach_id} score'


@app.post('/fitness_center/<gym_id>/trainer/<coach_id>/score')
def set_coach_score(gym_id, coach_id):
    return f'fitness center {gym_id} trainer {coach_id} score was added'


@app.put('/fitness_center/<gym_id>/trainer/<coach_id>/score')
def update_coach_score(gym_id, coach_id):
    return f'fitness center {gym_id} trainer {coach_id} score was updated'


@app.get('/user/reservations')
def get_user_reservations():
    res = get_from_db('select * from reservations')
    return str(res)


@app.post('/user/reservations')
def add_reservations():
    return 'user reservation created'


@app.get('/user/reservations/<reservation_id>')
def get_reservation_info(reservation_id):
    res = get_from_db(f'select * from reservations where id={reservation_id}')
    return f'user reservation {reservation_id} info'


@app.put('/user/reservations/<reservation_id>')
def update_reservation(reservation_id):
    return f'user reservation {reservation_id} updated'


@app.delete('/user/reservations/<reservation_id>')
def delete_reservation(reservation_id):
    return f'user reservation {reservation_id} deleted'


@app.get('/user/checkout')
def get_checkout_info():
    res = get_from_db('select * from checkout')
    return str(res)


@app.post('/user/checkout')
def create_checkout():
    return 'checkout created'


@app.put('/user/checkout')
def update_checkout():
    return 'checkout updated'


@app.get('/fitness_center')
def get_fitness_center():
    res = get_from_db('select name, address from fitness_center')
    return str(res)


@app.get('/fitness_center/<gym_id>')
def get_fitness_center_info(gym_id):
    res = get_from_db(f'select name, address from fitness_center where id = {gym_id}', False)
    return str(res)


@app.get('/fitness_center/<gym_id>/loyality_programs')
def get_loyality_programs(gym_id):
    res = get_from_db(f'select * from loyality_programs where id = {gym_id}')
    return str(res)


if __name__ == '__main__':
    app.run()
