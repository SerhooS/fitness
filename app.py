from flask import Flask

app = Flask(__name__)


@app.post('/register')
def new_user_register():  # put application's code here
    return 'new user registered'


@app.get('/register')
def new_user_register_invitation():
    return 'please sign in to register'


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
def user_info():
    return 'user information'


@app.put('/user')
def user_update():
    return 'user info was successfully updated'


@app.post('/funds')
def add_funds():
    return 'user account was successfully funded'


@app.get('/funds')
def add_deposit_info():
    return 'user deposit value'


@app.get('/fitness_center/<gym_id>/services/')
def get_service_list(gym_id):
    return f'fitness center {gym_id} services list'


@app.get('/fitness_center/<gym_id>/services/<service_id>')
def get_service_details(gym_id, service_id):
    return f'fitness center {gym_id} service {service_id} info'


@app.get('/fitness_center/<gym_id>/trainer/')
def get_trainers(gym_id):
    return f'fitness center {gym_id} trainers list'


@app.get('/fitness_center/<gym_id>/trainer/<coach_id>')
def get_coach_info(gym_id, coach_id):
    return f'fitness center {gym_id} trainer {coach_id} info'


@app.get('/fitness_center/<gym_id>/trainer/<coach_id>/score')
def get_coach_score(gym_id, coach_id):
    return f'fitness center {gym_id} trainer {coach_id} score'


@app.post('/fitness_center/<gym_id>/trainer/<coach_id>/score')
def set_coach_score(gym_id, coach_id):
    return f'fitness center {gym_id} trainer {coach_id} score was added'


@app.put('/fitness_center/<gym_id>/trainer/<coach_id>/score')
def update_coach_score(gym_id, coach_id):
    return f'fitness center {gym_id} trainer {coach_id} score was updated'


@app.get('/user/reservations')
def get_user_reservations():
    return 'user reservations list'


@app.post('/user/reservations')
def add_reservations():
    return 'user reservation created'


@app.get('/user/reservations/<reservation_id>')
def get_reservation_info(reservation_id):
    return f'user reservation {reservation_id} info'


@app.put('/user/reservations/<reservation_id>')
def update_reservation(reservation_id):
    return f'user reservation {reservation_id} updated'


@app.delete('/user/reservations/<reservation_id>')
def delete_reservation(reservation_id):
    return f'user reservation {reservation_id} deleted'


@app.get('/user/checkout')
def get_checkout_info():
    return 'checkout information'


@app.post('/user/checkout')
def create_checkout():
    return 'checkout created'


@app.put('/user/checkout')
def update_checkout():
    return 'checkout updated'


@app.get('/fitness_center/')
def get_fitness_center():
    return 'list of fitness centers'


@app.get('/fitness_center/<gym_id>')
def get_fitness_center_info(gym_id):
    return f'fitness center {gym_id} info'


@app.get('/fitness_center/<gym_id>/loyality_programs')
def get_loyality_programs(gym_id):
    return f'fitness center {gym_id} loyality programs list'


if __name__ == '__main__':
    app.run()
